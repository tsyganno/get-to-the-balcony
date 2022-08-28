from flask import Flask, render_template, request, redirect

from forms import ProfileForm


class Config(object):
    SECRET_KEY = 'lol'


app = Flask(__name__)

app.config.from_object(Config)


@app.route("/", methods=["GET", "POST"])
def index():
    form = ProfileForm()
    if form.validate_on_submit():
        username = form.username.data
        about_me = form.about_me.data
        password = form.password.data
        submit = form.submit.data
        return render_template('index.html', form=form, username=username, about_me=about_me, password=password)
    else:
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
