from flask import Flask
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://jdeleon:gamebang08@ds123434.mlab.com:23434/jdleague'

mongo = PyMongo(app)


class Team(object):

    def add_user(self, email, password):
        users = mongo.db.users
        existing_user = users.find_one({'email': email})

        if existing_user is None:
            hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            users.insert(
                {
                    "email": email,
                    "password": hashpass
                }
            )

    def add_team(self, team_name, general_manager):
        team = mongo.db.team
        team.insert(
            {
                "team_id": 1,
                "team_name": team_name,
                "general_manager": general_manager,
                "players": [
                    {
                        "player_id": 1,
                        "first_name": "",
                        "last_name": ""
                    }
                ]
            }
        )

    def update_team(self, team_name, first_name, last_name):
        """
        Locates team in mongo and adds players to team
        :return:
        """
        team = mongo.db.team
        team_name = team.find_one({'team_name': team_name})
        team_name['players'] = [
            {
                "player_id": 1,
                "first_name": first_name,
                "last_name": last_name
            }
        ]