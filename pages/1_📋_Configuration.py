import streamlit as st
import sys
sys.path.append('/home/claude/padel-bp-generator')

st.set_page_config(page_title="Configuration", page_icon="📋", layout="wide")

st.title("📋 Configuration de votre projet")
st.markdown("### Étape 1/4 : Définissez les caractéristiques de votre club")

# Nom du projet
st.markdown("#### Informations générales")
col1, col2 = st.columns(2)
with col1:
    project_name = st.text_input(
        "Nom de votre projet",
        value=st.session_state.get('project_name', ''),
        placeholder="Ex: Padel Club Bordeaux Sud"
    )
    st.session_state.project_name = project_name

# Configuration des terrains
st.markdown("---")
st.markdown("#### 🎾 Configuration des terrains")

col1, col2, col3 = st.columns(3)

with col1:
    nb_terrains = st.slider(
        "Nombre de terrains",
        min_value=2,
        max_value=12,
        value=st.session_state.get('nb_terrains', 4),
        step=1,
        help="La plupart des clubs français ont entre 4 et 8 terrains"
    )
    st.session_state.nb_terrains = nb_terrains

with col2:
    type_terrain = st.selectbox(
        "Type de terrains",
        options=["Indoor", "Outdoor", "Mixte"],
        index=["Indoor", "Outdoor", "Mixte"].index(st.session_state.get('type_terrain', 'Indoor')),
        help="Indoor = couvert, Outdoor = extérieur, Mixte = les deux"
    )
    st.session_state.type_terrain = type_terrain

with col3:
    if type_terrain == "Mixte":
        ratio_indoor = st.slider(
            "% de terrains Indoor",
            min_value=0,
            max_value=100,
            value=50,
            step=10
        )
        st.session_state.ratio_indoor = ratio_indoor
        st.info(f"{int(nb_terrains * ratio_indoor/100)} Indoor + {int(nb_terrains * (100-ratio_indoor)/100)} Outdoor")

# Services annexes
st.markdown("---")
st.markdown("#### 🍹 Services annexes")

col1, col2 = st.columns(2)

with col1:
    has_bar = st.checkbox(
        "Bar / Restaurant",
        value=st.session_state.get('has_bar', False),
        help="Augmente l'investissement mais génère des revenus complémentaires importants"
    )
    st.session_state.has_bar = has_bar
    
    if has_bar:
        bar_size = st.radio(
            "Taille du bar",
            options=["50m²", "100m²"],
            horizontal=True
        )
        st.session_state.bar_size = bar_size

with col2:
    has_proshop = st.checkbox(
        "Pro Shop (boutique)",
        value=st.session_state.get('has_proshop', False),
        help="Vente de raquettes, balles, vêtements et accessoires"
    )
    st.session_state.has_proshop = has_proshop

# Configuration immobilier
st.markdown("---")
st.markdown("#### 🏢 Configuration immobilière")

col1, col2 = st.columns(2)

with col1:
    immobilier = st.selectbox(
        "Type d'immobilier",
        options=["Location", "Achat", "Construction"],
        index=["Location", "Achat", "Construction"].index(st.session_state.get('immobilier', 'Location')),
        help="Location = loyer mensuel, Achat = crédit, Construction = terrain nu + construction complète"
    )
    st.session_state.immobilier = immobilier

with col2:
    travaux = st.selectbox(
        "État et travaux",
        options=["Clé en main", "Travaux légers", "Travaux lourds"],
        index=["Clé en main", "Travaux légers", "Travaux lourds"].index(st.session_state.get('travaux', 'Clé en main')),
        help="Clé en main = prêt à l'emploi, Travaux légers = rafraîchissement, Travaux lourds = rénovation complète"
    )
    st.session_state.travaux = travaux

# Estimation surface
st.markdown("---")
st.markdown("#### 📏 Estimation de surface nécessaire")

# Calcul automatique de la surface
surface_par_terrain = 200  # m² par terrain (terrain + dégagements)
surface_base = surface_par_terrain * nb_terrains

surface_services = 0
if has_bar:
    surface_services += 100 if bar_size == "100m²" else 50
if has_proshop:
    surface_services += 30

surface_commune = 150  # Vestiaires, accueil, stockage

surface_totale = surface_base + surface_services + surface_commune
st.session_state.surface_totale = surface_totale

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Surface terrains", f"{surface_base} m²")
with col2:
    st.metric("Surface services", f"{surface_services} m²")
with col3:
    st.metric("**Surface totale**", f"**{surface_totale} m²**")

# Estimation préliminaire d'investissement
st.markdown("---")
st.markdown("#### 💰 Estimation préliminaire d'investissement")

from data.market_data import get_investment_cost

investment = get_investment_cost(
    type_terrain=type_terrain,
    nb_terrains=nb_terrains,
    has_bar=has_bar,
    has_proshop=has_proshop,
    bar_size=st.session_state.get('bar_size', '50m²'),
    travaux_type=travaux
)

st.session_state.investment_estimation = investment

col1, col2 = st.columns([2, 1])
with col1:
    st.info(f"""
    **Investissement initial estimé : {investment:,.0f} €**
    
    *Cette estimation inclut :*
    - Construction/aménagement des {nb_terrains} terrains {type_terrain.lower()}
    - Bâtiments annexes (vestiaires, accueil, stockage)
    - {'Bar/Restaurant, ' if has_bar else ''}{'Pro Shop, ' if has_proshop else ''}Équipements de base
    - Majoration pour travaux ({travaux})
    
    *Non inclus dans cette estimation préliminaire :*
    - Coût du terrain/local (location ou achat)
    - Fonds de roulement
    - Frais de notaire (si achat)
    """)

with col2:
    st.warning("""
    ⚠️ **Attention**
    
    Cette estimation sera affinée aux prochaines étapes en fonction de votre localisation et de vos choix économiques.
    """)

# Bouton de navigation
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col3:
    if st.button("➡️ Étape suivante : Localisation", type="primary", use_container_width=True):
        st.switch_page("pages/2_📍_Localisation.py")

# Résumé en sidebar
with st.sidebar:
    st.markdown("### 📋 Résumé Configuration")
    st.markdown(f"""
    **Projet :** {project_name if project_name else '*Non défini*'}
    
    **Terrains :** {nb_terrains} {type_terrain}
    
    **Services :**
    - {'✅' if has_bar else '❌'} Bar/Restaurant
    - {'✅' if has_proshop else '❌'} Pro Shop
    
    **Immobilier :** {immobilier}
    
    **Travaux :** {travaux}
    
    **Surface totale :** {surface_totale} m²
    
    **Investissement :** {investment:,.0f} €
    """)
