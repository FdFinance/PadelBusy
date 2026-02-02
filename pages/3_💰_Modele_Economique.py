import streamlit as st
import sys
sys.path.append('/home/claude/padel-bp-generator')

st.set_page_config(page_title="Modèle Économique", page_icon="💰", layout="wide")

st.title("💰 Modèle Économique")
st.markdown("### Étape 3/4 : Définissez votre stratégie tarifaire et vos services")

# Vérification des étapes précédentes
if 'nb_terrains' not in st.session_state or 'city' not in st.session_state:
    st.warning("⚠️ Veuillez d'abord compléter les étapes précédentes")
    if st.button("← Retour"):
        st.switch_page("pages/1_📋_Configuration.py")
    st.stop()

# Stratégie tarifaire
st.markdown("#### 💵 Stratégie tarifaire")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Prix heure en semaine**")
    prix_semaine = st.number_input(
        "Prix/heure semaine (€)",
        min_value=20,
        max_value=80,
        value=st.session_state.get('prix_suggest_semaine', 35),
        step=1,
        help="Prix suggéré basé sur votre marché local"
    )
    st.session_state.prix_semaine = prix_semaine
    
    # Comparaison au marché
    diff_marche = prix_semaine - st.session_state.prix_suggest_semaine
    if diff_marche > 5:
        st.caption(f"🔴 +{diff_marche}€ vs marché (positionnement premium)")
    elif diff_marche < -5:
        st.caption(f"🟢 {diff_marche}€ vs marché (positionnement accessible)")
    else:
        st.caption(f"🟡 Aligné sur le marché")

with col2:
    st.markdown("**Prix heure en weekend**")
    prix_weekend = st.number_input(
        "Prix/heure weekend (€)",
        min_value=20,
        max_value=100,
        value=st.session_state.get('prix_suggest_weekend', 42),
        step=1,
        help="Généralement 15-20% plus élevé qu'en semaine"
    )
    st.session_state.prix_weekend = prix_weekend
    
    # Prime weekend
    prime = ((prix_weekend / prix_semaine) - 1) * 100
    st.caption(f"Prime weekend : +{prime:.0f}%")

# Créneaux à tarif réduit (off-peak)
st.markdown("---")
st.markdown("#### ⏰ Tarification heures creuses (optionnel)")

has_offpeak = st.checkbox(
    "Proposer des tarifs réduits pour les heures creuses",
    value=st.session_state.get('has_offpeak', False),
    help="Ex: 10h-14h en semaine à tarif réduit pour maximiser le remplissage"
)
st.session_state.has_offpeak = has_offpeak

if has_offpeak:
    col1, col2 = st.columns(2)
    with col1:
        prix_offpeak = st.number_input(
            "Prix heure creuse (€)",
            min_value=15,
            max_value=prix_semaine,
            value=int(prix_semaine * 0.75),
            step=1
        )
        st.session_state.prix_offpeak = prix_offpeak
        
    with col2:
        heures_offpeak = st.slider(
            "Heures creuses par semaine",
            min_value=10,
            max_value=40,
            value=20,
            help="Nombre d'heures par semaine à tarif réduit"
        )
        st.session_state.heures_offpeak = heures_offpeak

# Services complémentaires
st.markdown("---")
st.markdown("#### 🎾 Services complémentaires")

col1, col2 = st.columns(2)

prix_cours = 45  # Valeur par défaut
heures_cours_semaine = 20  # Valeur par défaut
revenu_moyen_tournoi = 800  # Valeur par défaut

with col1:
    st.markdown("**Cours de padel**")
    propose_cours = st.checkbox(
        "Proposer des cours particuliers/collectifs",
        value=True,
        help="Les cours génèrent des revenus complémentaires importants"
    )
    st.session_state.propose_cours = propose_cours
    
    if propose_cours:
        prix_cours = st.number_input(
            "Prix moyen cours (€/heure)",
            min_value=30,
            max_value=80,
            value=45,
            step=5
        )
        st.session_state.prix_cours = prix_cours
        
        heures_cours_semaine = st.slider(
            "Heures de cours par semaine",
            min_value=5,
            max_value=50,
            value=20,
            help="Nombre d'heures de cours dispensées par semaine"
        )
        st.session_state.heures_cours_semaine = heures_cours_semaine

with col2:
    st.markdown("**Tournois et événements**")
    nb_tournois_an = st.slider(
        "Nombre de tournois par an",
        min_value=0,
        max_value=24,
        value=12,
        help="Tournois amateurs, corporate, etc."
    )
    st.session_state.nb_tournois_an = nb_tournois_an
    
    if nb_tournois_an > 0:
        revenu_moyen_tournoi = st.number_input(
            "Revenu moyen par tournoi (€)",
            min_value=200,
            max_value=3000,
            value=800,
            step=100
        )
        st.session_state.revenu_moyen_tournoi = revenu_moyen_tournoi

# Estimation revenus annexes
st.markdown("---")
st.markdown("#### 🍹 Revenus annexes")

col1, col2 = st.columns(2)

revenu_bar_par_joueur = 4.5  # Valeur par défaut
ca_proshop_par_terrain = 3500  # Valeur par défaut
marge_proshop = 0.35  # Valeur par défaut

with col1:
    if st.session_state.has_bar:
        st.markdown("**Bar / Restaurant**")
        revenu_bar_par_joueur = st.number_input(
            "Revenu moyen par joueur (€)",
            min_value=2.0,
            max_value=15.0,
            value=4.5,
            step=0.5,
            help="Consommation moyenne par joueur (boissons, snacks)"
        )
        st.session_state.revenu_bar_par_joueur = revenu_bar_par_joueur
        
        st.caption("💡 Environ 80% des joueurs consomment au bar après leur partie")
    else:
        st.info("Vous n'avez pas sélectionné de bar dans la configuration")

with col2:
    if st.session_state.has_proshop:
        st.markdown("**Pro Shop**")
        ca_proshop_par_terrain = st.number_input(
            "CA annuel/terrain (€)",
            min_value=1000,
            max_value=10000,
            value=3500,
            step=500,
            help="Chiffre d'affaires annuel moyen par terrain"
        )
        st.session_state.ca_proshop_par_terrain = ca_proshop_par_terrain
        
        marge_proshop = st.slider(
            "Marge (%)",
            min_value=20,
            max_value=50,
            value=35,
            help="Marge commerciale sur les ventes"
        )
        st.session_state.marge_proshop = marge_proshop / 100
        marge_proshop = marge_proshop / 100
    else:
        st.info("Vous n'avez pas sélectionné de Pro Shop dans la configuration")

# Hypothèses d'occupation
st.markdown("---")
st.markdown("#### 📊 Hypothèses d'occupation")

st.info("""
💡 **Hypothèses par défaut basées sur les standards du marché :**
- Année 1 : 45% d'occupation (montée en charge)
- Année 2 : 60% d'occupation (croissance)
- Année 3 : 68% d'occupation (maturité)
""")

col1, col2, col3 = st.columns(3)

with col1:
    occup_an1_pct = st.slider(
        "Occupation Année 1 (%)",
        min_value=20,
        max_value=80,
        value=45,
        help="Taux d'occupation moyen la première année"
    )
    st.session_state.occup_an1 = occup_an1_pct / 100

with col2:
    occup_an2_pct = st.slider(
        "Occupation Année 2 (%)",
        min_value=30,
        max_value=90,
        value=60,
        help="Taux d'occupation moyen la deuxième année"
    )
    st.session_state.occup_an2 = occup_an2_pct / 100

with col3:
    occup_an3_pct = st.slider(
        "Occupation Année 3 (%)",
        min_value=40,
        max_value=95,
        value=68,
        help="Taux d'occupation moyen la troisième année"
    )
    st.session_state.occup_an3 = occup_an3_pct / 100

# Estimation rapide des revenus
st.markdown("---")
st.markdown("#### 💰 Estimation rapide des revenus annuels")

# Calcul simplifié
nb_terrains = st.session_state.nb_terrains
heures_ouverture_semaine = 14 * 5  # 14h/jour × 5 jours
heures_ouverture_weekend = 12 * 2  # 12h/jour × 2 jours
heures_total_semaine = heures_ouverture_semaine + heures_ouverture_weekend
heures_annuelles = heures_total_semaine * 52 * nb_terrains

# Revenus location terrains
revenus_location = (
    heures_ouverture_semaine * prix_semaine * 0.65 +  # 65% des heures en semaine
    heures_ouverture_weekend * prix_weekend * 0.35    # 35% des heures en weekend
) * 52 * nb_terrains

# Revenus cours
revenus_cours_annuel = 0
if propose_cours:
    revenus_cours_annuel = heures_cours_semaine * prix_cours * 52

# Revenus tournois
revenus_tournois_annuel = nb_tournois_an * revenu_moyen_tournoi if nb_tournois_an > 0 else 0

# Revenus bar
revenus_bar_annuel = 0
if st.session_state.has_bar:
    joueurs_annuels = (heures_annuelles / 1.5) * 4  # 4 joueurs par terrain, partie = 1.5h
    revenus_bar_annuel = joueurs_annuels * revenu_bar_par_joueur * 0.80  # 80% consomment

# Revenus proshop
revenus_proshop_annuel = 0
if st.session_state.has_proshop:
    revenus_proshop_annuel = ca_proshop_par_terrain * nb_terrains * marge_proshop

col1, col2, col3 = st.columns(3)

for idx, (annee, taux_pct, taux_decimal) in enumerate([
    (1, occup_an1_pct, st.session_state.occup_an1), 
    (2, occup_an2_pct, st.session_state.occup_an2), 
    (3, occup_an3_pct, st.session_state.occup_an3)
], 1):
    with [col1, col2, col3][idx-1]:
        rev_location = revenus_location * taux_decimal
        rev_cours = revenus_cours_annuel * min(taux_decimal * 1.2, 1)  # Cours montent plus vite
        rev_total = (rev_location + rev_cours + revenus_tournois_annuel + 
                    revenus_bar_annuel * taux_decimal + revenus_proshop_annuel * taux_decimal)
        
        st.metric(
            f"Année {annee}",
            f"{rev_total:,.0f}€",
            help=f"Estimation avec {taux_pct}% d'occupation"
        )
        
        st.caption(f"""
        - Location: {rev_location:,.0f}€
        - Cours: {rev_cours:,.0f}€
        - Autres: {revenus_tournois_annuel + revenus_bar_annuel * taux_decimal + revenus_proshop_annuel * taux_decimal:,.0f}€
        """)

# Sauvegarde pour la page suivante
st.session_state.revenus_location = revenus_location
st.session_state.revenus_cours_annuel = revenus_cours_annuel
st.session_state.revenus_tournois_annuel = revenus_tournois_annuel
st.session_state.revenus_bar_annuel = revenus_bar_annuel
st.session_state.revenus_proshop_annuel = revenus_proshop_annuel

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("← Localisation", use_container_width=True):
        st.switch_page("pages/2_📍_Localisation.py")

with col3:
    if st.button("➡️ Business Plan", type="primary", use_container_width=True):
        st.switch_page("pages/4_📊_Business_Plan.py")

# Sidebar résumé
with st.sidebar:
    st.markdown("### 💰 Résumé Économique")
    st.markdown(f"""
    **Tarifs :**
    - Semaine : {prix_semaine}€/h
    - Weekend : {prix_weekend}€/h
    
    **Services :**
    - {'✅' if propose_cours else '❌'} Cours ({heures_cours_semaine}h/sem)
    - Tournois : {nb_tournois_an}/an
    {'- ✅ Bar' if st.session_state.has_bar else ''}
    {'- ✅ Pro Shop' if st.session_state.has_proshop else ''}
    
    **Occupation :**
    - An 1 : {occup_an1_pct}%
    - An 2 : {occup_an2_pct}%
    - An 3 : {occup_an3_pct}%
    """)
