from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form as NoCsrfForm
from wtforms.validators import DataRequired, Length, Email, EqualTo


class TeamRoster(NoCsrfForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])


class RosterManagementForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    save_button = SubmitField("Save")