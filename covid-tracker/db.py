import os, sys
import psycopg2

from flask import current_app, g
from flask.cli import with_appcontext


def get_db(ini='db.ini'):
    global conn_str
    if conn_str not in globals():
        try:
            with open(ini) as f:
                conn_str = ''.join(f.readlines())
        except OSError as e:
            print(e)


    if 'db' not in g:
        g.db = psycopg2.connect(conn_str)

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)