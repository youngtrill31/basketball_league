from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from team_roster import TeamRoster


class TeamRegistration(FlaskForm):
    team_name = StringField('Team Name', validators=[DataRequired(), Length(min=4)])
    gm_name = StringField('GM Name', validators=[DataRequired(), Length(min=4)])
    gm_email = StringField('GM Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    players = FieldList(FormField(TeamRoster), min_entries=3)
    submit = SubmitField('Register')
