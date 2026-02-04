import streamlit as st
import sys
sys.path.append('/home/claude/padel-bp-generator')
from data.conseils import (
    get_conseils_personnalises,
    get_conseil_service,
    CONSEILS_FINANCEMENT,
    CONSEILS_JURIDIQUE,
    CONSEILS_MARKETING,
    CONSEILS_EXPLOITATION,
    CONSEILS_PRICING
)

st.set_page_config(page_title="Conseils Personnalises", page_icon="💡", layout="wide")

st.title("💡 Conseils Personnalisés")
st.markdown("### Votre guide pour réussir votre projet de club de padel")

# Vérification des étapes précédentes
if 'nb_terrains' not in st.session_state or 'city' not in st.session_state:
    st.warning("⚠️ Veuillez d'abord compléter les étapes de configuration et localisation")
    if st.button("← Retour à la configuration"):
        st.switch_page("pages/1_📋_Configuration.py")
    st.stop()

# Récupération de la configuration
from data.market_data import get_city_data
city_data = get_city_data(st.session_state.city)

config = {
    "nb_terrains": st.session_state.nb_terrains,
    "type_terrain": st.session_state.type_terrain,
    "immobilier": st.session_state.immobilier,
    "has_bar": st.session_state.has_bar,
    "has_proshop": st.session_state.has_proshop,
    "city": st.session_state.city,
    "taux_occupation_marche": city_data['taux_occupation_moyen'],
    "investment_total": st.session_state.get('total_investment', st.session_state.get('investment_estimation', 0))
}

# Génération des conseils personnalisés
conseils = get_conseils_personnalises(config)

# ═══════════════════════════════════════════════════════════════════
# SECTION 1: ALERTES ET CONSEILS PRIORITAIRES
# ═══════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 🎯 Conseils prioritaires pour votre projet")

if conseils["prioritaires"]:
    for conseil in conseils["prioritaires"]:
        if conseil["type"] == "attention":
            st.warning(f"""
            ⚠️ **{conseil['titre']}**

            {conseil['message']}
            """)
        elif conseil["type"] == "opportunite":
            st.success(f"""
            ✅ **{conseil['titre']}**

            {conseil['message']}
            """)
        else:
            st.info(f"""
            💡 **{conseil['titre']}**

            {conseil['message']}
            """)
else:
    st.success("✅ Votre configuration semble équilibrée. Découvrez nos conseils détaillés ci-dessous.")

# ═══════════════════════════════════════════════════════════════════
# SECTION 2: CONSEILS CONFIGURATION
# ═══════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 🏗️ Conseils sur votre configuration")

# Tabs pour les différents aspects
tab1, tab2, tab3 = st.tabs(["📊 Nombre de terrains", "🎾 Type de terrains", "🏢 Immobilier"])

with tab1:
    conseil_terrains = conseils["configuration"]["terrains"]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**✅ Avantages de votre choix**")
        for avantage in conseil_terrains.get("avantages", []):
            st.markdown(f"- {avantage}")

    with col2:
        st.markdown("**⚠️ Points de vigilance**")
        for inconvenient in conseil_terrains.get("inconvenients", []):
            st.markdown(f"- {inconvenient}")

    st.markdown("**💡 Nos conseils**")
    for conseil in conseil_terrains.get("conseils", []):
        st.info(conseil)

with tab2:
    conseil_type = conseils["configuration"]["type"]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**✅ Avantages**")
        for avantage in conseil_type.get("avantages", []):
            st.markdown(f"- {avantage}")

    with col2:
        st.markdown("**⚠️ Inconvénients**")
        for inconvenient in conseil_type.get("inconvenients", []):
            st.markdown(f"- {inconvenient}")

    st.markdown("**💡 Nos conseils**")
    for conseil in conseil_type.get("conseils", []):
        st.info(conseil)

with tab3:
    conseil_immo = conseils["configuration"]["immobilier"]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**✅ Avantages**")
        for avantage in conseil_immo.get("avantages", []):
            st.markdown(f"- {avantage}")

    with col2:
        st.markdown("**⚠️ Inconvénients**")
        for inconvenient in conseil_immo.get("inconvenients", []):
            st.markdown(f"- {inconvenient}")

    st.markdown("**💡 Nos conseils**")
    for conseil in conseil_immo.get("conseils", []):
        st.info(conseil)

# ═══════════════════════════════════════════════════════════════════
# SECTION 3: ANALYSE DU MARCHE
# ═══════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown(f"## 📍 Analyse du marché à {st.session_state.city}")

conseil_marche = conseils["marche"]

st.markdown(f"**{conseil_marche['analyse']}**")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ✅ Opportunités")
    for opp in conseil_marche.get("opportunites", []):
        st.success(opp)

with col2:
    st.markdown("### ⚠️ Risques")
    for risque in conseil_marche.get("risques", []):
        st.warning(risque)

st.markdown("### 💡 Conseils stratégiques pour ce marché")
for conseil in conseil_marche.get("conseils", []):
    st.info(conseil)

# ═══════════════════════════════════════════════════════════════════
# SECTION 4: CONSEILS SERVICES
# ═══════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 🎯 Conseils pour vos services")

services_tabs = st.tabs(["🍹 Bar/Restaurant", "🛒 Pro Shop", "👨‍🏫 Cours", "🏆 Tournois"])

with services_tabs[0]:
    conseil_bar = get_conseil_service("bar")

    if st.session_state.has_bar:
        st.success("✅ Vous avez choisi d'inclure un bar - excellente décision !")
    else:
        st.warning("⚠️ Vous n'avez pas prévu de bar. Voici pourquoi vous devriez y réfléchir :")

    st.markdown("**Pourquoi un bar ?**")
    for point in conseil_bar.get("pourquoi", []):
        st.markdown(f"- {point}")

    st.markdown("**💡 Conseils d'exploitation**")
    for conseil in conseil_bar.get("conseils", []):
        st.info(conseil)

    with st.expander("⚠️ Points de vigilance"):
        for risque in conseil_bar.get("risques", []):
            st.markdown(f"- {risque}")

with services_tabs[1]:
    conseil_shop = get_conseil_service("proshop")

    if st.session_state.has_proshop:
        st.success("✅ Vous avez prévu un Pro Shop")
    else:
        st.info("ℹ️ Vous n'avez pas prévu de Pro Shop. C'est optionnel mais peut être intéressant.")

    st.markdown("**Pourquoi un Pro Shop ?**")
    for point in conseil_shop.get("pourquoi", []):
        st.markdown(f"- {point}")

    st.markdown("**💡 Conseils**")
    for conseil in conseil_shop.get("conseils", []):
        st.info(conseil)

with services_tabs[2]:
    conseil_cours = get_conseil_service("cours")

    st.markdown("**Pourquoi proposer des cours ?**")
    for point in conseil_cours.get("pourquoi", []):
        st.markdown(f"- {point}")

    st.markdown("**💡 Conseils**")
    for conseil in conseil_cours.get("conseils", []):
        st.info(conseil)

    st.markdown("**💰 Tarification recommandée**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Cours particulier", "45-60€/h")
    with col2:
        st.metric("Cours collectif (4 pers.)", "15-20€/pers.")
    with col3:
        st.metric("Stage semaine", "150-250€/pers.")

with services_tabs[3]:
    conseil_tournois = get_conseil_service("tournois")

    st.markdown("**Pourquoi organiser des tournois ?**")
    for point in conseil_tournois.get("pourquoi", []):
        st.markdown(f"- {point}")

    st.markdown("**💡 Conseils**")
    for conseil in conseil_tournois.get("conseils", []):
        st.info(conseil)

    st.markdown("**💰 Revenus moyens par type de tournoi**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Tournoi amateur", "800-1200€ net")
    with col2:
        st.metric("Tournoi entreprise", "1500-3000€ net")
    with col3:
        st.metric("Tournoi homologué FFT", "1000-2000€ net")

# ═══════════════════════════════════════════════════════════════════
# SECTION 5: CONSEILS FINANCEMENT
# ═══════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 💰 Conseils financement")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💵 Apport personnel")
    st.metric("Minimum recommandé", "25-30%", help="De l'investissement total")

    for conseil in CONSEILS_FINANCEMENT["apport_personnel"]["conseils"]:
        st.info(conseil)

with col2:
    st.markdown("### 🏦 Prêt bancaire")
    st.metric("Taux actuel moyen", "4-5.5%", help="Taux 2025")

    for conseil in CONSEILS_FINANCEMENT["pret_bancaire"]["conseils"][:3]:
        st.info(conseil)

st.markdown("### 🎁 Aides et subventions possibles")
for aide in CONSEILS_FINANCEMENT["aides_et_subventions"]["types"]:
    st.markdown(f"- {aide}")

st.info("💡 **Conseil** : Renseignez-vous auprès de votre CCI locale et de BPI France pour connaître toutes les aides disponibles dans votre région.")

# ═══════════════════════════════════════════════════════════════════
# SECTION 6: CONSEILS JURIDIQUE
# ═══════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## ⚖️ Conseils juridiques et réglementaires")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📋 Statuts juridiques recommandés")

    for statut, details in CONSEILS_JURIDIQUE["statuts_recommandes"].items():
        with st.expander(f"**{statut}**"):
            st.markdown("**Avantages :**")
            for av in details["avantages"]:
                st.markdown(f"- {av}")
            st.markdown("**Inconvénients :**")
            for inc in details["inconvenients"]:
                st.markdown(f"- {inc}")

with col2:
    st.markdown("### 📜 Réglementations obligatoires")
    for regle in CONSEILS_JURIDIQUE["reglementations"]:
        st.markdown(f"- {regle}")

st.markdown("### 💡 Conseils juridiques")
for conseil in CONSEILS_JURIDIQUE["conseils"]:
    st.info(conseil)

# ═══════════════════════════════════════════════════════════════════
# SECTION 7: CONSEILS MARKETING
# ═══════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 📢 Conseils marketing")

tab_mkt1, tab_mkt2, tab_mkt3 = st.tabs(["🚀 Avant ouverture", "🎉 Lancement", "🔄 Actions récurrentes"])

with tab_mkt1:
    st.markdown("**Actions recommandées 3-4 mois avant l'ouverture :**")
    for action in CONSEILS_MARKETING["avant_ouverture"]:
        st.info(action)

with tab_mkt2:
    st.markdown("**Actions pour le lancement :**")
    for action in CONSEILS_MARKETING["lancement"]:
        st.info(action)

with tab_mkt3:
    st.markdown("**Actions marketing récurrentes :**")
    for action in CONSEILS_MARKETING["recurrent"]:
        st.info(action)

st.metric("Budget marketing recommandé", "5-10% du CA", help="La première année, puis 3-5% les années suivantes")

# ═══════════════════════════════════════════════════════════════════
# SECTION 8: CONSEILS EXPLOITATION
# ═══════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 🛠️ Conseils d'exploitation")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👥 Équipe recommandée")
    st.markdown(f"*Pour {st.session_state.nb_terrains} terrains :*")

    equipe = CONSEILS_EXPLOITATION["personnel"]["equipe_type_4_terrains"]
    if st.session_state.nb_terrains > 6:
        st.markdown("- 1 gérant/manager")
        st.markdown("- 2 agents d'accueil (temps plein)")
        st.markdown("- 1 agent d'entretien (temps plein)")
        st.markdown("- 2-3 professeurs (vacataires)")
    else:
        for membre in equipe:
            st.markdown(f"- {membre}")

with col2:
    st.markdown("### ⏰ Horaires d'ouverture conseillés")
    st.markdown(f"**Semaine :** {CONSEILS_EXPLOITATION['horaires']['semaine']}")
    st.markdown(f"**Weekend :** {CONSEILS_EXPLOITATION['horaires']['weekend']}")

    for conseil in CONSEILS_EXPLOITATION["horaires"]["conseils"]:
        st.info(conseil)

st.markdown("### 🧹 Maintenance")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Quotidien**")
    for task in CONSEILS_EXPLOITATION["maintenance"]["quotidien"]:
        st.markdown(f"- {task}")

with col2:
    st.markdown("**Hebdomadaire**")
    for task in CONSEILS_EXPLOITATION["maintenance"]["hebdomadaire"]:
        st.markdown(f"- {task}")

with col3:
    st.markdown("**Annuel**")
    for task in CONSEILS_EXPLOITATION["maintenance"]["annuel"]:
        st.markdown(f"- {task}")

st.metric("Budget maintenance", "3-5% du CA annuel")

# ═══════════════════════════════════════════════════════════════════
# SECTION 9: CHECKLIST DE LANCEMENT
# ═══════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## ✅ Checklist de lancement")

checklist = {
    "Étude de marché": [
        "Analyse de la concurrence locale",
        "Étude du bassin de population",
        "Validation du potentiel de clientèle"
    ],
    "Administratif & Juridique": [
        "Création de la structure juridique (SAS/SARL)",
        "Demande d'autorisation ERP",
        "Souscription assurance RC Pro",
        "Ouverture compte bancaire professionnel"
    ],
    "Immobilier & Travaux": [
        "Signature bail ou acte d'achat",
        "Obtention du permis de construire (si nécessaire)",
        "Sélection des entreprises de travaux",
        "Suivi du chantier"
    ],
    "Financement": [
        "Business plan finalisé",
        "Dossier de prêt bancaire",
        "Demande de subventions/aides",
        "Apport personnel disponible"
    ],
    "Marketing & Communication": [
        "Création identité visuelle (logo, charte graphique)",
        "Site web et système de réservation",
        "Réseaux sociaux actifs",
        "Plan de communication lancement"
    ],
    "Exploitation": [
        "Recrutement de l'équipe",
        "Sélection fournisseurs (boissons, équipements)",
        "Formation de l'équipe",
        "Test du système de réservation"
    ]
}

for categorie, items in checklist.items():
    with st.expander(f"📋 {categorie}"):
        for item in items:
            st.checkbox(item, key=f"check_{categorie}_{item}")

# ═══════════════════════════════════════════════════════════════════
# NAVIGATION
# ═══════════════════════════════════════════════════════════════════

st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("← Business Plan", use_container_width=True):
        st.switch_page("pages/4_📊_Business_Plan.py")

with col2:
    if st.button("🏠 Accueil", use_container_width=True):
        st.switch_page("app.py")

with col3:
    if st.button("📋 Modifier configuration", use_container_width=True):
        st.switch_page("pages/1_📋_Configuration.py")

# Sidebar
with st.sidebar:
    st.markdown("### 💡 Votre profil projet")
    st.markdown(f"""
    **Projet :** {st.session_state.get('project_name', 'Non défini')}

    **Configuration :**
    - {st.session_state.nb_terrains} terrains {st.session_state.type_terrain}
    - {'Bar ✅' if st.session_state.has_bar else 'Bar ❌'}
    - {'Pro Shop ✅' if st.session_state.has_proshop else 'Pro Shop ❌'}

    **Localisation :** {st.session_state.city}

    **Investissement :** {config['investment_total']:,.0f}€
    """)

    st.markdown("---")
    st.markdown("### 📞 Besoin d'accompagnement ?")
    st.markdown("""
    Nos experts peuvent vous accompagner dans votre projet :
    - Étude de faisabilité approfondie
    - Recherche de financement
    - Accompagnement juridique

    📧 contact@padel-bp.fr
    """)
