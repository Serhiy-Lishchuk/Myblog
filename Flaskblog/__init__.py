from flask import Flask
from Flaskblog.config.config import DEBUG, SECRET_KEY

app = Flask(__name__)

app.config.update(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY
)

from Flaskblog.services.logg_err import log_error
from Flaskblog.views.addentry import add_entry
from Flaskblog.views.login import login_in
from Flaskblog.views.logout import logout
from Flaskblog.views.showentries import show_entries
from Flaskblog.views.upload import upload
from Flaskblog.views.views import about, base, contact, home

app.add_url_rule('/', view_func=log_error(base), methods=['GET'])
app.add_url_rule('/Home', view_func=log_error(home), methods=['GET'])
app.add_url_rule('/about', view_func=log_error(about), methods=['GET'])
app.add_url_rule('/contact', view_func=log_error(contact), methods=['GET'])
app.add_url_rule('/login', view_func=log_error(login_in), methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=log_error(logout), methods=['GET'])
app.add_url_rule('/home', view_func=log_error(show_entries), methods=['GET'])
app.add_url_rule('/add', view_func=log_error(add_entry), methods=['POST'])
app.add_url_rule('/upload', view_func=log_error(upload), methods=['GET', 'POST'])
