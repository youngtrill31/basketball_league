from flask import Flask
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://jdeleon:gamebang08@ds123434.mlab.com:23434/jdleague'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/jdleague'

mongo = PyMongo(app)


class Team(object):

    ##### MongoDB Interactions #####
    def add_user(self, email, password, general_manager):
        general_managers = mongo.db.general_managers
        existing_general_managers = general_managers.find_one({'email': email})
        # existing_user = None

        if existing_general_managers is None:
            hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            general_managers.insert(
                {
                    "email": email,
                    "password": hashpass,
                    "general_manager": general_manager
                }
            )

    def get_gm_login(self, gm_email, pw):
        general_managers = mongo.db.general_managers
        login = general_managers.find_one({"email": gm_email})

        if login:
            if bcrypt.hashpw(pw.encode('utf-8'), login["password"].encode("utf-8")) == \
                    login['password'].encode('utf-8'):
                return login["email"]
            else:
                return Exception()

    def add_team(self, team_name, general_manager):
        teams = mongo.db.teams
        general_managers = mongo.db.general_managers
        gm = general_managers.find_one({"general_manager": general_manager})

        team_id = ''.join(team_name.split()).lower()
        teams.insert(
            {
                "team_name": team_name,
                "team_id": team_id,
                "general_manager": gm,
                "players": []
            }
        )

    def add_player(self, first_name, last_name):
        players = mongo.db.players
        players.insert(
            {
                "first_name": first_name,
                "last_name": last_name,
            }
        )

    def get_player(self, first_name, last_name):
        players = mongo.db.players
        player = players.find_one({"first_name": first_name, "last_name": last_name})

        return player

    def assign_player_to_team(self, first_name, last_name, team_name):
        teams = mongo.db.teams
        players = mongo.db.players
        player = players.find_one({"first_name": first_name, "last_name": last_name})

        teams.update_one(
            {   "team_name": team_name  },
            {   "$push": {  "players": player}})

    def get_teams(self):
        """
        Returns a two dimensional list of team names.
        :return:
        """
        team = mongo.db.teams
        cursor = team.find({})
        team_list = [[doc['team_name'],''.join(doc['team_name'].split()).lower()] for doc in cursor]

        return team_list

    def get_team_data_by_id(self, team_id):
        team = mongo.db.teams
        cursor = team.find({"team_id": team_id})
        team_data = []

        for doc in cursor:
            team_data.append(doc)

        return team_data

    def get_team_data_by_gm_email(self, gm_email):
        team = mongo.db.teams
        cursor = team.find({"general_manager.email": gm_email})
        team_data = []

        for doc in cursor:
            team_data.append(doc)

        return team_data


if __name__ == '__main__':
    from team import Team
    import json

    team = Team()
    # teams = team.get_team_data("Hawks")
    # print teams





    a = team.get_team_data_by_gm_email("aj@aol.com")
    print a