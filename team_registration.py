from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class TeamRegistration(FlaskForm):
    team_name = StringField('Team Name', validators=[DataRequired(), Length(min=4, max=30)])
    gm_name = StringField('GM Name', validators=[DataRequired(), Length(min=4, max=30)])
    gm_email = StringField('GM Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
