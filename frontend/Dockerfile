# Utilisation de l'image Node.js v18
FROM node:18

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers package.json et package-lock.json
COPY package*.json ./

# Installation des dépendances
RUN npm install

# Copie du reste des fichiers du projet
COPY . .

# Exposition du port 4200
EXPOSE 4200

# Commande pour démarrer l'application
CMD ["npm", "start", "--", "--host", "0.0.0.0"]
