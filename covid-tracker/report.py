import functools, os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,
    current_app
)
from . import db
from . import auth

bp = Blueprint('report', __name__, url_prefix='/report')

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        flags = [0 for x in range(32)]
        num_criteria = 10

        for i in range(num_criteria): 
            radio_str = 'criteria_' + str(i) + '_radio' # TODO Make this match the naming convention for the selector
            flag = int(request.form[radio_str])
            if flag == -1: # Negative
                flags[x] = 1
            elif flag == 1: # Positive
                flags[x + 16] = 1
        
        flags_out = 0
        for x in enumerate(flags):
            flags_out += x[1] << (31 - x[0])

        report_text = request.form['textbox'] # TODO Make this match the naming convention for the selector

        report = conn.execute(
            'INSERT INTO reports (UID, LID, TIMESTAMP, FLAGS, TEXT) VALUES (?, ?, current_timestamp, ?, ?);', (g.UID, g.LID, flags_out, report_text,)
        ).fetchone()

        if error is None:
            session.clear()
            return redirect(url_for('index'))

    else:
        return render_template('report/create.html', rules=current_app.config['RULES'])
    
@bp.route('/location', methods=('GET', 'POST'))
def create():
    num_criteria == 10

    flags_list = conn.execute(
            'SELECT (FLAGS) FROM REPORTS WHERE LID = ?;', (g.LID,)
        ).fetchone()

    flag_scores = [2.5 for x in range(num_criteria)]
    for flag_set in flags_list:
        for i in range(num_criteria):
            if not (flag_set & (1 << (31-i))) == 0:
                flag_scores[i] -= (1.0 / len(flags_list))
            if not (flag_set & (1 << (15-i))) == 0:
                flag_scores[i] += (1.0 / len(flags_list))

    # TODO Maybe do things to weight the scores or something.

    return render_template('report/location.html', scores=flag_scores)