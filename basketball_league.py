from flask import Flask, render_template, url_for, flash, redirect
from team_registration import TeamRegistration
from team_login import TeamLogin
app = Flask(__name__)

app.config['SECRET_KEY'] = 'R0HU997LNU9HKE48'

standings = [
    {
        'team': 'Clippers',
        'wins': 20,
        'losses': 0
    },
    {
        'team': 'Lakers',
        'wins': 0,
        'losses': 20
    }
]

@app.route("/home")
def home():
    return render_template('home.html', standings=standings, show_home=1)


@app.route("/team_registration", methods=["GET", "POST"])
def team_registration():
    form = TeamRegistration()
    if form.validate_on_submit():
        flash("Account created for %s" % {form.team_name.data}, 'success')
        return redirect(url_for('team_registration_confirmation'))
    return render_template('team_registration.html', show_home=0, title='Team Registration', form=form)

@app.route("/team_login")
def team_login():
    form = TeamLogin()
    return render_template('team_login.html', show_home=0, title='Team Login', form=form)

@app.route("/team_registration_confirmation")
def team_registration_confirmation():
    return render_template('team_registration_confirmation.html')

@app.route("/admin")
def admin():
    return "this is the admin page"
