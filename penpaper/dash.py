from flask import (
	Blueprint, g, request, redirect, url_for, flash, render_template, session
)


bp = Blueprint('dash', __name__, url_prefix='/dash')


@bp.route('', methods=('GET','POST'))
def index():
	return render_template('dash/index.html')

@bp.route('/calendar')
def calendar():
	return render_template('auth/calendar.html')
