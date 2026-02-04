import streamlit as st
from datetime import datetime
import hashlib

# Configuration de la page
st.set_page_config(
    page_title="Padel Business Plan Generator",
    page_icon="🎾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════
# SYSTÈME D'AUTHENTIFICATION
# ═══════════════════════════════════════════════════════════════════

# Mot de passe (changez-le ici)
# Pour plus de sécurité, utilisez un hash
CORRECT_PASSWORD = "PdBP022026"  # ← CHANGEZ CE MOT DE PASSE

def hash_password(password):
    """Hash le mot de passe pour plus de sécurité"""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password():
    """Retourne True si l'utilisateur a entré le bon mot de passe"""
    
    # Vérifier si déjà authentifié
    if st.session_state.get('authenticated', False):
        return True
    
    # Afficher l'écran de connexion
    st.markdown("""
    <div style='text-align: center; padding: 50px;'>
        <h1>🎾 Générateur de Business Plan Padel</h1>
        <h3>Authentification requise</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        password = st.text_input(
            "Mot de passe",
            type="password",
            key="password_input"
        )
        
        col_a, col_b, col_c = st.columns([1, 1, 1])
        with col_b:
            if st.button("Se connecter", type="primary", use_container_width=True):
                if password == CORRECT_PASSWORD:
                    st.session_state.authenticated = True
                    st.success("✅ Connexion réussie !")
                    st.rerun()
                else:
                    st.error("❌ Mot de passe incorrect")
        
        st.markdown("---")
        st.caption("💡 Application sécurisée - Accès réservé")
    
    return False

# Vérifier l'authentification
if not check_password():
    st.stop()

# ═══════════════════════════════════════════════════════════════════
# APPLICATION PRINCIPALE (après authentification)
# ═══════════════════════════════════════════════════════════════════

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
5. 💡 Conseils personnalisés
""")

# Page d'accueil
st.markdown("""
## Bienvenue sur votre assistant de business plan

Cet outil vous permet de créer un business plan professionnel pour votre projet de club de padel en France.

### Comment ca marche ?

1. **Configurez votre projet** : nombre de terrains, services, type d'immobilier
2. **Choisissez votre localisation** : nous enrichissons avec des données du marché local
3. **Définissez votre modèle économique** : pricing, services complémentaires
4. **Obtenez votre business plan** : projections financières sur 3 ans, graphiques
5. **Recevez des conseils personnalisés** : recommandations adaptées à votre projet

### Pourquoi utiliser cet outil ?

✅ **Données du marché réel** : prix, taux d'occupation, benchmarks par ville
✅ **Calculs automatiques** : investissement, compte de résultat, seuil de rentabilité
✅ **Conseils personnalisés** : recommandations basées sur votre configuration
✅ **Guide complet** : financement, juridique, marketing, exploitation

---

👉 **Commencez par la page "📋 Configuration" dans le menu de gauche**
""")

# Informations de contact
st.sidebar.markdown("---")

# Bouton de déconnexion
if st.sidebar.button("🔓 Se déconnecter"):
    st.session_state.authenticated = False
    st.rerun()

st.sidebar.markdown("**Besoin d'aide ?**")
st.sidebar.markdown("contact@padel-bp.fr")
st.sidebar.markdown(f"*Version MVP - {datetime.now().year}*")
