# app/routes/__init__.py
from flask import Blueprint

resto_bp = Blueprint('resto', __name__)

from app.routes.resto_routes import *
