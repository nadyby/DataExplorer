# 📊 DataExplorer AI Assistant

## Description
DataViz AI Assistant est une application interactive développée avec **Streamlit** et le modèle **Claude 3.5 Sonnet**, permettant aux utilisateurs d'analyser et de visualiser leurs données tabulaires grâce à l'intelligence artificielle.

## 🌐 View the App

You can access the Streamlit-hosted application here:  
➡️ [DataExplorer AI Assistant](https://dataexplorerassistant.streamlit.app/)

## 📖 Documentation

The project documentation is available here:  
➡️ [DataExplorer Documentation](https://nadyby.github.io/DataExplorer/)

## Fonctionnalités 🚀
- **Page d'accueil** : Présentation de l'outil avec un bouton menant vers l'interface d'analyse.
- **Chat interactif** : Un chatbot intelligent qui guide l'utilisateur dans l'exploration de ses données.
- **Importation de données** : Téléchargement de fichiers **CSV** pour analyse.
- **Nettoyage des données** :
  - Remplacement des valeurs nulles :
    - Variables numériques : médiane
    - Variables catégorielles : mode
  - Suppression des colonnes dupliquées.
- **Exploration et visualisation** :
  - Description générale des données.
  - Analyse spécifique de certaines colonnes ou variables.
  - Génération automatique de graphiques pertinents avec une interprétation détaillée.

## Structure du projet 📂

Voici une vue d'ensemble des fichiers et dossiers principaux du projet :

```plaintext
├── .devcontainer/            # Configuration du conteneur de développement  
├── .github/workflows/        # Fichiers de workflows GitHub Actions  
├── dist/                     # Distribution des fichiers builds  
├── docs/                     # Documentation du projet  
├── images/                   # Aperçu de l'application  
├── src/                      # Code source principal de l'application  
│   ├── dataexplorer/         # Dossier principal  
│   │   ├── chat.py           # Implementation de l'application  
│   │   ├── utils.py          # Fichier responsable du nettoyage des données  
├── tests/                    # Tests unitaires et fonctionnels  
│   │   ├── test_load_data.py # Fichier pour tester le chargement des données  
├── .coverage                 # Rapport de couverture des tests  
├── .gitignore                # Liste des fichiers ignorés par Git  
├── .pre-commit-config.yaml   # Configuration pour pre-commit  
├── poetry.lock               # Verrouillage des dépendances Python  
├── pyproject.toml            # Fichier de configuration pour Poetry  
├── README.md                 # Documentation principale du projet  
 
```

## Installation 🛠️
### Prérequis
- Python 3.12
- Poetry
- Clé API **Anthropic** pour pourvoir accéder au modèle **Claude 3.5 Sonnet**


### Étapes d'installation
1. **Cloner le projet**
   ```bash
   git clone https://github.com/nadyby/DataExplorer
   cd DataExplorer
   ```
2. **Créer un environnement virtuel (optionnel mais recommandé)**
   ```bash
   poetry env use python
   poetry shell
   poetry build
   ```
3. **Installer les dépendances**
   ```bash
   poetry install
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
   cd src
   cd dataexplorer
   poetry run streamlit run chat.py
   ```
2. **Page d'accueil** : Cliquer sur le bouton pour commencer l'exploration de vos données.
![accueil](images/accueil.png)

3. **Charger un fichier CSV** : L'application propose un bouton pour effectuer un nettoyage des données avant de permettre l'analyse et la visualisation.
![chatbot](images/chat.png)
![dataset](images/dataset.png)

4. **Interagir avec le chatbot** pour explorer et visualiser les données.
![plot](images/exemple_plot.jpeg)


## Exemples de requêtes 💡
- "Donne-moi une description générale des données."
- "Affiche-moi un histogramme de la colonne 'âge'."
- "Y a t-il les valeurs manquantes dans mon dataset ?"
- "Génère un scatter plot entre 'revenu' et 'score_credit'."

## Contributeurs 🤝
- **Jihed BHAR**
- **Nadia BEN YOUSSEF**

## Licence 📜
Ce projet est sous licence **MIT**.
