from flask import Flask
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

#app.config['MONGO_URI'] = 'mongodb://jdeleon:gamebang08@ds123434.mlab.com:23434/jdleague'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/jdleague'

mongo = PyMongo(app)


class Team(object):

    def add_user(self, email, password):
        users = mongo.db.users
        existing_user = users.find_one({'email': email})
        # existing_user = None

        if existing_user is None:
            hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            users.insert(
                {
                    "email": email,
                    "password": hashpass
                }
            )

    def add_team(self, team_name, general_manager):
        teams = mongo.db.teams
        teams.insert(
            {
                "team_id": 1,
                "team_name": team_name,
                "general_manager": general_manager,
                "players": [

                ]
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

    # def assign_player_to_team(self, first_name, team_name):
    #     players = mongo.db.players
    #     teams = mongo.db.teams
    #     for player in players.find_one({ "first_name": first_name }):
    #         team = teams.find_one({ "team_name": team_name })
    #         team["players"].append(player.get('_id'))

    def update_team(self, team_name, object_id):
        """
        Locates team in mongo and adds players to team
        :return:
        """
        teams = mongo.db.teams
        team_name = teams.find_one({'team_name': team_name})
        team_name['players'] = [
            {
                object_id
            }
        ]