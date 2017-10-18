from flask import render_template
from Flaskblog.models.models import base_entries


def show_entries():
    entries = base_entries()
    return render_template('home.html', entries=entries)
