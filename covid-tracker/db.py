import os, sys
import psycopg2

from flask import current_app, g
from flask.cli import with_appcontext


def get_db():

    if 'db' not in g:
        g.db = psycopg2.connect(**current_app.config["CONN_PARAMS"])

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)