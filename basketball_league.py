from __future__ import print_function
from flask import Flask, render_template, url_for, flash, redirect
from flask_pymongo import PyMongo
from team_registration import TeamRegistration
from team_login import TeamLogin
from team import Team
import sys
app = Flask(__name__)

app.config['SECRET_KEY'] = 'R0HU997LNU9HKE48'
app.config['MONGO_URI'] = 'mongodb://jdeleon:gamebang08@ds123434.mlab.com:23434/jdleague'

mongo = PyMongo(app)

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
    team = Team()
    p = []
    if form.validate_on_submit():
        team.add_user(form.gm_email.data, form.password.data)
        team.add_team(form.team_name.data, form.gm_name.data)
        for players in form.players.data:
            p.append(players)
        # flash("Account created for %s" % p, 'success')
        return p
        # return redirect(url_for('team_registration_confirmation'))
    else:
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


@app.route('/add_players')
def add_players():
    roster = Rosters()
    roster.add_players()
    return 'Added!'


@app.route('/add_team')
def add_team():
    roster = Rosters()
    roster.add_team("Clippers", "Jeremiah De Leon")
    return 'Team added!'


@app.route('/update_team')
def update_team():
    roster = Rosters()
    roster.update_team("Clippers", "Michael", "Jordan")