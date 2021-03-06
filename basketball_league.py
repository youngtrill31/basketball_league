from __future__ import print_function
from flask import Flask, render_template, url_for, flash, redirect, session, request
from flask_pymongo import PyMongo
from team_registration import TeamRegistration
from team_roster import TeamRoster, RosterManagementForm
from team_login import TeamLogin
from team import Team
import logging
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
    if "gm_email" in session:
        return "You already have a team registered!"

    form = TeamRegistration()
    team = Team()

    if form.validate_on_submit():
        team.add_user(form.gm_email.data, form.password.data, form.gm_name.data)
        team.add_team(form.team_name.data, form.gm_name.data)
        for player in form.players.data:
            team.add_player(player['first_name'], player['last_name'])
            team.assign_player_to_team(player['first_name'], player['last_name'], form.team_name.data)
        flash("Account created for %s" %  form.gm_email.data, 'success')
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

@app.route("/team_login")
def team_login():
    login_form = TeamLogin()

    return render_template('team_login.html', title='Teams', form=login_form)

@app.route("/gm_login", methods=['POST'])
def gm_login():
    login_form = TeamLogin()

    session["gm_email"] = login_form.gm_email.data
    return redirect(url_for("gm_home"))

@app.route("/gm_home")
def gm_home():
    team = Team()
    team_data = team.get_team_data_by_gm_email(session["gm_email"])

    if "gm_email" in session:
        return render_template("gm/gm_home.html", gm_email=session["gm_email"], team_data=team_data)

    login_form = TeamLogin()

    return render_template("team_login.html", form=login_form)

@app.route("/roster_management", methods=["GET", "POST"])
def roster_management():

    if "gm_email" in session:
        team = Team()
        team_data = team.get_team_data_by_gm_email(session["gm_email"])

        # Add team_id to session
        for td in team_data:
            app.logger.debug("team_id: %s" % td["team_id"])
            session["team_id"] = td["team_id"]

        roster_form = RosterManagementForm()

        if roster_form.validate_on_submit():
            if roster_form.add_button.data:
                team.add_player(roster_form.first_name.data, roster_form.last_name.data)
                for t in team_data:
                    team.assign_player_to_team(roster_form.first_name.data, roster_form.last_name.data, t["team_name"])
                app.logger.debug("%s %s is added to the roster." % (roster_form.first_name.data,
                                 roster_form.last_name.data))
            return redirect(url_for('roster_management'))
        else:
            app.logger.debug("NOT ADDED: %s %s" % (roster_form.first_name.data, roster_form.last_name.data))
            return render_template("gm/roster_management.html", team_data=team_data, form=roster_form)


@app.route("/remove_player", methods=["POST"])
def remove_player():
    app.logger.debug("Remove Player View")
    team = Team()
    if request.method == "POST":
        _id = request.json['data']
        team.remove_player_from_team_by_ids(_id, session["team_id"])
        app.logger.debug("Player with id %s has been removed from %s" % (_id, session["team_id"]))
        return redirect(url_for('roster_management'))
    return render_template("gm/roster_management.html")

@app.route("/logout")
def logout():
    session.pop("gm_email")
    return redirect(url_for("home"))

@app.route("/team_registration_confirmation")
def team_registration_confirmation():
    return render_template('team_registration_confirmation.html')

@app.route("/admin")
def admin():
    return "this is the admin page"

@app.route("/admin/team/<team_id>")
def admin_team(team_id):
    return "this is the admin team page"

