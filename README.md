
# Tarification du risque automobile par Machine Learning

## Présentation du projet

Projet personnel réalisé dans le cadre du développement
de mes compétences en Finance, Actuariat et Data Science.

L'objectif est d'estimer la prime pure annuelle d'un
contrat d'assurance automobile à partir de données
historiques et de modèles statistiques.

## Dataset

Source : freMTPL2, données françaises d'assurance
automobile disponibles sur OpenML.

- freMTPL2freq : fréquence des sinistres
- freMTPL2sev : montants des sinistres

L'analyse initiale porte sur 678 013 contrats.
Le premier entraînement utilise 100 000 contrats.

## Méthodologie

1. Importation et nettoyage des données
2. Analyse exploratoire
3. Calcul des indicateurs actuariels
4. Régression de Poisson pour la fréquence
5. Régression Gamma pour le coût moyen
6. Estimation de la prime pure
7. Évaluation des prédictions
8. Développement d'une application Streamlit

Prime pure = Fréquence prédite × Coût moyen prédit

## Technologies

- Python
- Pandas et NumPy
- Matplotlib et Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

## Résultats préliminaires

Modèle corrigé :

- MAE : 277,84
- MAE de référence : 278,82
- Déviance Tweedie : 77,8932
- Déviance de référence : 78,4012

Le modèle corrigé améliore légèrement la référence
sur le jeu de test étudié.

## Application Streamlit

L'application permet de saisir :
- L'âge du conducteur
- L'âge du véhicule
- La puissance du véhicule
- Le bonus-malus
- La densité de population

Elle affiche la fréquence, le coût moyen et la
prime pure annuelle estimée.

## Limites

Ce projet est une étude pédagogique.

Les données concernent le marché français.
Certaines observations ont été harmonisées pour
la modélisation des sinistres à coût positif.

Le jeu de test a servi à examiner les corrections :
une validation indépendante reste nécessaire.

Les résultats ne constituent pas une tarification
commerciale validée.

## Auteur

Projet personnel — Master Finance, Actuariat
et Data Science.

## Installation et utilisation

### 1. Télécharger le projet
Télécharger le repository au format ZIP depuis GitHub,
puis extraire les fichiers.

### 2. Installer les bibliothèques
Ouvrir le dossier du projet dans VS Code,
puis exécuter dans le terminal :

python -m pip install -r requirements.txt

### 3. Lancer l'application Streamlit

python -m streamlit run app.py

### 4. Utiliser le simulateur
Renseigner les caractéristiques du conducteur
et du véhicule, puis cliquer sur
"Calculer la prime pure".

L'application utilise les modèles Poisson
et Gamma enregistrés dans le dossier modeles.

Note : les modèles ont été entraînés localement.
Des versions compatibles de Python et
scikit-learn sont nécessaires pour les charger.
