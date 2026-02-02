# 🎾 Générateur de Business Plan Padel - MVP

## Description

Application Streamlit permettant aux entrepreneurs de créer un business plan professionnel pour leur projet de club de padel en France.

L'outil guide l'utilisateur à travers 4 étapes :
1. **Configuration** : Définition du projet (nb terrains, services, immobilier)
2. **Localisation** : Choix de la ville avec données de marché enrichies
3. **Modèle Économique** : Stratégie tarifaire et services complémentaires
4. **Business Plan** : Projections financières sur 3 ans, visualisations, export

## Fonctionnalités MVP

✅ Configuration guidée du projet (terrains, bar, pro shop)  
✅ Données de marché pour 8 grandes villes françaises  
✅ Calculs automatiques d'investissement initial  
✅ Compte de résultat prévisionnel sur 3 ans  
✅ Analyse de sensibilité et seuil de rentabilité  
✅ Visualisations interactives (graphiques Plotly)  
✅ Interface intuitive multi-pages  

🚧 En développement :
- Export PDF du business plan
- Authentification utilisateur
- Sauvegarde multi-projets
- Intégration de vraies données via CSV

## Installation

### Prérequis
- Python 3.8 ou supérieur
- pip

### Étapes

1. **Cloner ou télécharger le projet**
```bash
cd padel-bp-generator
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt --break-system-packages
```

3. **Lancer l'application**
```bash
streamlit run app.py
```

4. **Ouvrir dans le navigateur**
L'application s'ouvre automatiquement à l'adresse : `http://localhost:8501`

## Structure du projet

```
padel-bp-generator/
├── app.py                          # Page d'accueil
├── pages/
│   ├── 1_📋_Configuration.py       # Étape 1 : Config projet
│   ├── 2_📍_Localisation.py        # Étape 2 : Choix ville + marché
│   ├── 3_💰_Modele_Economique.py   # Étape 3 : Pricing + services
│   └── 4_📊_Business_Plan.py       # Étape 4 : Résultats + visualisations
├── data/
│   └── market_data.py              # Données de marché mockées
├── requirements.txt
└── README.md
```

## Données actuelles

Le MVP utilise des données réalistes issues de recherches web pour 8 villes :
- Paris
- Lyon
- Marseille
- Toulouse
- Bordeaux
- Nantes
- Nice
- Strasbourg

### Données par ville
- Prix moyen heure (semaine/weekend)
- Nombre de clubs existants
- Taux d'occupation moyen
- Prix immobilier (location/achat au m²)
- Population du bassin (rayon 5km)
- Revenu moyen par ménage

## Intégration de vos vraies données

Pour remplacer les données mockées par vos vraies données :

### Format CSV recommandé

**market_data.csv**
```csv
ville,prix_semaine,prix_weekend,nb_clubs,population_5km,prix_m2_location,prix_m2_achat,taux_occupation,revenu_moyen
Paris,42,50,18,280000,320,9500,0.72,42000
Lyon,35,42,12,185000,180,4800,0.68,35000
...
```

### Modification du code

Dans `data/market_data.py`, remplacer le dictionnaire `MARKET_DATA` par :

```python
import pandas as pd

# Chargement depuis CSV
df_market = pd.read_csv('data/market_data.csv')

MARKET_DATA = {}
for _, row in df_market.iterrows():
    MARKET_DATA[row['ville']] = {
        'prix_moyen_heure_semaine': row['prix_semaine'],
        'prix_moyen_heure_weekend': row['prix_weekend'],
        'nb_clubs_existants': row['nb_clubs'],
        'population_bassin_5km': row['population_5km'],
        'prix_m2_location_mensuel': row['prix_m2_location'],
        'prix_m2_achat': row['prix_m2_achat'],
        'taux_occupation_moyen': row['taux_occupation'],
        'revenu_moyen_menage': row['revenu_moyen']
    }
```

## Utilisation

1. **Lancez l'application** : `streamlit run app.py`
2. **Suivez les 4 étapes** dans l'ordre
3. **Consultez votre business plan** avec projections et graphiques
4. **Ajustez les paramètres** pour tester différents scénarios

## Fonctionnalités clés

### Calculs automatiques
- Investissement initial selon type de terrains (indoor/outdoor/mixte)
- Coûts mensuels récurrents (charges fixes + variables)
- Revenus par source (location, cours, bar, pro shop, tournois)
- Seuil de rentabilité et taux d'occupation nécessaire

### Hypothèses modifiables
- Taux d'occupation par année (montée en charge)
- Stratégie tarifaire (semaine/weekend/heures creuses)
- Services complémentaires (cours, tournois, etc.)
- Plan de financement (apport personnel vs emprunt)

### Visualisations
- Évolution revenus vs charges sur 3 ans
- Répartition des sources de revenus
- Indicateurs clés (métriques, marges)

## Prochaines évolutions (post-MVP)

- Export PDF professionnel du business plan
- Authentification et comptes utilisateurs
- Sauvegarde et gestion multi-projets
- Scénarios comparatifs (optimiste/réaliste/pessimiste)
- Tableaux de trésorerie mensuels
- Intégration API pour données en temps réel
- Migration vers stack plus robuste (React + FastAPI)

## Support

Pour toute question ou suggestion : fred@padel-bp.fr

## Licence

Propriétaire - Tous droits réservés
