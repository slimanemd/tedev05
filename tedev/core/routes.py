from flask import request, render_template

#
from tedev.app import app
from tedev.core.models.model_tedevB import Participant, Employee
from tedev.data.data_tedevB import participant_fields, employee_fields
from tedev.core.forms import ParticipantForm, EmployeeForm
from tedev.core.helpers import create_or_edit_entity


#
from tedev.data.data_general import employee_form_data, participant_form_data


@app.route('/')
def index():
    is_reg =  True if request.args.get('registred') == 'Yes' else False
    return render_template('pages/index.html', data= {'registred': is_reg, 'show_navbar': 'N'})

#Employees + Particpants
@app.route('/<string:entities>')
def entities(entities):
    #
    entity_list = (Employee if entities == 'employees' else Participant).query.all()
    entity_fields = (employee_fields if entities == 'employees' else participant_fields)
    Entities = ('Employees' if entities == 'employees' else 'Participants')

    return render_template(
        'pages/entities.html',
        data={ 'entities_name': entities,
               'Entities_name': Entities,
               'fields': entity_fields,
               'entities': entity_list,
               'show_navbar': 'N'}
    )

#  Create employee
@app.route('/<string:entities>/create', methods=['GET','POST'])
def create_entity(entities):
    print(entities)
    return create_or_edit_entity(
        (EmployeeForm if entities == 'employees' else ParticipantForm),
        (Employee if entities == 'employees' else Participant) ,
        ('employee' if entities == 'employees' else 'participant'),
        ('employees' if entities == 'employees' else 'participants'),
        None,
        (employee_form_data if entities == 'employees' else participant_form_data)
    )

