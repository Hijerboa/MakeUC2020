import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from . import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = db.get_db()
        error = None

        if not email:
            error = "Email is required."
        elif not password:
            error = "Password is required."
        elif conn.execute(
            'SELECT id FROM users WHERE email = ?', (email)
        ).fetchone() is not None:
            error = f'User with email {email} is already registered!'

        if error is None:
            conn.execute(
                'INSERT INTO users (email, password) VALUES (?, ?)', 
                (email, generate_password_hash(password))
            )

            conn.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = db.get_db()
        error = None
        user = conn.execute(
            'SELECT * FROM users WHERE email = ?', (email,)
        ).fetchone()

        if user is None or not check_password_hash(user['password'], password):
            error = 'Incorrect email or password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db.get_db().execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def log_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view