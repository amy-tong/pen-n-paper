import functools

from flask import (
	Blueprint, g, request, redirect, url_for, flash, render_template, session
)
from werkzeug.security import generate_password_hash, check_password_hash
from penpaper.db import get_db


bp = Blueprint('auth', __name__)


@bp.route('/register', methods=('GET', 'POST'))
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		name = request.form['name']
		email = request.form['email']
		error = None
		db = get_db()

		if not username:
			error = "Username is required."
		elif not password:
			error = "Password is required."
		elif not email:
			error = "Email is required."
		elif db.execute(
			'SELECT user_id FROM user WHERE username = ?', (username,)
		).fetchone() is not None:
			error = "This username has been taken."
		# elif db.execute(
		# 	'SELECT id FROM user WHERE email = ?', (email,)
		# ).fetchone() is not None:
		# 	error = "This email is already registered."

		if not error:
			db.execute(
				'INSERT INTO user (username, password, name, email)'
					' VALUES (?, ?, ?, ?)', (username, 
					generate_password_hash(password), name, email,)
			)
			db.commit()

			return redirect(url_for("auth.confirm"))

		flash(error)
	return render_template("auth/register.html")


@bp.route('/confirm')
def confirm():
	return render_template("auth/confirm.html")


@bp.route('/login', methods=('GET','POST'))
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		error = None
		db = get_db()

		if not username:
			error = 'Username is required.'
		elif not password:
			error = 'Password is required.'
		else:
			user = db.execute(
				'SELECT * FROM user WHERE username = ?', (username,)
			).fetchone()
			if user is None:
				error = 'This user does not exist.'
			elif not check_password_hash(user['password'], password):
				error = 'The username or password is incorrect.'

			if error is None:
				session.clear()
				session['user_id'] = user['id']
				return redirect(url_for('dash.index'))
				
		flash(error)

	return render_template('auth/login.html')


@bp.route('/calendar')
def calendar():
	return render_template('auth/login.html')
