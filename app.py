
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Configuration de l'application
st.set_page_config(
    page_title="Tarification automobile",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Tarification Automobile")
st.subheader("Simulation de la prime pure par Machine Learning")

st.write(
    "Estimation actuarielle fondée sur des modèles "
    "de fréquence (Poisson) et de coût moyen (Gamma)."
)

# Charger nos modèles enregistrés
fichier = Path(__file__).parent / "modeles" / "tarification_corrigee.joblib"

if not fichier.exists():
    st.error("Modèles introuvables. Exécute d'abord le notebook.")
    st.stop()

modeles = joblib.load(fichier)

model_poisson = modeles["poisson"]
model_gamma = modeles["gamma"]
variables = modeles["variables"]

st.header("Caractéristiques de l'assuré")

# Saisie des caractéristiques
age = st.slider("Âge du conducteur", 18, 100, 35)
veh_age = st.slider("Âge du véhicule", 0, 50, 6)
veh_power = st.slider("Classe de puissance du véhicule", 4, 15, 6)
bonus = st.slider("Bonus-malus", 50, 230, 70)

density = st.number_input(
    "Densité de population (hab./km²)",
    min_value=1,
    max_value=27000,
    value=400
)

# Construire les données pour la prédiction
donnees = pd.DataFrame([{
    "DrivAge": age,
    "VehAge": veh_age,
    "VehPower": veh_power,
    "BonusMalus": bonus,
    "Density": density
}], columns=variables)

# Lancer la simulation
if st.button("Calculer la prime pure", type="primary"):

    frequence = float(model_poisson.predict(donnees)[0])
    cout = float(model_gamma.predict(donnees)[0])

    prime = frequence * cout

    st.success("Simulation terminée !")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Fréquence annuelle", f"{frequence:.2%}")

    with col2:
        st.metric("Coût moyen", f"{cout:,.2f} €")

    st.metric("Prime pure annuelle", f"{prime:,.2f} €")

    st.info(
        "Cette prime est une estimation pédagogique. "
        "Elle n'inclut ni taxes, ni frais, ni chargements."
    )
