# Image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Installation des dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier requirements.txt pour installer les dépendances Python
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du projet dans le conteneur
COPY . .

# Définir les variables d'environnement pour Flask
ENV FLASK_APP=application.py
ENV FLASK_ENV=development

# Exposer le port 5000 pour l'application Flask
EXPOSE 5000

# Commande pour démarrer l'application Flask en mode développement
CMD ["flask", "run", "--host", "0.0.0.0"]
