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
        password2 = request.form['password2']
        conn = db.get_db()
        error = None

        if not email:
            error = "Email is required."
        elif not password:
            error = "Password is required."
        elif not password == password2:
            error = "Passwords do not match."
        
        cursor = conn.cursor()

        print(email)
        cursor.execute(
            'SELECT * FROM users WHERE email = %s',(email,)
        ) 
        if cursor.fetchone() is not None:
            error = f'User with email {email} is already registered!'
        cursor.close()

        if error is None:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO users (email, password) VALUES (%s, %s)', 
                (email, generate_password_hash(password))
            )
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        error = None
        try:
            cursor = db.get_db().cursor()
        except:
            error = 'Failed to create cursor'
        try:
            cursor.execute(
                'SELECT * FROM users WHERE email = %s', (email,)
            )
            user = cursor.fetchone()
        except:
            error = 'Failed to fetch from database'
            user = None
        cursor.close()

        if user is None or not check_password_hash(user[2], password):
            error = 'Incorrect email or password.'

        if error is None:
            session.clear()
            session['uid'] = user[0]
            conn.close()
            return redirect(url_for('index'))
        conn.close()
        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('uid')

    if user_id is None:
        g.user = None
    else:
        connection = db.get_db()
        cursor = connection.cursor()
        cursor.execute(
            'SELECT id, email FROM users WHERE id = %s', (user_id,)
        )
        g.user = cursor.fetchone()
        cursor.close()
        

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view