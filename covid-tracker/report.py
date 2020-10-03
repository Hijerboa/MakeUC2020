import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from . import db

bp = Blueprint('report', __name__, url_prefix='/report')

@bp.route('/create', methods=('GET', 'POST'))
def create():
    return render_template('report/create.html')