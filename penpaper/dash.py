from datetime import datetime

from flask import (
	Blueprint, g, request, redirect, url_for, flash, render_template, session
)


bp = Blueprint('dash', __name__, url_prefix='/dash')


@bp.route('', methods=('GET','POST'))
def index():
	return render_template('dash/index.html')

@bp.route('/new')
def jounral():
	return render_template('dash/journal.html')

@bp.route('/calendar')
def calendar():
<<<<<<< HEAD
	return render_template('dash/calendar.html')

@bp.route('/journal', methods=('GET', 'POST'))
def journal():
	if request.method == 'POST':
		entry = request.form["entry_id"]
		now = datetime.now()
		date_time = now.strftime("%d/%m/%Y %H:%M:%S")

		error = None
		db = get_db()

		if not entry:
			error = "Please type your thoughts."
		if not error:
			db.execute(
				'INSERT INTO entry (entry, date_time, rating)'
					' VALUES (?, ?, ?)', (entry, date_time, 0)
			)
			db.commit()

			return redirect(url_for("dash.index"))

		flash(error)
	return render_template('dash/journal.html')
||||||| merged common ancestors
	return render_template('auth/calendar.html')
=======
	return render_template('dash/calendar.html')

>>>>>>> 1d55d9b32763cf7311ac2d53f23abf4878b42665
