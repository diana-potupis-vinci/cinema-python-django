# 🎬 Cinema Django Application

Une application web de gestion de cinéma développée avec Django, permettant la gestion des films, séances, et réservations.

## 📋 Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Technologies utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Modèles de données](#modèles-de-données)
- [API & URLs](#api--urls)
- [Contribuer](#contribuer)

## ✨ Fonctionnalités

### 🎭 Gestion des films
- Affichage de la liste des films avec pagination
- Détails complets des films (titre, description, durée, genre, affiche, acteurs)
- Ajout de nouveaux films (réservé aux administrateurs)
- Upload d'affiches

### 🎫 Gestion des séances
- Visualisation des séances disponibles
- Association films-salles-horaires
- Filtrage des séances par date

### 👤 Gestion des utilisateurs
- Inscription et connexion des utilisateurs
- Authentification sécurisée
- Profils utilisateurs avec prénom, nom, email

### 📅 Système de réservation
- Réservation de places pour les séances
- Gestion des réservations utilisateur (création, modification, suppression)
- Historique des réservations

### 🎨 Interface utilisateur
- Design responsive avec Bootstrap 5
- Navigation intuitive
- Interface en français
- Thème cinéma avec icônes Font Awesome

## 🛠 Technologies utilisées

- **Backend:** Django 4.x, Python 3.x
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Base de données:** SQLite (par défaut)
- **Authentification:** Django Auth
- **Icônes:** Font Awesome 6.4.0
- **Formulaires:** Django Forms avec validation

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip
- virtualenv (recommandé)

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone https://github.com/diana-potupis-vinci/cinema-python-django.git
cd cinema-python-django
```

2. **Créer un environnement virtuel**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer la base de données**
```bash
python manage.py migrate
```

5. **Créer un superutilisateur**
```bash
python manage.py createsuperuser
```

6. **Collecter les fichiers statiques**
```bash
python manage.py collectstatic
```

7. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

L'application sera accessible à l'adresse : `http://127.0.0.1:8000/`

## ⚙️ Configuration

### Paramètres média
Les fichiers uploadés (affiches) sont stockés dans le dossier `media/img/`

## 📖 Utilisation

### Interface administrateur
Accédez à `/admin/` avec vos identifiants de superutilisateur pour :
- Gérer les films, acteurs, genres
- Créer des salles et séances
- Modérer les réservations

### Interface utilisateur
- **Page d'accueil** : Aperçu des films avec pagination
- **Films** : Liste complète des films disponibles
- **Séances** : Planning des séances
- **Réservations** : Gestion des réservations (utilisateurs connectés)

## 🗄️ Modèles de données

### Film
- Titre, description, durée
- Genre (ForeignKey)
- Affiche (ImageField)
- Acteurs (ManyToMany)

### Séance
- Film, date, heure
- Salle (ForeignKey)

### Réservation
- Utilisateur, séance
- Nombre de places
- Date de réservation

### Modèles auxiliaires
- **Genre** : Catégories de films
- **Acteur** : Informations des acteurs
- **Salle** : Salles de cinéma

## 🔗 API & URLs

```
/                          # Page d'accueil
/films/                    # Liste des films
/films/<id>/              # Détails d'un film
/films/add/               # Ajouter un film (admin)
/seances/                 # Liste des séances
/reservations/            # Mes réservations
/reservations/new/        # Nouvelle réservation
/login/                   # Connexion
/register/                # Inscription
/admin/                   # Interface d'administration
```

## 👥 Auteur

**Diana Potupis** - *Développement initial* - [diana-potupis-vinci](https://github.com/diana-potupis-vinci)
---

*Développé avec ❤️ dans le cadre du programme de développement web*