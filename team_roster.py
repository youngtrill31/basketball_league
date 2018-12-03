# from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import Form as NoCsrfForm
from wtforms.validators import DataRequired


class TeamRoster(NoCsrfForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
