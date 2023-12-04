# app/__init__.py
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


# Inisialisasi aplikasi Flask
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Import dan daftarkan blueprint
from app.routes import resto_bp
app.register_blueprint(resto_bp)
