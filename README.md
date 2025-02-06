# 📊 DataExplorer AI Assistant

## Description
DataViz AI Assistant est une application interactive développée avec **Streamlit** et le modèle **Claude 3.5 Sonnet**, permettant aux utilisateurs d'analyser et de visualiser leurs données tabulaires grâce à l'intelligence artificielle.

## Fonctionnalités 🚀
- **Page d'accueil** : Présentation de l'outil avec un bouton menant vers l'interface d'analyse.
- **Chat interactif** : Un chatbot intelligent qui guide l'utilisateur dans l'exploration de ses données.
- **Importation de données** : Téléchargement de fichiers **CSV** pour analyse.
- **Nettoyage des données** :
  - Remplacement des valeurs nulles :
    - Variables numériques : médiane
    - Variables catégorielles : mode
  - Suppression des colonnes dupliquées
- **Exploration et visualisation** :
  - Description générale des données
  - Analyse spécifique de certaines colonnes ou variables
  - Génération automatique de graphiques pertinents

## Installation 🛠️
### Prérequis
- Python 3.12
- Poetry
- Anthropic
- Streamlit
- Pour la visualisation : seaborn, matplotlib, pandas..
- Clé API **Claude 3.5 Sonnet**


### Étapes d'installation
1. **Cloner le projet**
   ```bash
   git clone https://github.com/nadyby/DataExplorer
   cd DataExplorer
   ```
2. **Créer un environnement virtuel (optionnel mais recommandé)**
   ```bash
   poetry env use python
   poetry install
   poetry shell
   poetry build
   ```
3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configurer la clé API Claude**
   - Créer un fichier `.env` à la racine du projet et y ajouter la clé API :
     ```ini
     ANTHROPIC_API_KEY=ta_clé_API
     ```
   - Ajouter `.env` au fichier `.gitignore` pour éviter de commettre la clé API dans le dépôt Git.


## Utilisation 🖥️
1. **Lancer l'application**
   ```bash
   streamlit run chat.py
   ```
2. **Page d'accueil** : cliquer sur le bouton pour commencer l'exploration de vos données.
3. **Charger un fichier CSV** et interagir avec le chatbot pour explorer et visualiser les données.

## Exemples de requêtes 💡
- "Donne-moi une description générale des données."
- "Affiche-moi un histogramme de la colonne 'âge'."
- "y a t-il les valeurs manquantes dans mon dataset ?"
- "Génère un scatter plot entre 'revenu' et 'score_credit'."

## Contributeurs 🤝
- **Jihed BHAR**
- **Nadia BEN YOUSSEF**

## Licence 📜
Ce projet est sous licence **MIT**.
