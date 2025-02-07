
Installation
==========================


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
   poetry install 
   ```
4. **Configurer la clé API Claude**
   - Créer un fichier `.env` à la racine du projet et y ajouter la clé API :
     ```ini
     ANTHROPIC_API_KEY=ta_clé_API
     ```
   - Ajouter `.env` au fichier `.gitignore` pour éviter de commettre la clé API dans le dépôt Git.