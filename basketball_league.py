from flask import Flask, render_template, url_for
app = Flask(__name__)


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


@app.route("/team_registration")
def team_registration():
    return render_template('team_registration.html', show_home=0)


@app.route("/admin")
def admin():
    return "this is the admin page"
