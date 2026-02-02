# Données de marché pour les principales villes françaises
# Sources : recherches web sur le marché du padel en France (2024-2025)

MARKET_DATA = {
    "Paris": {
        "prix_moyen_heure_semaine": 42,
        "prix_moyen_heure_weekend": 50,
        "nb_clubs_existants": 18,
        "population_bassin_5km": 280000,
        "prix_m2_location_mensuel": 320,
        "prix_m2_achat": 9500,
        "taux_occupation_moyen": 0.72,
        "revenu_moyen_menage": 42000,
        "clubs_premium": ["Padel Club Paris", "4Padel Paris", "Greenweez Paris Premier Padel"]
    },
    "Lyon": {
        "prix_moyen_heure_semaine": 35,
        "prix_moyen_heure_weekend": 42,
        "nb_clubs_existants": 12,
        "population_bassin_5km": 185000,
        "prix_m2_location_mensuel": 180,
        "prix_m2_achat": 4800,
        "taux_occupation_moyen": 0.68,
        "revenu_moyen_menage": 35000,
        "clubs_premium": ["Padel Club Lyon", "Lyon Padel Club"]
    },
    "Marseille": {
        "prix_moyen_heure_semaine": 32,
        "prix_moyen_heure_weekend": 38,
        "nb_clubs_existants": 10,
        "population_bassin_5km": 195000,
        "prix_m2_location_mensuel": 150,
        "prix_m2_achat": 3800,
        "taux_occupation_moyen": 0.65,
        "revenu_moyen_menage": 28000,
        "clubs_premium": ["Marseille Padel Club", "4Padel Marseille"]
    },
    "Toulouse": {
        "prix_moyen_heure_semaine": 33,
        "prix_moyen_heure_weekend": 40,
        "nb_clubs_existants": 9,
        "population_bassin_5km": 165000,
        "prix_m2_location_mensuel": 145,
        "prix_m2_achat": 3500,
        "taux_occupation_moyen": 0.66,
        "revenu_moyen_menage": 31000,
        "clubs_premium": ["Toulouse Padel Club", "T Padel"]
    },
    "Bordeaux": {
        "prix_moyen_heure_semaine": 34,
        "prix_moyen_heure_weekend": 41,
        "nb_clubs_existants": 8,
        "population_bassin_5km": 145000,
        "prix_m2_location_mensuel": 165,
        "prix_m2_achat": 4200,
        "taux_occupation_moyen": 0.67,
        "revenu_moyen_menage": 33000,
        "clubs_premium": ["Bordeaux Padel Club", "Padel Bordeaux Lac"]
    },
    "Nantes": {
        "prix_moyen_heure_semaine": 32,
        "prix_moyen_heure_weekend": 39,
        "nb_clubs_existants": 7,
        "population_bassin_5km": 138000,
        "prix_m2_location_mensuel": 155,
        "prix_m2_achat": 3900,
        "taux_occupation_moyen": 0.64,
        "revenu_moyen_menage": 30000,
        "clubs_premium": ["Nantes Padel Club", "We Padel Nantes"]
    },
    "Nice": {
        "prix_moyen_heure_semaine": 36,
        "prix_moyen_heure_weekend": 44,
        "nb_clubs_existants": 9,
        "population_bassin_5km": 155000,
        "prix_m2_location_mensuel": 220,
        "prix_m2_achat": 5500,
        "taux_occupation_moyen": 0.70,
        "revenu_moyen_menage": 34000,
        "clubs_premium": ["Nice Padel Club", "Padel Riviera"]
    },
    "Strasbourg": {
        "prix_moyen_heure_semaine": 31,
        "prix_moyen_heure_weekend": 38,
        "nb_clubs_existants": 5,
        "population_bassin_5km": 125000,
        "prix_m2_location_mensuel": 140,
        "prix_m2_achat": 3400,
        "taux_occupation_moyen": 0.62,
        "revenu_moyen_menage": 29000,
        "clubs_premium": ["Strasbourg Padel Club"]
    }
}

# Templates de coûts d'investissement initial
INVESTMENT_COSTS = {
    "terrain_outdoor": {
        "construction": 35000,  # par terrain
        "eclairage": 12000,
        "clotures_filets": 8000,
        "sol_gazon_synthetique": 6000
    },
    "terrain_indoor": {
        "construction": 55000,  # par terrain (+ structure)
        "eclairage": 15000,
        "clotures_filets": 8000,
        "sol_gazon_synthetique": 6000,
        "chauffage_ventilation": 18000
    },
    "batiment": {
        "vestiaires_douches": 45000,
        "accueil_reception": 25000,
        "bar_restaurant_100m2": 80000,
        "bar_restaurant_50m2": 45000,
        "proshop_30m2": 15000,
        "stockage": 8000
    },
    "equipements": {
        "mobilier_accueil": 8000,
        "systeme_reservation": 5000,
        "materiel_entretien": 3000,
        "raquettes_balles_location": 4000,
        "videosurveillance": 6000
    },
    "travaux": {
        "cle_en_main": 1.0,  # multiplicateur
        "travaux_legers": 1.15,
        "travaux_lourds": 1.35
    }
}

# Coûts récurrents mensuels
RECURRING_COSTS = {
    "fixe": {
        "assurances": 800,  # par mois base 4 terrains
        "internet_telephonie": 150,
        "comptabilite": 300,
        "licences_logiciels": 200,
        "marketing_communication": 500,
        "entretien_maintenance": 600
    },
    "par_terrain": {
        "energie_outdoor": 150,  # par terrain par mois
        "energie_indoor": 350,
        "assurance_supplementaire": 80
    },
    "bar": {
        "salaire_barman_partiel": 1800,
        "achats_consommations": 1200,
        "licences": 150
    },
    "personnel": {
        "manager": 3200,
        "accueil_reception": 1900,
        "entretien": 1600,
        "prof_padel_vacataire": 35  # par heure
    }
}

# Hypothèses de revenus
REVENUE_ASSUMPTIONS = {
    "taux_occupation": {
        "annee_1": 0.45,  # 45% la première année
        "annee_2": 0.60,  # 60% la deuxième
        "annee_3": 0.68   # 68% la troisième
    },
    "heures_ouverture": {
        "semaine_jour": 14,  # 8h-22h
        "weekend_jour": 12   # 9h-21h
    },
    "repartition_creneaux": {
        "semaine": 0.65,
        "weekend": 0.35
    },
    "bar_revenu_par_joueur": 4.5,  # revenu moyen bar par joueur
    "cours_prix_moyen": 45,  # prix moyen cours particulier
    "cours_heures_semaine": 20,  # heures de cours par semaine
    "tournois_par_an": 12,
    "revenu_moyen_tournoi": 800,
    "proshop_marge": 0.35,
    "proshop_ca_annuel_par_terrain": 3500
}

def get_city_data(city_name):
    """Retourne les données d'une ville"""
    return MARKET_DATA.get(city_name, None)

def get_all_cities():
    """Retourne la liste de toutes les villes disponibles"""
    return sorted(list(MARKET_DATA.keys()))

def get_investment_cost(type_terrain, nb_terrains, has_bar, has_proshop, bar_size, travaux_type):
    """Calcule l'investissement initial total"""
    
    total = 0
    
    # Coûts des terrains
    if type_terrain == "Indoor":
        terrain_cost = INVESTMENT_COSTS["terrain_indoor"]
    elif type_terrain == "Outdoor":
        terrain_cost = INVESTMENT_COSTS["terrain_outdoor"]
    else:  # Mixte
        # On suppose 50/50
        terrain_cost_indoor = INVESTMENT_COSTS["terrain_indoor"]
        terrain_cost_outdoor = INVESTMENT_COSTS["terrain_outdoor"]
        terrain_cost = {k: (terrain_cost_indoor[k] + terrain_cost_outdoor[k]) / 2 
                       for k in terrain_cost_indoor.keys()}
    
    for key, value in terrain_cost.items():
        total += value * nb_terrains
    
    # Bâtiments de base
    total += INVESTMENT_COSTS["batiment"]["vestiaires_douches"]
    total += INVESTMENT_COSTS["batiment"]["accueil_reception"]
    total += INVESTMENT_COSTS["batiment"]["stockage"]
    
    # Bar
    if has_bar:
        if bar_size == "50m²":
            total += INVESTMENT_COSTS["batiment"]["bar_restaurant_50m2"]
        else:
            total += INVESTMENT_COSTS["batiment"]["bar_restaurant_100m2"]
    
    # Pro shop
    if has_proshop:
        total += INVESTMENT_COSTS["batiment"]["proshop_30m2"]
    
    # Équipements
    for key, value in INVESTMENT_COSTS["equipements"].items():
        total += value
    
    # Multiplicateur travaux - normalisation pour gérer les accents
    travaux_key = travaux_type.lower().replace(" ", "_").replace("é", "e")
    travaux_mult = INVESTMENT_COSTS["travaux"][travaux_key]
    total *= travaux_mult
    
    return round(total, -3)  # Arrondi au millier

def get_monthly_costs(nb_terrains, type_terrain, has_bar, immobilier, surface_totale):
    """Calcule les coûts mensuels récurrents"""
    
    total = 0
    
    # Coûts fixes
    for key, value in RECURRING_COSTS["fixe"].items():
        total += value
    
    # Coûts par terrain
    if type_terrain == "Indoor":
        total += RECURRING_COSTS["par_terrain"]["energie_indoor"] * nb_terrains
    elif type_terrain == "Outdoor":
        total += RECURRING_COSTS["par_terrain"]["energie_outdoor"] * nb_terrains
    else:  # Mixte
        total += (RECURRING_COSTS["par_terrain"]["energie_indoor"] + 
                 RECURRING_COSTS["par_terrain"]["energie_outdoor"]) / 2 * nb_terrains
    
    total += RECURRING_COSTS["par_terrain"]["assurance_supplementaire"] * nb_terrains
    
    # Bar
    if has_bar:
        for key, value in RECURRING_COSTS["bar"].items():
            total += value
    
    # Personnel de base
    total += RECURRING_COSTS["personnel"]["manager"]
    total += RECURRING_COSTS["personnel"]["accueil_reception"]
    total += RECURRING_COSTS["personnel"]["entretien"]
    
    # Loyer ou crédit (simplifié pour le MVP)
    # On ne l'ajoute pas ici, sera calculé séparément
    
    return round(total, -2)  # Arrondi à la centaine
