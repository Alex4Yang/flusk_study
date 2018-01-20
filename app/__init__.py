from flask import Blueprint

routes = Blueprint('routes', __name__)

from .index import *
from .users import *
from .nine_bang import *
