from flask_wtf import  FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField, TextAreaField, SelectField
from wtforms.validators  import Optional

class AppForm(FlaskForm):
    app_name = StringField()
    app_description = TextAreaField(validators=[Optional()])
    app_protocol = SelectField(choices=[('http', 'http'), ('https', 'https')], validators=[Optional()])
    app_address = StringField(validators=[Optional()])
    app_port = IntegerField(validators=[Optional()])
    submit = SubmitField()
