"""Default configuration for the Product Catalogue service."""
import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///products.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv("SECRET_KEY", "local-development-only")
TESTING = os.getenv("FLASK_ENV") == "testing"
