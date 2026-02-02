import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import sys
sys.path.append('/home/claude/padel-bp-generator')
from data.market_data import get_monthly_costs

st.set_page_config(page_title="Business Plan", page_icon="📊", layout="wide")

st.title("📊 Votre Business Plan Padel")
st.markdown(f"### Projet : {st.session_state.get('project_name', 'Sans nom')} - {st.session_state.get('city', '')}")

# Vérification
if 'nb_terrains' not in st.session_state or 'city' not in st.session_state:
    st.warning("⚠️ Veuillez compléter toutes les étapes précédentes")
    if st.button("← Retour"):
        st.switch_page("pages/1_📋_Configuration.py")
    st.stop()

# Récapitulatif du projet
st.markdown("---")
st.markdown("#### 📋 Récapitulatif du projet")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Terrains", f"{st.session_state.nb_terrains} {st.session_state.type_terrain}")
    
with col2:
    services = []
    if st.session_state.has_bar:
        services.append("Bar")
    if st.session_state.has_proshop:
        services.append("Shop")
    if st.session_state.get('propose_cours', False):
        services.append("Cours")
    st.metric("Services", ", ".join(services) if services else "Location seule")

with col3:
    st.metric("Ville", st.session_state.city)

with col4:
    st.metric("Surface", f"{st.session_state.surface_totale} m²")

# Investissement initial
st.markdown("---")
st.markdown("### 💰 Investissement Initial")

investment = st.session_state.investment_estimation
immobilier_cost = 0

# Ajout du coût immobilier selon le type
if st.session_state.immobilier == "Achat":
    immobilier_cost = st.session_state.prix_achat
    frais_notaire = immobilier_cost * 0.08
    immobilier_cost += frais_notaire
elif st.session_state.immobilier == "Construction":
    # Terrain + construction
    immobilier_cost = st.session_state.prix_achat * 0.3  # Terrain = 30% du prix normal
    immobilier_cost += investment * 0.4  # Construction supplémentaire

# Fonds de roulement (3 mois de charges)
monthly_costs = get_monthly_costs(
    st.session_state.nb_terrains,
    st.session_state.type_terrain,
    st.session_state.has_bar,
    st.session_state.immobilier,
    st.session_state.surface_totale
)

if st.session_state.immobilier == "Location":
    monthly_costs += st.session_state.loyer_mensuel

fonds_roulement = monthly_costs * 3

total_investment = investment + immobilier_cost + fonds_roulement

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Aménagement & Équipements",
        f"{investment:,.0f}€",
        help="Terrains, bâtiments, équipements"
    )

with col2:
    st.metric(
        "Immobilier",
        f"{immobilier_cost:,.0f}€",
        help=f"{st.session_state.immobilier}" + (" (+ frais notaire)" if st.session_state.immobilier == "Achat" else "")
    )

with col3:
    st.metric(
        "Fonds de roulement",
        f"{fonds_roulement:,.0f}€",
        help="3 mois de trésorerie de sécurité"
    )

with col4:
    st.metric(
        "**TOTAL INVESTISSEMENT**",
        f"**{total_investment:,.0f}€**",
        help="Investissement total nécessaire"
    )

# Sauvegarde
st.session_state.total_investment = total_investment
st.session_state.monthly_costs = monthly_costs

# Plan de financement
st.markdown("---")
st.markdown("#### 💳 Plan de financement suggéré")

apport_perso = st.slider(
    "Apport personnel (%)",
    min_value=10,
    max_value=100,
    value=30,
    step=5
)

apport_montant = total_investment * (apport_perso / 100)
emprunt_montant = total_investment - apport_montant

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Apport personnel", f"{apport_montant:,.0f}€")

with col2:
    st.metric("Emprunt bancaire", f"{emprunt_montant:,.0f}€")

with col3:
    taux_interet = 4.5  # Taux moyen 2025
    duree_emprunt = 15  # ans
    mensualite_emprunt = (emprunt_montant * (taux_interet/100/12)) / (1 - (1 + taux_interet/100/12)**(-duree_emprunt*12)) if emprunt_montant > 0 else 0
    st.metric("Mensualité emprunt", f"{mensualite_emprunt:,.0f}€", help=f"Sur {duree_emprunt} ans à {taux_interet}%")

# Compte de résultat prévisionnel
st.markdown("---")
st.markdown("### 📈 Compte de Résultat Prévisionnel (3 ans)")

# Calcul des revenus par année
revenus_data = []
charges_data = []
resultats_data = []

for annee in [1, 2, 3]:
    taux_occup = st.session_state[f'occup_an{annee}']
    
    # Revenus
    rev_location = st.session_state.revenus_location * taux_occup
    rev_cours = st.session_state.revenus_cours_annuel * min(taux_occup * 1.2, 1)
    rev_tournois = st.session_state.revenus_tournois_annuel
    rev_bar = st.session_state.revenus_bar_annuel * taux_occup if st.session_state.has_bar else 0
    rev_proshop = st.session_state.revenus_proshop_annuel * taux_occup if st.session_state.has_proshop else 0
    
    total_revenus = rev_location + rev_cours + rev_tournois + rev_bar + rev_proshop
    
    # Charges
    charges_fixes_annuelles = monthly_costs * 12
    charges_mensualite = mensualite_emprunt * 12 if st.session_state.immobilier != "Location" else 0
    
    # Charges variables (proportionnelles à l'activité)
    charges_variables = total_revenus * 0.15  # 15% du CA (énergie supplémentaire, entretien, etc.)
    
    total_charges = charges_fixes_annuelles + charges_mensualite + charges_variables
    
    # Résultat
    resultat = total_revenus - total_charges
    
    revenus_data.append({
        'Année': f'An {annee}',
        'Location terrains': rev_location,
        'Cours': rev_cours,
        'Tournois': rev_tournois,
        'Bar': rev_bar,
        'Pro Shop': rev_proshop,
        'TOTAL': total_revenus
    })
    
    charges_data.append({
        'Année': f'An {annee}',
        'Charges fixes': charges_fixes_annuelles,
        'Remb. emprunt': charges_mensualite,
        'Charges variables': charges_variables,
        'TOTAL': total_charges
    })
    
    resultats_data.append({
        'Année': f'An {annee}',
        'Revenus': total_revenus,
        'Charges': total_charges,
        'Résultat': resultat,
        'Marge': (resultat / total_revenus * 100) if total_revenus > 0 else 0
    })

# Affichage tableau revenus
df_revenus = pd.DataFrame(revenus_data)
st.markdown("**Revenus annuels**")
st.dataframe(
    df_revenus.style.format("{:,.0f}€", subset=df_revenus.columns[1:]),
    use_container_width=True,
    hide_index=True
)

# Affichage tableau charges
df_charges = pd.DataFrame(charges_data)
st.markdown("**Charges annuelles**")
st.dataframe(
    df_charges.style.format("{:,.0f}€", subset=df_charges.columns[1:]),
    use_container_width=True,
    hide_index=True
)

# Affichage résultats
df_resultats = pd.DataFrame(resultats_data)
st.markdown("**Résultat net**")

col1, col2, col3 = st.columns(3)
for idx, row in df_resultats.iterrows():
    with [col1, col2, col3][idx]:
        color = "normal" if row['Résultat'] >= 0 else "inverse"
        st.metric(
            row['Année'],
            f"{row['Résultat']:,.0f}€",
            delta=f"{row['Marge']:.1f}%",
            delta_color=color
        )

# Graphiques
st.markdown("---")
st.markdown("### 📊 Visualisations")

col1, col2 = st.columns(2)

with col1:
    # Graphique évolution revenus vs charges
    fig_evolution = go.Figure()
    
    fig_evolution.add_trace(go.Bar(
        name='Revenus',
        x=df_resultats['Année'],
        y=df_resultats['Revenus'],
        marker_color='lightblue'
    ))
    
    fig_evolution.add_trace(go.Bar(
        name='Charges',
        x=df_resultats['Année'],
        y=df_resultats['Charges'],
        marker_color='lightcoral'
    ))
    
    fig_evolution.update_layout(
        title='Évolution Revenus vs Charges',
        xaxis_title='Année',
        yaxis_title='Euros (€)',
        barmode='group',
        height=400
    )
    
    st.plotly_chart(fig_evolution, use_container_width=True)

with col2:
    # Graphique répartition revenus An 3
    rev_an3 = revenus_data[2]
    labels = []
    values = []
    for key, value in rev_an3.items():
        if key != 'Année' and key != 'TOTAL' and value > 0:
            labels.append(key)
            values.append(value)
    
    fig_repartition = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=.3
    )])
    
    fig_repartition.update_layout(
        title='Répartition des revenus (Année 3)',
        height=400
    )
    
    st.plotly_chart(fig_repartition, use_container_width=True)

# Seuil de rentabilité
st.markdown("---")
st.markdown("### 🎯 Seuil de Rentabilité")

# Calcul du seuil
charges_fixes_mensuelles = charges_fixes_annuelles / 12 + (charges_mensualite / 12 if charges_mensualite > 0 else 0)
marge_variable = 0.85  # 85% de marge après charges variables

ca_seuil_mensuel = charges_fixes_mensuelles / marge_variable
ca_seuil_annuel = ca_seuil_mensuel * 12

# Taux d'occupation nécessaire
prix_moyen_heure = (st.session_state.prix_semaine * 0.65 + st.session_state.prix_weekend * 0.35)
heures_dispo_annuelles = (14 * 5 + 12 * 2) * 52 * st.session_state.nb_terrains  # Total heures disponibles

ca_max_location = heures_dispo_annuelles * prix_moyen_heure
taux_occup_seuil = (ca_seuil_annuel / ca_max_location) if ca_max_location > 0 else 0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CA seuil mensuel", f"{ca_seuil_mensuel:,.0f}€")

with col2:
    st.metric("CA seuil annuel", f"{ca_seuil_annuel:,.0f}€")

with col3:
    st.metric(
        "Taux occupation nécessaire",
        f"{taux_occup_seuil*100:.0f}%",
        help="Taux d'occupation minimum pour être rentable"
    )

if taux_occup_seuil < 0.50:
    st.success("✅ Seuil de rentabilité atteignable dès la première année")
elif taux_occup_seuil < 0.65:
    st.info("ℹ️ Seuil de rentabilité atteignable en année 2")
else:
    st.warning("⚠️ Seuil de rentabilité élevé - nécessite un très bon remplissage")

# Analyse de sensibilité
st.markdown("---")
st.markdown("### 🔍 Analyse de Sensibilité")

st.info("""
💡 **Impact d'une variation de ±10% sur les paramètres clés :**
""")

# Calcul de référence (an 2)
revenus_ref = resultats_data[1]['Revenus']
resultat_ref = resultats_data[1]['Résultat']

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Variation du prix moyen (-10%)**")
    impact_prix_down = resultat_ref - (revenus_ref * 0.10)
    st.metric("Résultat An 2", f"{impact_prix_down:,.0f}€", delta=f"{-revenus_ref*0.10:,.0f}€")

with col2:
    st.markdown("**Variation du prix moyen (+10%)**")
    impact_prix_up = resultat_ref + (revenus_ref * 0.10)
    st.metric("Résultat An 2", f"{impact_prix_up:,.0f}€", delta=f"+{revenus_ref*0.10:,.0f}€")

# Points clés et recommandations
st.markdown("---")
st.markdown("### 💡 Points Clés & Recommandations")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**✅ Points forts du projet**")
    points_forts = []
    
    if taux_occup_seuil < 0.50:
        points_forts.append("Seuil de rentabilité facilement atteignable")
    
    if st.session_state.has_bar:
        points_forts.append("Revenus diversifiés avec bar/restaurant")
    
    if resultats_data[2]['Marge'] > 15:
        points_forts.append(f"Bonne marge nette en année 3 ({resultats_data[2]['Marge']:.1f}%)")
    
    if st.session_state.get('propose_cours'):
        points_forts.append("Revenus complémentaires via cours")
    
    for point in points_forts:
        st.markdown(f"- {point}")

with col2:
    st.markdown("**⚠️ Points de vigilance**")
    points_vigilance = []
    
    if taux_occup_seuil > 0.60:
        points_vigilance.append("Seuil de rentabilité exigeant")
    
    if total_investment > 1000000:
        points_vigilance.append("Investissement initial important")
    
    if not st.session_state.has_bar and not st.session_state.has_proshop:
        points_vigilance.append("Revenus dépendants uniquement de la location")
    
    if resultats_data[0]['Résultat'] < 0:
        points_vigilance.append("Résultat négatif en année 1 (normal)")
    
    for point in points_vigilance:
        st.markdown(f"- {point}")

# Export
st.markdown("---")
st.markdown("### 📄 Export du Business Plan")

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("📥 Télécharger le Business Plan (PDF)", type="primary", use_container_width=True):
        st.info("🚧 Fonctionnalité d'export en cours de développement. Disponible prochainement !")
        st.markdown("""
        **Le PDF inclura :**
        - Récapitulatif du projet
        - Analyse de marché
        - Plan d'investissement
        - Compte de résultat 3 ans
        - Graphiques et indicateurs clés
        - Analyse de sensibilité
        """)

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("← Modèle économique", use_container_width=True):
        st.switch_page("pages/3_💰_Modele_Economique.py")

with col2:
    if st.button("🏠 Accueil", use_container_width=True):
        st.switch_page("app.py")

with col3:
    if st.button("🔄 Nouveau projet", use_container_width=True):
        # Reset session state
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.switch_page("app.py")
