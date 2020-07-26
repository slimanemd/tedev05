#
from flask import render_template, request, flash, url_for
from markupsafe import Markup
from werkzeug.utils import redirect

#
from tedev.core.models.db_initializer import db
from tedev.data.data_general import model01s


# fill_entity_from_form: on post request, fill entity fields from posted form fields
# from tedev.utiles import send_email

#
def fill_entity_from_form(entity, entity_id, entity_name):
    keys = list(request.form.keys())
    for attribute in model01s['tedevB']['fields']:
        if attribute != 'id' and attribute in keys:
            setattr(entity, attribute, request.form[attribute])
    entity_data = None if entity_id == None else {'id': entity_id, 'name': entity.name}  # return entity, entity_data
    return entity_data


#
def fill_form_from_entity(EntityForm, Entity, entity_id, entity_name):
    entity_form =  EntityForm()
    if entity_id != None:  #if request.method == 'POST':
        entity = Entity.query.get(entity_id)
        if entity:
            fields = model01s['tedevB']['fields']
            print(fields)
            for attribute in fields:
                if attribute != 'id' and hasattr(entity,attribute):
                    entity_form[attribute].data = getattr(entity, attribute)
    return entity_form, { 'id': entity_id, 'name' : entity_name }


#
def process_core(Entity, entity_id, pform):
    entity = Entity(pform)  # entity_data = fill_entity_from_form(entity, None, entity_name)  # (001)  get_new_entity 003
    if entity_id == None: db.session.add(entity)
    db.session.commit()


#
def create_or_edit_entity(EntityForm, Entity, entity_name, entities_name, entity_id, entity_form_data):
    print(Entity)
    operation = 'create' if entity_id == None else 'update'   ; print(operation)

    entity_form, entity_data = fill_form_from_entity(EntityForm, Entity, entity_id, entity_name)
    if request.method == 'POST':
        if entity_form.validate_on_submit():   # instanciated the entity fill its fields with values if the editing           # persiste the modification
            try:
                process_core(Entity, entity_id, request.form)  #process_core(request.form)

                msg01 = entity_name + ' was successfully ' + operation + 'd!, check your email please' # \n' + result
                flash(msg01)
                return redirect('/?registred=Yes' if entity_name == 'participant' else '/')
            except:          # on unsuccessful db insert, flash an error instead.
                msg01 = 'An error occurred. ' + entity_name + ' could not be ' + operation + 'd!.' + str(entity_form.errors)
                flash(msg01)
                return render_template('pages/index.html')
        else:   # for err in form.errors: Markup("<h1>Voila! Platform is ready to used</h1>")
            msg01=entity_name + ' erreur de validation lors de l ' + operation + '. Les erreurs:<br>' + str(entity_form.errors)
            flash(Markup(msg01.replace(',', ',<br>').replace('{', '').replace('}', '')))

    #
    entity_data['form_data'] = entity_form_data
    entity_data['entities_name'] = entities_name
    entity_data['entity_name'] = entity_name
    entity_data['Entity_name'] = entity_name.capitalize()
    entity_data['show_navbar'] = 'N'

    #'forms/' + ('new' if operation == 'create' else 'edit') + '_' + entity_name + '.html',
    return render_template(
        'forms/new_entity.html',
        form = entity_form,
        data = entity_data )
