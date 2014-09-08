from flask import Flask
from flask.ext.socketio import SocketIO
from flask_bootstrap import Bootstrap
socketio = SocketIO()

def create_app(debug=False):
  """Create an application."""
  app = Flask(__name__)  
  app.debug = debug
  app.config['SECRET_KEY'] = 'Taj#HIWc*f23'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jorelo<3u@localhost/development'
  from .main.models import db
  from .main import main as main_blueprint
  from .main import routes
  app.register_blueprint(main_blueprint)  
  db.init_app(app)
  socketio.init_app(app)
  Bootstrap(app)
  return app





"""
app = Flask(__name__)      

app.secret_key = 'development key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jorelo<3u@localhost/development'
 
from models import db
db.init_app(app)

import main.routes

"""