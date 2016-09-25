from flask import flash, redirect, session, url_for


def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home'))
