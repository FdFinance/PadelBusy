import streamlit as st
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Padel Business Plan Generator",
    page_icon="🎾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialisation du session state
if 'project_name' not in st.session_state:
    st.session_state.project_name = ""
if 'nb_terrains' not in st.session_state:
    st.session_state.nb_terrains = 4
if 'has_bar' not in st.session_state:
    st.session_state.has_bar = False
if 'has_proshop' not in st.session_state:
    st.session_state.has_proshop = False
if 'type_terrain' not in st.session_state:
    st.session_state.type_terrain = "Indoor"
if 'immobilier' not in st.session_state:
    st.session_state.immobilier = "Location"
if 'travaux' not in st.session_state:
    st.session_state.travaux = "Clé en main"

# Header
st.title("🎾 Générateur de Business Plan Padel")
st.markdown("### Créez votre business plan en 4 étapes simples")

# Navigation
st.sidebar.title("Navigation")
st.sidebar.info("""
**Étapes :**
1. 📋 Configuration du projet
2. 📍 Localisation & marché
3. 💰 Modèle économique
4. 📊 Business Plan final
""")

# Page d'accueil
st.markdown("""
## Bienvenue sur votre assistant de business plan

Cet outil vous permet de créer un business plan professionnel pour votre projet de club de padel en France.

### Comment ça marche ?

1. **Configurez votre projet** : nombre de terrains, services, type d'immobilier
2. **Choisissez votre localisation** : nous enrichissons avec des données du marché local
3. **Définissez votre modèle économique** : pricing, services complémentaires
4. **Obtenez votre business plan** : projections financières sur 3 ans, graphiques, export PDF

### Pourquoi utiliser cet outil ?

✅ **Données du marché réel** : prix, taux d'occupation, benchmarks par ville  
✅ **Calculs automatiques** : investissement, compte de résultat, seuil de rentabilité  
✅ **Scénarios multiples** : optimiste, réaliste, pessimiste  
✅ **Export professionnel** : business plan prêt à présenter aux banques

---

👉 **Commencez par la page "📋 Configuration" dans le menu de gauche**
""")

# Informations de contact
st.sidebar.markdown("---")
st.sidebar.markdown("**Besoin d'aide ?**")
st.sidebar.markdown("contact@padel-bp.fr")
st.sidebar.markdown(f"*Version MVP - {datetime.now().year}*")
