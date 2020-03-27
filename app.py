import dash
import dash_bootstrap_components as dbc
from flask_login import LoginManager, UserMixin
from users import db, User as base
from config import config
import os


executive_fonts = ['https://fonts.googleapis.com/css?family=Merriweather&display=swap',
				'https://fonts.googleapis.com/css?family=Source+Sans+Pro&display=swap']

app = dash.Dash(__name__,
	external_stylesheets=executive_fonts,
	meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)
server = app.server
app.config.suppress_callback_exceptions = True
app.title = 'The Executive Desk'

server.config.update(
	SECRET_KEY=os.environ.get('APP_SECRET_KEY'),
	SQLALCHEMY_DATABASE_URI=config.get('database', 'con'),
	SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db.init_app(server)

login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'

class User(UserMixin, base):
	pass

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)
