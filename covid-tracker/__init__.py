import os, pathlib, json
from configparser import ConfigParser

from flask import (Flask, render_template, request, send_from_directory)


def config_db(filename='db.ini'):
    db = dict()
    with open(filename) as f:
        for line in f:
            key, value = line.split('=')
            db[key] = value.strip()
    return db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
    
    app.config.from_mapping(
        SECRET_KEY='dev'
    )  

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    rulesfile = os.path.join(pathlib.Path(__file__).parent.absolute(), 'rules.txt')
    with open(rulesfile) as f:
        rules = list(f.readlines())
    app.config['RULES'] = rules

    connfile = os.path.join(pathlib.Path(__file__).parent.absolute(), 'db.ini')
    app.config["CONN_PARAMS"] = config_db(connfile)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import report
    app.register_blueprint(report.bp)

    @app.route('/', methods=('GET', 'POST'))
    def index():
        keywords = None
        print('got a post!')
        if 'searchBar' in request.args:
            keywords = request.args.get('searchBar')
        print(keywords)
        return render_template('report/index.html', keywords=json.dumps(keywords))
    return app