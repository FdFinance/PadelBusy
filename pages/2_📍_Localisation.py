import streamlit as st
import sys
sys.path.append('/home/claude/padel-bp-generator')
from data.market_data import get_all_cities, get_city_data

st.set_page_config(page_title="Localisation", page_icon="📍", layout="wide")

st.title("📍 Localisation & Analyse de marché")
st.markdown("### Étape 2/4 : Choisissez votre ville et découvrez le marché local")

# Vérification que la configuration a été faite
if 'nb_terrains' not in st.session_state:
    st.warning("⚠️ Veuillez d'abord compléter la configuration de votre projet")
    if st.button("← Retour à la configuration"):
        st.switch_page("pages/1_📋_Configuration.py")
    st.stop()

# Sélection de la ville
st.markdown("#### 🗺️ Sélection de la localisation")

cities = get_all_cities()
selected_city = st.selectbox(
    "Ville d'implantation",
    options=cities,
    index=cities.index(st.session_state.get('city', 'Paris')) if st.session_state.get('city') in cities else 0,
    help="Sélectionnez la ville où vous souhaitez implanter votre club"
)
st.session_state.city = selected_city

# Récupération des données de marché
city_data = get_city_data(selected_city)

# Affichage des données de marché
st.markdown("---")
st.markdown(f"#### 📊 Analyse du marché du padel à {selected_city}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Prix moyen/heure",
        f"{city_data['prix_moyen_heure_semaine']}€",
        help="Prix moyen d'une heure de jeu en semaine"
    )
    st.caption(f"Weekend: {city_data['prix_moyen_heure_weekend']}€")

with col2:
    st.metric(
        "Clubs existants",
        city_data['nb_clubs_existants'],
        help="Nombre de clubs de padel déjà présents dans la ville"
    )

with col3:
    st.metric(
        "Taux d'occupation",
        f"{int(city_data['taux_occupation_moyen']*100)}%",
        help="Taux d'occupation moyen des clubs existants"
    )

with col4:
    st.metric(
        "Population (5km)",
        f"{city_data['population_bassin_5km']:,.0f}",
        help="Population dans un rayon de 5km (bassin de clientèle typique)"
    )

# Données immobilières
st.markdown("---")
st.markdown("#### 🏢 Données immobilières locales")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Location",
        f"{city_data['prix_m2_location_mensuel']}€/m²/mois",
        help="Prix moyen de location au m² par mois"
    )
    loyer_mensuel = city_data['prix_m2_location_mensuel'] * st.session_state.surface_totale
    st.caption(f"Soit ~{loyer_mensuel:,.0f}€/mois pour {st.session_state.surface_totale}m²")

with col2:
    st.metric(
        "Achat",
        f"{city_data['prix_m2_achat']:,.0f}€/m²",
        help="Prix moyen d'achat au m²"
    )
    prix_achat = city_data['prix_m2_achat'] * st.session_state.surface_totale
    st.caption(f"Soit ~{prix_achat:,.0f}€ pour {st.session_state.surface_totale}m²")

with col3:
    st.metric(
        "Revenu moyen",
        f"{city_data['revenu_moyen_menage']:,.0f}€",
        help="Revenu moyen annuel par ménage"
    )

# Sauvegarde des coûts immobiliers
st.session_state.loyer_mensuel = loyer_mensuel
st.session_state.prix_achat = prix_achat

# Analyse concurrentielle
st.markdown("---")
st.markdown("#### 🎯 Positionnement concurrentiel")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
    **Clubs premium identifiés à {selected_city} :**
    """)
    for club in city_data['clubs_premium']:
        st.markdown(f"- {club}")
    
    st.markdown(f"""
    
    **Analyse du marché :**
    - Le marché compte actuellement **{city_data['nb_clubs_existants']} clubs**
    - Le taux d'occupation moyen est de **{int(city_data['taux_occupation_moyen']*100)}%**
    - {'✅ **Marché mature avec forte demande**' if city_data['taux_occupation_moyen'] > 0.65 else '⚠️ **Marché en développement**'}
    """)

with col2:
    if city_data['taux_occupation_moyen'] > 0.70:
        st.success("""
        ✅ **Opportunité forte**
        
        Marché dynamique avec forte occupation. Les clubs existants sont saturés, ce qui indique un potentiel pour de nouveaux entrants.
        """)
    elif city_data['taux_occupation_moyen'] > 0.60:
        st.info("""
        ℹ️ **Opportunité modérée**
        
        Marché équilibré. Positionnement et différenciation importants pour capter la clientèle.
        """)
    else:
        st.warning("""
        ⚠️ **Vigilance requise**
        
        Marché encore en développement. Privilégier un investissement prudent et prévoir une montée en charge progressive.
        """)

# Potentiel de clientèle
st.markdown("---")
st.markdown("#### 👥 Potentiel de clientèle")

# Calcul du potentiel
population = city_data['population_bassin_5km']
taux_pratiquants = 0.025  # 2.5% de pratiquants estimés (croissance du padel)
pratiquants_potentiels = int(population * taux_pratiquants)
nb_terrains_ville = city_data['nb_clubs_existants'] * 5  # Moyenne 5 terrains/club
nb_terrains_total_futur = nb_terrains_ville + st.session_state.nb_terrains

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Pratiquants potentiels",
        f"{pratiquants_potentiels:,}",
        help="Estimation : 2.5% de la population (taux de croissance du padel en France)"
    )

with col2:
    st.metric(
        "Terrains actuels",
        nb_terrains_ville,
        help=f"Estimation basée sur {city_data['nb_clubs_existants']} clubs × 5 terrains/club en moyenne"
    )

with col3:
    st.metric(
        "Terrains futurs",
        nb_terrains_total_futur,
        delta=f"+{st.session_state.nb_terrains}",
        help="Total de terrains après votre implantation"
    )

ratio_pratiquants_terrain = pratiquants_potentiels / nb_terrains_total_futur if nb_terrains_total_futur > 0 else 0

st.info(f"""
📈 **Ratio pratiquants/terrain après votre implantation : {ratio_pratiquants_terrain:.0f} pratiquants par terrain**

{'✅ Ratio favorable (> 100 pratiquants/terrain)' if ratio_pratiquants_terrain > 100 else '⚠️ Ratio serré, différenciation importante'}
""")

# Recommandation de pricing
st.markdown("---")
st.markdown("#### 💡 Recommandation de pricing")

prix_suggest_semaine = city_data['prix_moyen_heure_semaine']
prix_suggest_weekend = city_data['prix_moyen_heure_weekend']

col1, col2 = st.columns(2)
with col1:
    st.info(f"""
    **Prix suggéré semaine :** {prix_suggest_semaine}€/heure
    
    Basé sur la moyenne du marché local. Vous pourrez ajuster selon votre positionnement (premium ou accessible).
    """)

with col2:
    st.info(f"""
    **Prix suggéré weekend :** {prix_suggest_weekend}€/heure
    
    Les weekends commandent généralement une prime de 15-20% sur les prix en semaine.
    """)

# Sauvegarde des prix suggérés
st.session_state.prix_suggest_semaine = prix_suggest_semaine
st.session_state.prix_suggest_weekend = prix_suggest_weekend

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("← Configuration", use_container_width=True):
        st.switch_page("pages/1_📋_Configuration.py")

with col3:
    if st.button("➡️ Modèle économique", type="primary", use_container_width=True):
        st.switch_page("pages/3_💰_Modele_Economique.py")

# Sidebar résumé
with st.sidebar:
    st.markdown("### 📍 Résumé Localisation")
    st.markdown(f"""
    **Ville :** {selected_city}
    
    **Marché :**
    - {city_data['nb_clubs_existants']} clubs existants
    - Taux occupation : {int(city_data['taux_occupation_moyen']*100)}%
    
    **Prix marché :**
    - Semaine : {prix_suggest_semaine}€/h
    - Weekend : {prix_suggest_weekend}€/h
    
    **Immobilier :**
    - Location : {loyer_mensuel:,.0f}€/mois
    - Achat : {prix_achat:,.0f}€
    """)
