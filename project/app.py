from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

from forms import ProfileForm
from matrix import Matrix


class Config(object):
    SECRET_KEY = 'lol'


app = Flask(__name__)

app.config.from_object(Config)
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def index():
    global game
    game = Matrix()
    return render_template('index.html')


@app.route("/game/", methods=["GET", "POST"])
def game():
    if isinstance(game, Matrix):
        form = ProfileForm()
        if form.validate_on_submit():
            side_of_the_world = form.side_of_the_world.data
            step = form.step.data
            submit = form.submit.data
            print(step)
            print(side_of_the_world)

            location = game.movement(side_of_the_world, step)
            if location is not None:
                return render_template('game.html', form=form, side_of_the_world=side_of_the_world, step=step, submit=submit, location=location)
            else:
                return render_template('game.html', form=form, side_of_the_world=side_of_the_world, step=step, submit=submit, location='Вы не можете сюда идти!')
        else:
            return render_template('game.html', form=form)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
