from datetime import datetime
import sqlite3
from flask import (
	Blueprint, g, request, redirect, url_for, flash, render_template, session
)
import os

from penpaper.db import get_db

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
def sentiment(text):
    client = language.LanguageServiceClient.from_service_account_json(r"C:\Users\zliu1\projects\pen-paper\penpaper\credentials.json")

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    return sentiment.score


bp = Blueprint('dash', __name__, url_prefix='/dash')


@bp.route('', methods=('GET','POST'))
def index():
	return render_template('dash/index.html')

@bp.route('/calendar')
def calendar():
	return render_template('dash/calendar.html')

@bp.route('/journal', methods=('GET', 'POST'))
def journal():
	if request.method == 'POST':
		entry = request.form["entry"]
		now = datetime.now()
		date_time = now.strftime("%d/%m/%Y %H:%M:%S")
		rating = sentiment(entry)
		error = None
		db = get_db()

		if not entry:
			error = "Please type your thoughts."
		if not error:
			db.execute(
				'INSERT INTO entry (entry, date_time, rating)'
					' VALUES (?, ?, ?)', (entry, date_time, rating)
			)
			db.commit()

			return redirect(url_for("dash.index"))

		flash(error)
	return render_template('dash/journal.html')

@bp.route('/past_entries')
def past_entries():
	db = get_db()
	#cur = db.cursor()
	db.row_factory = sqlite3.Row
	cur = db.cursor()
	cur.execute("select * from entry")
	rows = cur.fetchall()
	return render_template("dash/past_entries.html", rows = rows)
	# test = cur.fetchall()
	# cur.execute('SELECT * FROM entry')
	# entries = [dict(entry=row[0],
    #                 date=row[1])
    #                  for row in cur.fetchall()]
	# db.close()
	#return render_template('dash/past_entries.html') #, rows = entries)
