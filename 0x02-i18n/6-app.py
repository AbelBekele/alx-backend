#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template, request, g
from flask_babel import Babel, _ as get_translation
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int) -> dict:
    """
    ----------------
    METHOD: get_user
    ----------------
    Description:
        Given a valid user id, get_user returns
        the dictionary object containing the
        parameters for a specific object
    Args:
        @id: user id
    """
    if user_id and type(user_id) in [int, str]:
        return users.get(int(user_id))


class Config(object):
    """
    -------------
    CLASS: config
    -------------
    Description:
        Initializes config class with class attributes
        containing the expected configuration for the
        Babel module.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request():
    """
    ----------------------
    METHOD: before_request
    ----------------------
    Description:
        Sets up a behavior to be applied
        with every single request before
        @app.routes are triggered
    """
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


@babel.localeselector
def get_locale():
    """ Sets up the correct locale """
    if request.args.get('locale') == 'fr' or\
            g.user and g.user.get('locale') == 'fr' or\
            request.headers.get('Accept-Language') and\
            request.headers.get('Accept-Language').split()[0][:2] == 'fr' or\
            Config.BABEL_DEFAULT_LOCALE == 'fr':
        return 'fr'
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def root():
    """
    ------------
    METHOD: root
    ------------
    Description:
        Returns a rendered template of an
        HTML site
    """
    if g.user:
        login_msg = get_translation('logged_in_as', username=g.user['name'])
    else:
        login_msg = get_translation('not_logged_in')

    return render_template('/5-index.html',
                           title=get_translation('home_title'),
                           heading=get_translation('home_header'),
                           login_msg=login_msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
