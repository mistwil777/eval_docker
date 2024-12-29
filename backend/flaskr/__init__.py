import flaskr.models  # Importer les modèles Flask
from flask import Flask  # Importer Flask
from config import DockerConfig  # Importer la configuration Docker
from flaskr.extensions import migrate, api, cors, jwt  # Importer les extensions Flask
from flaskr.db import db  # Importer l'objet db
from flaskr.routes.task_route import bp as task_route  # Importer les routes des tâches

def create_app(test_config=None):
    app = Flask(__name__)  # Créer une instance de l'application Flask

    if test_config is None:
        app.config.from_object(DockerConfig)  # Charger la configuration Docker par défaut
    else:
        app.config.from_object(test_config)  # Charger une configuration de test si fournie

    db.init_app(app)  # Initialiser la base de données avec l'application
    migrate.init_app(app, db)  # Initialiser les migrations avec l'application
    api.init_app(app)  # Initialiser l'API avec l'application
    cors.init_app(app)  # Initialiser CORS avec l'application
    jwt.init_app(app)  # Initialiser JWT avec l'application

    api.register_blueprint(task_route, url_prefix="/api/v1")  # Enregistrer les routes des tâches

    return app  # Retourner l'instance de l'application Flask
