# LOG3000 - Calculatrice simple
Équipe 15

## Description
Ce projet est une application web développée en Python et utilisant la librairie Flask. Celle-ci fournit une calculatrice simple permettant d'effectuer des calculs arithmétiques de base. L'objectif de ce projet est de documenter, collaborer, tester et régler les bogues dans le cadre du developpement.

## Portée du projet
- Implémenter une interface utilisateur de calculatrice.
- Offrir des calculs arithmetiques de base: addition, soustraction, multiplication et division.
- Gérer les erreurs lors d'expressions invalides ou trop complexes et informer l'utilisateur de celles-ci.
- Documenter le projet.

## Prérequis
Avant de lancer le projet, il faut avoir d'installé localement:
- Python 3.10+
- pip
- Git

Ainsi qu'avoir un compte Github.


## Instructions d'installation
1. Cloner le dépôt localement
`git clone https://github.com/crisscrosstheroad/TP3---LOG3000.git`

2. Se diriger dans le répertoire du projet
`cd TP3---LOG3000`

3. Installer les dépendances
`pip install flask`

## Instructions d'utilisation
1. Lancer l'application à partir de la racine du projet
`python app.py`

2. Ouvrir l'application dans le navigateur. Celle-ci sera disponible à l'addresse `http://127.0.0.1:5000/`

3. Utiliser l'application: la calculatrice est composée de boutons cliquables représentant les operateurs et les opérantes. Le bouton C sert à vider l'écran et le = sert à calculer l'expression mathématique et afficher le résultat.

## Exécution des tests
Afin d'exécuter les tests, il faut lancer la commande `python -m unittest discover tests` dans la racine du projet.
Pour exécuter des tests spécifiques, il faut lancer la commande `python -m unittest tests.test_filename`

## Flux de contribution
- Issues:
    - Avant d'implémenter une nouvelle fonctionnalité, corriger un bogue ou créer une branche ou ouvrir une PR, il faut créer un issue sur Github afin de documenter les fonctionnalités à ajouter ou les bogues à corriger. Plus spécifiquement, il faut décrire le problème ou la nouvelle fonctionnalité, fournir les étapes de reproduction ou les cas de test en échec si c'est une correction de bogue et assigner l'issue à un membre de l'équipe.
- Branches: 
    - pour chaque nouvelle fonctionnalité, une branche sous le nom de `feature/[description-fonctionnalité]` doit être créée. La description doit être courte.
    - pour chaque correction de bogue, une branche sous le nom de `bugfix/[description-bogue]` doit être créée. La description doit être courte.
- PR:
    - Après avoir poussé la branche au remote et poussé tout changement pertinent sur la branche, il faut créer une PR vers la branche main et assigner un membre de l'équipe pour que celui-ci la passe en revue et l'approuve. Après avoir été approuvée, la PR peut être fusionnée à la branche main.
