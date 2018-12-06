from __future__ import print_function
from flask import Flask, render_template, url_for, flash, redirect, session
from flask_pymongo import PyMongo
from team_registration import TeamRegistration
from team_login import TeamLogin
from team import Team
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
    if form.validate_on_submit():
        team.add_user(form.gm_email.data, form.password.data)
        team.add_team(form.team_name.data, form.gm_name.data)
        for player in form.players.data:
            team.add_player(player['first_name'], player['last_name'])
            team.assign_player_to_team(player['first_name'], player['last_name'], form.team_name.data)
        session['gm_email'] = form.gm_email.data
        flash("Account created for %s" % session['gm_email'], 'success')
        return redirect(url_for('team_registration_confirmation'))
    else:
        # return form.errors
        return render_template('team_registration.html', show_home=0, title='Team Registration', form=form)

@app.route("/teams")
def teams():
    team = Team()
    teams = team.get_teams()

    return render_template('teams.html', title='Teams', team_list=teams)

@app.route("/teams/<team_id>")
def team_page(team_id):
    team = Team()
    team_data = team.get_team_data_by_id(team_id)

    return render_template('team_information.html', title='Teams', team_info_list=team_data)

@app.route("/team_login", methods=['POST'])
def team_login():
    form = TeamLogin()

    # if 'gm_email' in session:
    #     return 'you are logged in as ' + session['gm_email']
    return render_template('team_login.html', show_home=0, title='Team Login', form=form)

@app.route("/team_registration_confirmation")
def team_registration_confirmation():
    return render_template('team_registration_confirmation.html')

@app.route("/admin")
def admin():
    return "this is the admin page"

@app.route("/admin/team/<team_id>")
def admin_team(team_id):
    return "this is the admin team page"

@app.route('/add_players')
def add_players():
    team = Team()
    team.add_user('jdeleon@gmail.com', 'password')
    return 'Added!'

