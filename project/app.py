from flask import Flask, render_template, request, redirect

from forms import ProfileForm


class Config(object):
    SECRET_KEY = 'lol'


app = Flask(__name__)

app.config.from_object(Config)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route("/game/", methods=["GET", "POST"])
def game():
    return render_template('game.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
