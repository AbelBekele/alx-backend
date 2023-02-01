#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template
app = Flask(__name__)


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
    return render_template('/0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
