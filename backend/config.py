import os
from dotenv import load_dotenv
from datetime import timedelta

# Définir le répertoire de base
basedir = os.path.abspath(os.path.dirname(__file__))

# Charger les variables d'environnement depuis le fichier .env
load_dotenv(os.path.join(basedir, ".env"))

class Config(object):
    # Clé secrète pour JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    # Durée d'expiration du token d'accès JWT
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=4)

    # Désactiver le suivi des modifications de SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Informations sur l'API
    API_TITLE = "Rest API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/docs"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

class DevelopmentConfig(Config):
    # URI de la base de données pour l'environnement de développement (SQLite)
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.db")

class TestConfig(Config):
    # Configuration pour les tests (base de données en mémoire)
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

class DockerConfig(Config):
    # URI de la base de données pour l'environnement Docker (MySQL)
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@db/{os.getenv('MYSQL_DATABASE')}"
