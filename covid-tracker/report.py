import functools, os, datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,
    current_app
)
from . import db

bp = Blueprint('report', __name__, url_prefix='/report')


@bp.route('/about')
def about():
    return render_template('report/about.html')


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        flags = [0 for x in range(32)]
        num_criteria = 10
        error = None

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

        report_text = request.form['criteria_report'] # TODO Make this match the naming convention for the selector

        timestamp = datetime.datetime.now()
        conn = db.get_db()
        cursor = conn.cursor()
        # TODO: Insert into the database.
        try:
            cursor.execute(
                'INSERT INTO reports (UID, LID, TIMESTAMP, FLAGS, TEXT) VALUES (%s, %s, %s, %s, %s);', 
                (session.get('uid'), 1, timestamp, flags_out, report_text)
            )
        except:
            error = 'There was an error uploading your report, try again later.'
        cursor.close()

        if error is None:
            conn.commit()
            return redirect(url_for('index'))
        flash(error)
    return render_template('report/create.html', rules=current_app.config['RULES'])
    

@bp.route('/location', methods=('GET', 'POST'))
def location():
    num_criteria = 10
    
    cursor = db.get_db().cursor()
  
    cursor.execute(
            'SELECT (FLAGS) FROM REPORTS WHERE LID = %s;', (g.LID,)
        )
    flags_list = cursor.fetchone()
    cursor.close()

    flag_scores = [2.5 for x in range(num_criteria)]
    for flag_set in flags_list:
        for i in range(num_criteria):
            if not (flag_set & (1 << (31-i))) == 0:
                flag_scores[i] -= (1.0 / len(flags_list))
            if not (flag_set & (1 << (15-i))) == 0:
                flag_scores[i] += (1.0 / len(flags_list))

    # TODO Maybe do things to weight the scores or something.

    return render_template('report/location.html', scores=flag_scores)
    