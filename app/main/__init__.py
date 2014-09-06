from flask import Blueprint
from models import db

main = Blueprint('main', __name__)

import routes