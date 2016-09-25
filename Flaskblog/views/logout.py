from flask import redirect, session, url_for


def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))
