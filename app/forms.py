from flask_wtf import  FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField, TextAreaField, SelectField, FileField, BooleanField
from wtforms.validators  import Optional
from . import db
from .models import Background, RowStructure

class AppForm(FlaskForm):
    app_name = StringField()
    app_icon_link = StringField()
    app_description = TextAreaField(validators=[Optional()])
    app_protocol = SelectField(choices=[('http', 'http'), ('https', 'https')], validators=[Optional()])
    app_address = StringField(validators=[Optional()])
    app_port = IntegerField(validators=[Optional()])
    submit = SubmitField()

class ProfileForm(FlaskForm):
    profile_name = StringField()
    profile_default_url = StringField()
    profile_background = SelectField(
        choices=[('', 'Choose a background')] + [
            (row.id, row.background)
            for row in db.session.query(
                Background.id,
                Background.background,
            )
            .distinct()
            .order_by(Background.id)
            .all()
        ],
        validators=[Optional()])
    # profile_background = StringField(validators=[Optional()])
    profile_background_picture = FileField(validators=[Optional()])
    profile_columns = IntegerField(validators=[Optional()])
    profile_cards_per_row = SelectField(
        choices=[('', 'How many cards per row?')] + [
            (row.id, row.row_cards)
            for row in db.session.query(
                RowStructure.id,
                RowStructure.row_cards,
            )
            .distinct()
            .order_by(RowStructure.id)
            .all()
        ],
        validators=[Optional()])
    profile_is_current = BooleanField(validators=[Optional()])
    profile_submit = SubmitField()

    
