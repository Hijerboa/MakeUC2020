import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from . import db

bp = Blueprint('report', __name__, url_prefix='/report')

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
    