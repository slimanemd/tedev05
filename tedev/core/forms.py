# import wtf wtforms
import phonenumbers
from flask_wtf import FlaskForm  #Form
from wtforms import StringField,  SelectField
from wtforms.validators import DataRequired, Email

#
from tedev.core.models.model_tedevB import Participant
from tedev.data.data_general import cities

msg01 = u'Il y a deja un compte avec de mail.'  #u'This element already exists.'
msg02 = u'Le numero de telephone n est pas valide.'  #u'This element already exists.'

# ourapp/util/validators.py
from wtforms.validators import ValidationError

#
class isCAPhone(object):
    def __init__(self, message=msg02):
        self.message = message

    def __call__(self, form, field):
        check = phonenumbers.is_valid_number(phonenumbers.parse(field.data, 'CA'))
        if check:
            raise ValidationError(self.message)

#
class Unique(object):
    def __init__(self, model, field, message=msg01):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

# Employee
class BaseForm01(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    state = SelectField('state', validators=[DataRequired()], choices =cities) # [('a','Ottawa'),('b','Toronto'),('c','Sudbury')])


# Participant
class ParticipantForm(BaseForm01):  #FlaskForm):
    phone = StringField('phone', validators=[DataRequired(), isCAPhone(message=msg02)])
    email = StringField(
        'email',
        validators=[DataRequired(), Email(),
            Unique(Participant,Participant.email,message=msg01)])  #There is already an account with that email
    entreprise = StringField(
        'entreprise',
        validators=[DataRequired(),
                    Unique(Participant,Participant.entreprise,message=msg01)])

# Employee
class EmployeeForm(BaseForm01):  #(FlaskForm):
    phone = StringField('phone')
    email = StringField('email', validators=[DataRequired()])
    entreprise = StringField('entreprise')
