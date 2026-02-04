# Module de conseils personnalisés pour la création de club de padel
# Conseils basés sur les meilleures pratiques et l'expérience du marché français

CONSEILS_CONFIGURATION = {
    "nb_terrains": {
        "petit": {  # 2-3 terrains
            "avantages": [
                "Investissement initial réduit",
                "Gestion simplifiée",
                "Montée en charge progressive possible",
                "Idéal pour tester le marché"
            ],
            "inconvenients": [
                "Capacité d'accueil limitée aux heures de pointe",
                "Moins d'économies d'échelle",
                "Difficile d'organiser des tournois"
            ],
            "conseils": [
                "Privilégiez un emplacement à fort potentiel pour une extension future",
                "Maximisez le taux d'occupation avec des offres heures creuses",
                "Envisagez des partenariats avec des entreprises locales"
            ]
        },
        "moyen": {  # 4-6 terrains
            "avantages": [
                "Bon équilibre investissement/rentabilité",
                "Possibilité d'organiser des tournois",
                "Économies d'échelle sur les charges fixes",
                "Flexibilité pour différentes activités (cours, matchs, tournois)"
            ],
            "inconvenients": [
                "Investissement conséquent",
                "Nécessite une équipe de gestion"
            ],
            "conseils": [
                "Prévoyez 2 terrains indoor minimum pour une exploitation toute l'année",
                "Investissez dans un bon système de réservation en ligne",
                "Développez une communauté active de joueurs réguliers"
            ]
        },
        "grand": {  # 7+ terrains
            "avantages": [
                "Forte capacité d'accueil",
                "Positionnement premium possible",
                "Économies d'échelle importantes",
                "Attractivité pour les tournois régionaux"
            ],
            "inconvenients": [
                "Investissement très important",
                "Charges fixes élevées",
                "Nécessite un volume de clientèle important"
            ],
            "conseils": [
                "Étudiez attentivement la concurrence et la demande locale",
                "Prévoyez un plan marketing robuste dès l'ouverture",
                "Considérez des partenariats avec des fédérations ou sponsors"
            ]
        }
    },
    "type_terrain": {
        "Indoor": {
            "avantages": [
                "Exploitation 365 jours/an quelles que soient les conditions météo",
                "Confort optimal pour les joueurs",
                "Meilleur taux d'occupation sur l'année",
                "Possibilité de climatisation été/hiver"
            ],
            "inconvenients": [
                "Coût de construction 40-50% plus élevé",
                "Charges énergétiques plus importantes",
                "Surface au sol nécessaire plus importante (hauteur sous plafond)"
            ],
            "conseils": [
                "Indispensable dans le Nord et l'Est de la France",
                "Prévoir une hauteur minimum de 8m sous plafond",
                "Investir dans un bon système de ventilation/chauffage"
            ]
        },
        "Outdoor": {
            "avantages": [
                "Coût d'investissement réduit",
                "Charges d'exploitation plus faibles",
                "Ambiance conviviale en été",
                "Installation plus rapide"
            ],
            "inconvenients": [
                "Exploitation dépendante de la météo",
                "Saison réduite (avril-octobre dans la plupart des régions)",
                "Moins de créneaux rentables"
            ],
            "conseils": [
                "Recommandé uniquement dans le Sud (Nice, Marseille, Montpellier)",
                "Prévoir un éclairage de qualité pour les soirées d'été",
                "Installer des brumisateurs pour les journées chaudes"
            ]
        },
        "Mixte": {
            "avantages": [
                "Flexibilité maximale",
                "Exploitation indoor garantie toute l'année",
                "Terrains outdoor comme bonus en été",
                "Possibilité de différencier les tarifs"
            ],
            "inconvenients": [
                "Gestion plus complexe",
                "Double investissement (structure indoor + outdoor)"
            ],
            "conseils": [
                "Ratio idéal : 70% indoor / 30% outdoor",
                "Les terrains outdoor permettent des tarifs légèrement réduits",
                "Prévoir une transition facile entre les deux zones"
            ]
        }
    },
    "immobilier": {
        "Location": {
            "avantages": [
                "Pas d'immobilisation de capital dans l'immobilier",
                "Flexibilité en cas de besoin de déménagement",
                "Trésorerie préservée pour l'exploitation",
                "Charges prévisibles (loyer fixe)"
            ],
            "inconvenients": [
                "Pas de constitution de patrimoine",
                "Dépendance vis-à-vis du propriétaire",
                "Risque de non-renouvellement ou hausse de loyer"
            ],
            "conseils": [
                "Négociez un bail 3-6-9 avec clause de renouvellement prioritaire",
                "Prévoir une clause de cession de bail si revente",
                "Vérifiez les autorisations ERP (Établissement Recevant du Public)",
                "Faites inclure une période de franchise pendant les travaux"
            ]
        },
        "Achat": {
            "avantages": [
                "Constitution d'un patrimoine immobilier",
                "Stabilité à long terme",
                "Possibilité de plus-value",
                "Liberté totale d'aménagement"
            ],
            "inconvenients": [
                "Immobilisation importante de capitaux",
                "Frais de notaire (7-8%)",
                "Risque immobilier"
            ],
            "conseils": [
                "Privilégiez les zones en développement avec potentiel de valorisation",
                "Négociez le prix en fonction des travaux nécessaires",
                "Créez une SCI distincte pour l'immobilier (optimisation fiscale)",
                "Prévoyez les coûts de mise aux normes ERP"
            ]
        },
        "Construction": {
            "avantages": [
                "Bâtiment 100% adapté à l'activité padel",
                "Optimisation des espaces et flux",
                "Aucune contrainte de l'existant",
                "Image moderne et attractive"
            ],
            "inconvenients": [
                "Délais de construction longs (12-18 mois)",
                "Dépassements de budget fréquents",
                "Recherche de terrain complexe",
                "Démarches administratives (permis de construire)"
            ],
            "conseils": [
                "Prévoyez 20% de marge sur le budget construction",
                "Travaillez avec un architecte spécialisé sport",
                "Anticipez les délais administratifs (6-9 mois pour le permis)",
                "Vérifiez le PLU et les contraintes d'urbanisme"
            ]
        }
    }
}

CONSEILS_LOCALISATION = {
    "marche_mature": {  # taux occupation > 70%
        "analyse": "Marché mature avec forte demande. Les clubs existants sont saturés.",
        "opportunites": [
            "Clientèle déjà éduquée au padel",
            "Forte demande insatisfaite",
            "Prix du marché établis et soutenables"
        ],
        "risques": [
            "Concurrence active et réactive",
            "Emplacements premium déjà pris",
            "Coûts immobiliers potentiellement élevés"
        ],
        "conseils": [
            "Différenciez-vous par les services (bar premium, coaching, tournois)",
            "Ciblez une zone géographique mal desservie",
            "Investissez dans la qualité des installations",
            "Proposez des horaires étendus si la concurrence ferme tôt"
        ]
    },
    "marche_equilibre": {  # taux occupation 60-70%
        "analyse": "Marché équilibré avec de la place pour de nouveaux acteurs.",
        "opportunites": [
            "Croissance du marché encore possible",
            "Possibilité de se positionner stratégiquement",
            "Moins de pression sur les prix"
        ],
        "risques": [
            "Nécessité de créer de la demande",
            "Temps de montée en charge potentiellement long"
        ],
        "conseils": [
            "Investissez significativement dans le marketing local",
            "Proposez des offres d'initiation pour recruter de nouveaux joueurs",
            "Développez des partenariats avec clubs de tennis, entreprises",
            "Créez une communauté active (tournois hebdomadaires, ligues)"
        ]
    },
    "marche_emergent": {  # taux occupation < 60%
        "analyse": "Marché en développement. Le padel est encore peu connu localement.",
        "opportunites": [
            "Positionnement de pionnier",
            "Coûts immobiliers potentiellement plus bas",
            "Peu de concurrence directe"
        ],
        "risques": [
            "Éducation du marché nécessaire",
            "Temps de rentabilité plus long",
            "Demande incertaine"
        ],
        "conseils": [
            "Commencez avec un investissement prudent (3-4 terrains)",
            "Budget marketing conséquent pour faire connaître le padel",
            "Partenariats avec la presse locale et influenceurs",
            "Proposez des séances découverte gratuites",
            "Ciblez les anciens joueurs de tennis en priorité"
        ]
    }
}

CONSEILS_SERVICES = {
    "bar": {
        "pourquoi": [
            "70-80% des joueurs consomment après leur partie",
            "Améliore l'expérience globale et la fidélisation",
            "Revenu complémentaire à forte marge",
            "Crée un lieu de vie et de convivialité"
        ],
        "conseils": [
            "Licence IV recommandée pour l'alcool",
            "Privilégiez des produits à forte marge (café, boissons)",
            "Proposez des formules 'partie + consommation'",
            "Zone de 80-100m² idéale avec vue sur les terrains",
            "Prévoyez une terrasse si possible"
        ],
        "risques": [
            "Gestion RH supplémentaire (barman)",
            "Stock et approvisionnement à gérer",
            "Réglementation sanitaire stricte"
        ]
    },
    "proshop": {
        "pourquoi": [
            "Service attendu par les joueurs réguliers",
            "Marge de 30-40% sur les équipements",
            "Renforce l'image professionnelle du club",
            "Fidélisation (les joueurs reviennent pour renouveler leur matériel)"
        ],
        "conseils": [
            "Partenariats avec 2-3 marques maximum (négociation prix)",
            "Stock limité : raquettes best-sellers + accessoires",
            "Service de cordage = fidélisation",
            "Espace de 20-30m² suffisant",
            "Possibilité de test de raquettes avant achat"
        ],
        "risques": [
            "Stock immobilisé",
            "Concurrence du e-commerce",
            "Nécessite une expertise produit"
        ]
    },
    "cours": {
        "pourquoi": [
            "Revenu complémentaire significatif (40-60€/h)",
            "Fidélise les débutants qui deviennent joueurs réguliers",
            "Utilise les créneaux creux (journée semaine)",
            "Professionnalise l'image du club"
        ],
        "conseils": [
            "Un professeur diplômé minimum (DE ou DES padel)",
            "Proposez des cours collectifs (4-8 personnes) plus rentables",
            "Stages intensifs pendant les vacances scolaires",
            "Cours enfants le mercredi après-midi",
            "Programmes de progression (débutant, intermédiaire, avancé)"
        ],
        "modele_economique": {
            "cours_particulier": "45-60€/h",
            "cours_collectif_4": "15-20€/personne",
            "stage_semaine": "150-250€/personne"
        }
    },
    "tournois": {
        "pourquoi": [
            "Anime le club et crée de l'émulation",
            "Revenus directs (inscriptions) et indirects (bar, pro shop)",
            "Communication et visibilité",
            "Attire de nouveaux joueurs"
        ],
        "conseils": [
            "1-2 tournois par mois en rythme de croisière",
            "Variez les formats : P100, P250, tournois entreprises, mixtes",
            "Prévoyez des lots attractifs (partenariats équipementiers)",
            "Système de classement interne pour fidéliser",
            "Tournois after-work le jeudi soir"
        ],
        "revenus_moyens": {
            "tournoi_amateur_32_equipes": "800-1200€ net",
            "tournoi_entreprise": "1500-3000€ net",
            "tournoi_homologue_FFT": "1000-2000€ net"
        }
    }
}

CONSEILS_PRICING = {
    "positionnement_premium": {
        "definition": "Prix 15-20% au-dessus du marché",
        "quand": [
            "Installations haut de gamme",
            "Services différenciants (spa, restaurant gastronomique)",
            "Zone à fort pouvoir d'achat",
            "Peu de concurrence directe"
        ],
        "conseils": [
            "La qualité doit être irréprochable pour justifier le prix",
            "Proposez des abonnements premium avec avantages exclusifs",
            "Service client exemplaire",
            "Terrains toujours en parfait état"
        ]
    },
    "positionnement_marche": {
        "definition": "Prix alignés sur la moyenne du marché",
        "quand": [
            "Installations standards de qualité",
            "Concurrence établie",
            "Cible large (particuliers et entreprises)"
        ],
        "conseils": [
            "Différenciez-vous par les services, pas par le prix",
            "Fidélisez avec des cartes d'abonnement",
            "Offres spéciales heures creuses pour optimiser le remplissage"
        ]
    },
    "positionnement_accessible": {
        "definition": "Prix 10-15% en dessous du marché",
        "quand": [
            "Nouveau sur le marché et besoin de volume",
            "Zone à pouvoir d'achat moyen",
            "Objectif de démocratisation du padel"
        ],
        "conseils": [
            "Compensez par un volume important",
            "Attention aux charges fixes qui restent constantes",
            "Prévoyez une hausse progressive des prix sur 2-3 ans"
        ]
    },
    "heures_creuses": {
        "definition": "Tarifs réduits pour les créneaux peu demandés",
        "creneaux_types": [
            "10h-14h en semaine",
            "Lundi toute la journée",
            "Dimanche soir"
        ],
        "reduction_recommandee": "20-30% de réduction",
        "conseils": [
            "Ciblez les retraités, étudiants, travailleurs en horaires décalés",
            "Proposez des formules matinales + café offert",
            "Partenariats avec entreprises pour leurs séminaires"
        ]
    }
}

CONSEILS_FINANCEMENT = {
    "apport_personnel": {
        "minimum_recommande": "25-30% de l'investissement total",
        "pourquoi": [
            "Condition nécessaire pour obtenir un prêt bancaire",
            "Démontre votre engagement dans le projet",
            "Réduit le risque financier global"
        ],
        "conseils": [
            "En dessous de 20%, très difficile d'obtenir un financement",
            "Les banques apprécient 30%+ d'apport",
            "Possibilité d'apport en nature (local, matériel)"
        ]
    },
    "pret_bancaire": {
        "duree_recommandee": "10-15 ans pour l'immobilier, 5-7 ans pour l'équipement",
        "taux_actuels": "4-5.5% (2025)",
        "conseils": [
            "Consultez plusieurs banques (BPI France en plus des banques classiques)",
            "Présentez un business plan solide et réaliste",
            "Prévoyez des garanties (caution personnelle, nantissement)",
            "Négociez un différé de remboursement de 6-12 mois"
        ]
    },
    "aides_et_subventions": {
        "types": [
            "Prêt d'honneur (0% via Initiative France ou Réseau Entreprendre)",
            "BPI France : garantie prêt bancaire jusqu'à 70%",
            "Aides régionales au développement sportif",
            "FEDER pour les zones rurales",
            "Aides CNDS pour les clubs associatifs"
        ],
        "conseils": [
            "Renseignez-vous auprès de la CCI locale",
            "Le prêt d'honneur peut servir d'apport complémentaire",
            "Certaines régions ont des dispositifs spécifiques sport"
        ]
    }
}

CONSEILS_JURIDIQUE = {
    "statuts_recommandes": {
        "SARL": {
            "avantages": ["Responsabilité limitée", "Adapté aux projets familiaux", "Fiscalité IR possible les premières années"],
            "inconvenients": ["Moins flexible pour les investisseurs"]
        },
        "SAS": {
            "avantages": ["Flexibilité statutaire", "Attractif pour les investisseurs", "Président assimilé salarié"],
            "inconvenients": ["Coût social plus élevé pour le dirigeant"]
        }
    },
    "reglementations": [
        "Déclaration ERP (Établissement Recevant du Public) obligatoire",
        "Affiliation FFT recommandée pour les tournois homologués",
        "Assurance RC professionnelle obligatoire",
        "Respect des normes d'accessibilité PMR",
        "Déclaration CNIL pour les fichiers clients"
    ],
    "conseils": [
        "Faites-vous accompagner par un expert-comptable dès le départ",
        "Consultez un avocat pour les baux commerciaux",
        "Séparez l'immobilier (SCI) de l'exploitation (SAS/SARL)"
    ]
}

CONSEILS_MARKETING = {
    "avant_ouverture": [
        "Créez une page Instagram/Facebook 3-4 mois avant l'ouverture",
        "Teasing avec photos des travaux",
        "Partenariats avec des joueurs locaux influents",
        "Relations presse locale",
        "Pré-inscriptions avec offre early-bird"
    ],
    "lancement": [
        "Inauguration avec personnalité locale (sportif, élu)",
        "Week-end portes ouvertes avec initiations gratuites",
        "Offre de lancement (premier match offert)",
        "Partenariat influenceurs locaux"
    ],
    "recurrent": [
        "Newsletter mensuelle aux membres",
        "Tournois réguliers pour animer la communauté",
        "Programme de parrainage (offre pour le parrain et le filleul)",
        "Présence sur les apps de réservation (PadelShot, etc.)",
        "Google My Business optimisé"
    ],
    "budget_recommande": "5-10% du CA la première année, 3-5% ensuite"
}

CONSEILS_EXPLOITATION = {
    "personnel": {
        "equipe_type_4_terrains": [
            "1 gérant/manager (vous ou salarié)",
            "1 agent d'accueil (temps plein)",
            "1 agent d'entretien (mi-temps)",
            "1-2 professeurs (vacataires)"
        ],
        "conseils": [
            "Recrutez des passionnés de padel",
            "Formez votre équipe au service client",
            "Prévoyez des plannings flexibles (activité en soirée et weekend)"
        ]
    },
    "horaires": {
        "semaine": "8h-23h (14-15h d'ouverture)",
        "weekend": "9h-21h (12h d'ouverture)",
        "conseils": [
            "Les créneaux 18h-21h en semaine sont les plus demandés",
            "Le dimanche matin est excellent pour les familles",
            "Envisagez une ouverture plus tard le lundi (jour creux)"
        ]
    },
    "maintenance": {
        "quotidien": ["Nettoyage terrains", "Vérification éclairage", "Arrosage gazon synthétique"],
        "hebdomadaire": ["Nettoyage vestiaires en profondeur", "Vérification vitres et filets"],
        "annuel": ["Regarnissage gazon synthétique", "Révision éclairage", "Peinture et rafraîchissement"],
        "budget": "3-5% du CA annuel"
    }
}

def get_conseil_terrains(nb_terrains):
    """Retourne les conseils basés sur le nombre de terrains"""
    if nb_terrains <= 3:
        return CONSEILS_CONFIGURATION["nb_terrains"]["petit"]
    elif nb_terrains <= 6:
        return CONSEILS_CONFIGURATION["nb_terrains"]["moyen"]
    else:
        return CONSEILS_CONFIGURATION["nb_terrains"]["grand"]

def get_conseil_marche(taux_occupation):
    """Retourne les conseils basés sur le taux d'occupation du marché"""
    if taux_occupation >= 0.70:
        return CONSEILS_LOCALISATION["marche_mature"]
    elif taux_occupation >= 0.60:
        return CONSEILS_LOCALISATION["marche_equilibre"]
    else:
        return CONSEILS_LOCALISATION["marche_emergent"]

def get_conseil_type_terrain(type_terrain):
    """Retourne les conseils pour le type de terrain"""
    return CONSEILS_CONFIGURATION["type_terrain"].get(type_terrain, {})

def get_conseil_immobilier(type_immobilier):
    """Retourne les conseils pour le type d'immobilier"""
    return CONSEILS_CONFIGURATION["immobilier"].get(type_immobilier, {})

def get_conseil_service(service):
    """Retourne les conseils pour un service donné"""
    return CONSEILS_SERVICES.get(service, {})

def get_conseils_personnalises(config):
    """
    Génère des conseils personnalisés complets basés sur la configuration du projet

    Args:
        config: dict avec les clés:
            - nb_terrains: int
            - type_terrain: str ("Indoor", "Outdoor", "Mixte")
            - immobilier: str ("Location", "Achat", "Construction")
            - has_bar: bool
            - has_proshop: bool
            - city: str
            - taux_occupation_marche: float
            - investment_total: float

    Returns:
        dict avec les conseils organisés par catégorie
    """
    conseils = {
        "prioritaires": [],
        "configuration": {},
        "marche": {},
        "financement": [],
        "exploitation": [],
        "marketing": []
    }

    # Conseils prioritaires basés sur le profil
    nb_terrains = config.get("nb_terrains", 4)
    investment = config.get("investment_total", 0)
    taux_occupation = config.get("taux_occupation_marche", 0.65)

    # Conseil 1: Taille du projet
    if nb_terrains <= 3 and investment > 400000:
        conseils["prioritaires"].append({
            "type": "attention",
            "titre": "Investissement élevé pour peu de terrains",
            "message": "Votre investissement par terrain est élevé. Vérifiez si vous pouvez optimiser les coûts ou ajouter des terrains pour améliorer la rentabilité."
        })

    # Conseil 2: Marché
    if taux_occupation < 0.60:
        conseils["prioritaires"].append({
            "type": "attention",
            "titre": "Marché encore jeune",
            "message": "Le marché local est en développement. Prévoyez un budget marketing conséquent et une montée en charge progressive."
        })
    elif taux_occupation >= 0.70:
        conseils["prioritaires"].append({
            "type": "opportunite",
            "titre": "Forte demande locale",
            "message": "Le marché est dynamique avec une forte demande. C'est le bon moment pour vous lancer si vous trouvez un bon emplacement."
        })

    # Conseil 3: Services
    if not config.get("has_bar", False):
        conseils["prioritaires"].append({
            "type": "suggestion",
            "titre": "Bar/Restaurant recommandé",
            "message": "70-80% des joueurs consomment après leur partie. Un bar améliore significativement la rentabilité et l'expérience client."
        })

    # Conseils configuration
    conseils["configuration"] = {
        "terrains": get_conseil_terrains(nb_terrains),
        "type": get_conseil_type_terrain(config.get("type_terrain", "Indoor")),
        "immobilier": get_conseil_immobilier(config.get("immobilier", "Location"))
    }

    # Conseils marché
    conseils["marche"] = get_conseil_marche(taux_occupation)

    # Conseils financement
    if investment > 500000:
        conseils["financement"].append("Projet important : consultez BPI France pour une garantie de prêt")
        conseils["financement"].append("Envisagez un prêt d'honneur pour compléter votre apport")

    conseils["financement"].append("Négociez un différé de remboursement de 6-12 mois")
    conseils["financement"].append("Prévoyez 3 mois de trésorerie de sécurité minimum")

    # Conseils exploitation
    conseils["exploitation"] = CONSEILS_EXPLOITATION["personnel"]["conseils"]

    # Conseils marketing
    conseils["marketing"] = CONSEILS_MARKETING["avant_ouverture"][:3]

    return conseils
