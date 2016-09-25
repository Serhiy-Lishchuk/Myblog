from datetime import datetime
from flask import abort,  redirect, request, session, url_for
from Flaskblog.db.db import get_db


def add_entry():
    """
    Add an entry to the database
    """
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('INSERT INTO entries (title, text, image, music, timestamp) VALUES (?,?,?,?,?)',
               [request.form['title'], request.form['text'], request.form['image'], request.form['music'],
                datetime.now().strftime('%d.%m.%Y / %H:%M:%S')])
    db.commit()
    db.close()
    return redirect(url_for('show_entries'))
