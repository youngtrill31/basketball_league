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

@app.route("/")
def main():
    return render_template('main.html', standings=standings)


@app.route("/team_registration")
def team_registration():
    return render_template('team_registration.html')


@app.route("/admin")
def admin():
    return "this is the admin page"
