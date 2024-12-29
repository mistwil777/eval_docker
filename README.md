# Projet Todo App avec Docker

Ce projet est une application de gestion de tâches (Todo) utilisant une stack moderne et déployée avec Docker.

## Stack Technique

- Frontend: Angular
- Backend: Flask (Python)
- Base de données: MySQL
- Proxy inverse: Nginx
- Administration de base de données: PHPMyAdmin
- Service IA: TensorFlow

## Prérequis

- Docker
- Docker Compose

## Configuration

1. Clonez le dépôt
2. Assurez-vous que Docker et Docker Compose sont installés sur votre machine

## Démarrage

Pour lancer l'application, exécutez :

```
docker-compose up --build
```

Cette commande va construire et démarrer tous les services définis dans le fichier `docker-compose.yml`.

## Services

- Frontend: Accessible sur http://localhost
- Backend API: Accessible via http://localhost/api
- PHPMyAdmin: Accessible sur http://localhost:8080
- TensorFlow: Service d'IA accessible sur le port 8501

## Structure du Projet

- `frontend/`: Code source Angular
- `backend/`: Code source Flask
- `docker-compose.yml`: Configuration des services Docker
- `Dockerfiles`: Un pour le frontend et un pour le backend

## Développement

Pour le développement, les volumes sont montés pour permettre le hot-reloading du code frontend et backend.

## Notes

- Assurez-vous que la variable d'environnement `MODEL_NAME` est correctement définie pour le service TensorFlow.
- Le projet utilise Node.js v18 pour le frontend Angular.
