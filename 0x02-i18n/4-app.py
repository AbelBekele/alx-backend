#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template, request
from flask_babel import Babel, _ as get_translation


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


@babel.localeselector
def get_locale():
    """ Sets up the correct locale """
    if request.args.get('locale') == 'fr':
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
    return render_template('/4-index.html',
                           title=get_translation('home_title'),
                           heading=get_translation('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
