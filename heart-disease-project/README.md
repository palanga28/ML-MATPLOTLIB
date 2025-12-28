# Matplotlib - Heart Disease Project

## Nom du groupe : Matplotlib
**Dataset :** [Heart Disease UCI](https://archive.ics.uci.edu/dataset/45/heart+disease)
**Travail sur :** Maladie du cœur – prédiction à partir des données médicales

---

## 1. Règles de jeu définies par le professeur

1. Collecter les données  
2. Analyser et faire un rapport d'analyse  
3. Traiter les données en utilisant Pandas, NumPy ou PyTorch  
4. Concevoir le modèle de prédiction  
5. Entraîner le modèle  
6. Rédiger un rapport de l’évaluation des résultats d’entraînement et de test  
7. Rédiger un rapport de participation des membres

---

## 2. Structure du projet

```
heart-disease-project/
│
├── datasets/
│   ├── raw_data/          # Données brutes téléchargées depuis UCI
│   │   └── heart.csv
│   └── processed/         # Données nettoyées et traitées
│
├── src/
│   ├── dataset/
│   │   └── data_loader.py # Module pour charger le dataset et afficher un aperçu
│   ├── model/             # Contiendra la définition du modèle ML
│   ├── train.py           # Script pour entraîner le modèle
│   └── test.py            # Script pour tester et évaluer le modèle
│
├── main.py                # Point d’entrée pour exécuter le projet complet
├── README.md              # Documentation et instructions
├── requirements.txt       # Liste des packages Python requis
└── config.yml             # Paramètres globaux et hyperparamètres
```

### Importance de chaque fichier / dossier

| Fichier / Dossier        | Rôle / Importance |
|--------------------------|-----------------|
| `datasets/raw_data/`     | Contient les fichiers originaux téléchargés depuis UCI. Point de départ de toutes les analyses. |
| `datasets/processed/`    | Contient les données nettoyées et prétraitées, prêtes pour le modèle ML. |
| `src/dataset/data_loader.py` | Charge les données, ajoute les noms de colonnes, gère les valeurs manquantes. Étape clé avant tout traitement. |
| `src/model/`             | Contiendra les définitions des modèles de prédiction. |
| `src/train.py`           | Script d’entraînement du modèle sur le dataset traité. |
| `src/test.py`            | Évaluation et test du modèle sur un dataset indépendant. |
| `main.py`                | Coordonne toutes les étapes : chargement, nettoyage, entraînement, test, visualisation. |
| `README.md`              | Document explicatif : structure, étapes et instructions d’exécution. |
| `requirements.txt`       | Dépendances Python pour reproduire le projet sur n’importe quel ordinateur. |
| `config.yml`             | Paramètres globaux : chemins, hyperparamètres, choix de modèle, pour faciliter la maintenance et la reproductibilité. |

---

## 3. Ce qui a été fait

- Structure complète du projet créée conformément aux consignes  
- Dataset téléchargé et renommé `heart.csv` dans `datasets/raw_data/`  
- Module `data_loader.py` créé et testé :
  - Chargement du dataset  
  - Attribution des noms de colonnes  
  - Détection des valeurs manquantes (`ca` et `thal`)  
  - Aperçu des 5 premières lignes et infos générales  
- Installation des dépendances Python et création de `requirements.txt`

---

## 4. Étapes restantes

1. Analyse exploratoire des données (EDA)  
   - Histogrammes, boxplots  
   - Corrélations entre variables
2. Nettoyage et traitement des données  
   - Gestion des valeurs manquantes (`ca` et `thal`)  
   - Conversion de la colonne `target` en binaire (0/1)
3. Conception du modèle de prédiction  
   - Choix du modèle (ex : Logistic Regression, Random Forest…)  
   - Définition des hyperparamètres
4. Entraînement du modèle (`train.py`)  
   - Séparation train/test  
   - Entraînement et sauvegarde du modèle
5. Évaluation du modèle (`test.py`)  
   - Précision, recall, F1-score  
   - Visualisation des résultats
6. Rapports finaux  
   - Rapport d’analyse EDA  
   - Rapport de résultats d’entraînement/test  
   - Rapport de participation des membres

---

## 5. Répartition des tâches (branches Git)

| Membre           | Rôle / Tâche principale | Branche |
|-----------------|------------------------|---------|
| **Paul Palanga** | Chef de groupe, gestion de la branche `main`, coordination, merge requests | `main` |
| Tegra           | Analyse exploratoire et visualisation des données (EDA) | `tegramk-ux` |
| Van Bondo       | Nettoyage et prétraitement des données | `vanbondo` |
| Lamberto        | Conception et implémentation du modèle ML | `lamberto` |
| David           | Entraînement, évaluation et création des rapports finaux | `david` |

**Règles Git :**
- Chaque membre crée sa branche à partir de `main` :
```bash
git checkout main
git pull
git checkout -b prenom
```
- Après modification, push sur sa branche et faire une merge request vers `main`
- Le chef de groupe (Paul) gère les merges, rebase et conflits

---

## 6. Références utiles

- [train_test_split – scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)  
- Documentation Pandas, NumPy et Matplotlib pour traitement et visualisation

