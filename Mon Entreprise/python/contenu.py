"""
CONTENU DU SITE — Baraza All Services
=====================================

C'est le SEUL fichier à modifier pour changer les textes, les prix,
les coordonnées et les moyens de paiement.

Après modification, régénérez le site :
    python python/construire_site.py

Règles d'écriture :
  - [[texte]]  -> texte mis en couleur (dégradé) dans les titres
  - chaque texte existe en français ("fr") et en anglais ("en")
  - les prix sont en dollars américains (USD), sans symbole
"""

# --------------------------------------------------------------------------
# 1. ENTREPRISE ET CONTACT
# --------------------------------------------------------------------------
ENTREPRISE = {
    "nom": "Baraza All Services",
    "initiales": "BA",
    "email": "contact@example.com",           # <- votre email
    "telephone": "+27 00 000 0000",            # <- numéro affiché
    "whatsapp": "27000000000",                 # <- WhatsApp : indicatif + numéro, sans + ni espaces
    "site_url": "https://baraza-all-services.netlify.app/",  # <- adresse du site une fois en ligne
    # Nom officiel et numéro CIPC (ex. "Baraza All Services (Pty) Ltd", "2026/123456/07").
    # Laisse "numero_enregistrement" vide si l'entreprise n'est pas encore enregistrée.
    "raison_sociale": "Baraza All Services",
    "numero_enregistrement": "",
    # Adresse affichée dans le pied de page (une ligne par élément). Liste vide [] = pas d'adresse affichée.
    "adresse": ["À COMPLÉTER (rue)", "Ville, Province", "Code postal", "South Africa"],
    # Réseaux sociaux : colle l'adresse de ta page. Vide = icône non affichée.
    "reseaux": {
        "facebook": "",    # ex. https://www.facebook.com/BarazaAllServices
        "linkedin": "",    # ex. https://www.linkedin.com/company/baraza-all-services
        "instagram": "",   # ex. https://www.instagram.com/barazaallservices
        "tiktok": "",      # ex. https://www.tiktok.com/@barazaallservices
    },
}

# --------------------------------------------------------------------------
# 2. DEVISES
# Les prix sont fixés en USD. Le visiteur peut afficher l'équivalent
# approximatif dans sa devise (taux mis à jour automatiquement en ligne ;
# les taux ci-dessous servent de secours si le service est indisponible).
# --------------------------------------------------------------------------
DEVISE_BASE = "USD"
DEVISES = [
    # code, nom FR, nom EN, taux de secours (1 USD = ...)
    ("USD", "Dollar américain", "US dollar", 1),
    ("ZAR", "Rand sud-africain", "South African rand", 18.2),
    ("EUR", "Euro", "Euro", 0.92),
    ("GBP", "Livre sterling", "British pound", 0.79),
    ("CDF", "Franc congolais", "Congolese franc", 2850),
    ("XAF", "Franc CFA (CEMAC)", "Central African CFA franc", 605),
    ("XOF", "Franc CFA (UEMOA)", "West African CFA franc", 605),
    ("KES", "Shilling kényan", "Kenyan shilling", 129),
    ("TZS", "Shilling tanzanien", "Tanzanian shilling", 2600),
    ("UGX", "Shilling ougandais", "Ugandan shilling", 3700),
    ("RWF", "Franc rwandais", "Rwandan franc", 1400),
    ("BIF", "Franc burundais", "Burundian franc", 2950),
    ("NGN", "Naira nigérian", "Nigerian naira", 1550),
    ("ZMW", "Kwacha zambien", "Zambian kwacha", 26),
    ("BWP", "Pula botswanais", "Botswana pula", 13.6),
    ("AOA", "Kwanza angolais", "Angolan kwanza", 910),
    ("CAD", "Dollar canadien", "Canadian dollar", 1.37),
    ("CHF", "Franc suisse", "Swiss franc", 0.88),
]

# --------------------------------------------------------------------------
# 3. PAIEMENT — tout arrive sur le compte FNB
# Liens de paiement : créez-les chez le prestataire (voir docs/PAIEMENTS.md)
# puis collez-les ici. Tant qu'un lien est vide, le bouton ouvre WhatsApp.
# --------------------------------------------------------------------------
LIENS_PAIEMENT = {
    "carte": "",    # <- lien de paiement Yoco (yoco.com > Payment Links), ex. https://pay.yoco.com/...
    "paypal": "",   # facultatif : ex. https://paypal.me/VotreNom (le bouton n'apparaît que si rempli)
    "wise": "",     # facultatif : ex. https://wise.com/pay/me/votrenom (le bouton n'apparaît que si rempli)
}

COMPTE_FNB = {
    "banque": "First National Bank (FNB), South Africa",
    "titulaire": "Baraza All Services",
    "numero": "À COMPLÉTER",          # <- numéro de compte FNB
    "shapid": "À COMPLÉTER",          # <- ton ShapID PayShap (app FNB > PayShap > ShapID), en général ton numéro de téléphone
    "type": "Business Cheque Account",
    "code_agence": "250655",          # code universel FNB (vérifiez dans votre app FNB)
    "swift": "FIRNZAJJ",              # SWIFT/BIC FNB (confirmez-le dans votre app FNB)
    "adresse_banque": "First National Bank, Johannesburg, South Africa",  # <- vérifiez auprès de FNB
}

# --------------------------------------------------------------------------
# 4. OFFRES (prix en USD)
# --------------------------------------------------------------------------
ABONNEMENTS = [
    {"slug": "starter", "prix": 29, "installation": 149, "populaire": False},
    {"slug": "business", "prix": 49, "installation": 249, "populaire": True},
    {"slug": "business-pro", "prix": 89, "installation": 390, "populaire": False},
    {"slug": "ecommerce", "prix": 129, "installation": 590, "populaire": False},
]

FORFAITS = [
    {"slug": "landing-page", "icone": "send", "prix": 390},
    {"slug": "site-vitrine", "icone": "layers", "prix": 890},
    {"slug": "site-entreprise", "icone": "briefcase", "prix": 1490},
    {"slug": "site-ecommerce", "icone": "cart", "prix": 2490},
    {"slug": "sur-mesure", "icone": "code", "prix": None},   # None = sur devis
]

APPLICATIONS = [
    {"slug": "app-reservation", "prix": 19},
    {"slug": "app-facturation", "prix": 15},
    {"slug": "app-stock", "prix": 25},
]

ICONES_DEFIS = ["browser", "pulse", "monitor", "phone", "shield", "scale"]
ICONES_SERVICES = ["browser", "bag", "code", "portal", "plug", "phone", "app", "shield", "pulse"]

# --------------------------------------------------------------------------
# 5. TEXTES (français / anglais)
# --------------------------------------------------------------------------
TEXTES = {
    "fr": {
        "meta": {
            "title": "Baraza All Services — Création de sites web, applications et logiciels",
            "description": "Sites vitrines, boutiques en ligne, applications et logiciels sur mesure. Abonnement dès 29 $/mois ou projet à prix fixe. Paiement dans votre devise. Devis gratuit sous 24 h.",
            "og_title": "Sites web professionnels dès 29 $/mois — Baraza All Services",
        },
        "brand": {"tagline": "Développement Web & Logiciel"},
        "ui": {
            "skip": "Aller au contenu",
            "menu_open": "Ouvrir le menu",
            "menu_close": "Fermer le menu",
            "theme_dark": "Passer en mode sombre",
            "theme_light": "Passer en mode clair",
            "lang_switch": "Switch to English",
            "lang_label": "EN",
            "currency": "Devise",
            "currency_note": "Prix de référence en dollars US. Les montants dans une autre devise sont indicatifs (taux du jour).",
            "copy": "Copier",
            "copied": "Copié !",
            "from": "dès",
            "per_month": "/mois",
            "quote_only": "Sur devis",
            "whatsapp": "Me contacter sur WhatsApp",
            "top": "Retour en haut ↑",
            "rights": "Tous droits réservés.",
        },
        "nav": {
            "services": "Services", "pricing": "Tarifs", "apps": "Applications",
            "payment": "Paiement", "faq": "FAQ", "cta": "Devis gratuit",
        },
        "breadcrumb": {"home": "Accueil", "services": "Services", "current": "Développement Web & Logiciel"},
        "hero": {
            "eyebrow": "Développement web & logiciel",
            "title": "Des sites web professionnels pour les [[entreprises qui grandissent]]",
            "lead": "Lancez un site professionnel, ouvrez votre boutique en ligne ou simplifiez votre activité avec un logiciel sur mesure. Abonnement mensuel tout compris ou projet à prix fixe, payable dans votre devise, depuis n'importe quel pays.",
            "cta_primary": "Voir les formules",
            "cta_secondary": "Demander un devis gratuit",
            "proof1": "par mois, tout compris",
            "proof2_value": "24 h",
            "proof2": "pour recevoir votre devis",
            "proof3_value": "+15",
            "proof3": "devises acceptées",
        },
        "strip": ["Design & développement web", "Hébergement sécurisé", "Nom de domaine", "Support continu"],
        "challenges": {
            "eyebrow": "Défis numériques",
            "title": "Des outils dépassés freinent la [[croissance de votre entreprise]]",
            "lead": "Beaucoup d'entreprises perdent des clients à cause d'un site lent, d'outils qui ne communiquent pas, de tâches manuelles et d'une présence en ligne trop faible.",
            "items": [
                {"title": "Site web dépassé", "text": "Un site ancien, lent ou mal structuré fait perdre la confiance des visiteurs, réduit les demandes de contact et affaiblit votre image."},
                {"title": "Processus manuels", "text": "Les tâches répétitives font perdre du temps, multiplient les erreurs et freinent la croissance de votre activité."},
                {"title": "Outils déconnectés", "text": "Quand vos outils ne communiquent pas, vos équipes ressaisissent les données, jonglent avec des tableurs et perdent l'information."},
                {"title": "Mauvaise expérience mobile", "text": "Vos clients attendent une expérience rapide et fluide sur ordinateur, tablette et smartphone. Sans cela, ils partent chez un concurrent."},
                {"title": "Failles de sécurité", "text": "Extensions obsolètes, absence de sauvegardes et mauvaises pratiques exposent votre activité à des risques réels."},
                {"title": "Croissance limitée", "text": "Une plateforme doit pouvoir accueillir plus d'utilisateurs, de services, d'intégrations et de contenus au fil de votre développement."},
            ],
        },
        "services": {
            "eyebrow": "Services de développement",
            "title": "Des solutions web & logicielles construites [[autour de votre activité]]",
            "lead": "Nous créons des plateformes qui vous aident à attirer des clients, automatiser vos tâches, gérer vos informations, vendre en ligne et travailler plus efficacement.",
            "items": [
                {"title": "Sites vitrines professionnels", "text": "Des sites conçus pour inspirer confiance, présenter clairement votre valeur et transformer les visiteurs en demandes de devis."},
                {"title": "Boutiques en ligne", "text": "Catalogue produits, panier, paiement en ligne, gestion des commandes et parcours d'achat pensé pour vendre."},
                {"title": "Logiciels sur mesure", "text": "Des outils adaptés à vos processus internes : gestion, reporting, rôles utilisateurs et automatisations."},
                {"title": "Portails & espaces clients", "text": "Espaces clients, intranets, tableaux de bord, formulaires de demande et accès sécurisé aux documents."},
                {"title": "Intégrations & API", "text": "Connexion de votre site avec vos outils : paiement, CRM, emailing, bases de données et services tiers."},
                {"title": "Design UX / UI responsive", "text": "Des interfaces claires et agréables, pensées d'abord pour le mobile puis adaptées à tous les écrans."},
                {"title": "Applications web & mobiles", "text": "Des applications qui résolvent un besoin précis de votre activité et améliorent votre efficacité."},
                {"title": "Sécurité & maintenance", "text": "Mises à jour, sauvegardes, surveillance, certificat SSL, corrections et améliorations continues."},
                {"title": "Performance & SEO", "text": "Vitesse de chargement, référencement naturel, structure et fiabilité pour être trouvé sur Google."},
            ],
        },
        "pricing": {
            "eyebrow": "Formules de création de site",
            "title": "Construisez votre présence. [[Développez-vous en ligne.]]",
            "lead": "Choisissez la souplesse d'un abonnement mensuel tout compris ou investissez dans un projet à prix fixe. Des tarifs clairs, un travail professionnel et un vrai suivi.",
            "tab_monthly": "Abonnement mensuel",
            "tab_oneoff": "Paiement unique",
            "aria_tabs": "Type de formule",
            "intro_monthly": "Hébergement, SSL, maintenance et modifications inclus — un moyen économique d'avoir un site pro avec un suivi continu.",
            "intro_oneoff": "Vous préférez un projet ponctuel ? Nous le construisons pour vous, le site vous appartient.",
            "kicker": "Abonnement mensuel",
            "popular": "Le plus populaire",
            "setup": "de mise en place (une fois)",
            "choose": "Choisir",
            "order": "Commander",
            "ask_quote": "Demander un devis",
            "plans": {
                "starter": {"name": "Starter", "tagline": "Pour démarrer votre présence en ligne.", "features": ["Jusqu'à 3 pages responsive", "Hébergement & certificat SSL", "Formulaire de contact & WhatsApp", "SEO de base", "1 modification de contenu / mois"]},
                "business": {"name": "Business", "tagline": "Le meilleur équilibre pour les PME.", "features": ["Jusqu'à 8 pages", "Hébergement & certificat SSL", "Formulaires & statistiques de visite", "SEO de base optimisé", "2 modifications de contenu / mois"]},
                "business-pro": {"name": "Business Pro", "tagline": "Pour les entreprises qui veulent plus de clients.", "features": ["Jusqu'à 15 pages", "Formulaires avancés", "SEO avancé", "Rapport mensuel de performance", "4 modifications de contenu / mois"]},
                "ecommerce": {"name": "E-commerce", "tagline": "Vendez en ligne, 24 h / 24.", "features": ["Boutique en ligne (jusqu'à 30 produits)", "Paiement en ligne configuré", "Configuration des livraisons", "Hébergement géré & sauvegardes", "4 modifications de contenu / mois"]},
            },
            "packages": {
                "landing-page": {"name": "Landing page", "detail": "1 page, idéale pour une campagne publicitaire"},
                "site-vitrine": {"name": "Site vitrine", "detail": "Jusqu'à 5 pages"},
                "site-entreprise": {"name": "Site entreprise", "detail": "Jusqu'à 10 pages"},
                "site-ecommerce": {"name": "Site e-commerce", "detail": "Jusqu'à 30 produits"},
                "sur-mesure": {"name": "Site sur mesure / application web", "detail": "Fonctionnalités spécifiques, logiciel métier"},
            },
            "guarantees": ["Adapté au mobile", "Sécurité SSL", "Hébergement fiable", "Paiement dans votre devise", "Support dédié"],
        },
        "apps": {
            "eyebrow": "Applications prêtes à l'emploi",
            "title": "Des applications pour [[gagner du temps dès aujourd'hui]]",
            "lead": "Pas besoin de partir de zéro : ces applications sont déjà développées, nous les installons et les adaptons à votre entreprise en quelques jours.",
            "demo": "Demander une démo",
            "items": {
                "app-reservation": {"name": "Réservation en ligne", "category": "Salons, cabinets, restaurants", "text": "Vos clients réservent un créneau 24 h / 24, reçoivent des rappels automatiques et vous gérez votre agenda depuis un tableau de bord.", "features": ["Agenda & créneaux", "Rappels email / SMS", "Paiement d'acompte"]},
                "app-facturation": {"name": "Devis & facturation", "category": "Artisans, indépendants, TPE", "text": "Créez vos devis et factures en quelques clics, suivez les paiements et exportez votre comptabilité.", "features": ["Devis → facture", "Suivi des impayés", "Export comptable"]},
                "app-stock": {"name": "Gestion de stock & ventes", "category": "Commerces, grossistes", "text": "Suivez vos entrées, sorties et ventes en temps réel, avec alertes de rupture et statistiques claires.", "features": ["Inventaire en temps réel", "Alertes de rupture", "Rapports de ventes"]},
            },
        },
        "process": {
            "eyebrow": "Comment ça marche",
            "title": "Un processus simple, [[sans mauvaise surprise]]",
            "items": [
                {"title": "Échange découverte", "text": "Un appel gratuit de 30 minutes pour comprendre votre activité, vos objectifs et votre budget."},
                {"title": "Proposition & devis", "text": "Vous recevez une proposition claire : pages, fonctionnalités, délais et prix fixe en dollars. Aucune surprise."},
                {"title": "Acompte & design", "text": "Vous réglez l'acompte dans votre devise, nous concevons la maquette et vous la validez."},
                {"title": "Développement & mise en ligne", "text": "Développement, tests sur tous les écrans, domaine, SSL et référencement, puis lancement."},
                {"title": "Suivi & évolution", "text": "Maintenance, sauvegardes, mises à jour et nouvelles fonctionnalités selon vos besoins."},
            ],
        },
        "payment": {
            "eyebrow": "Moyens de paiement",
            "title": "Payez [[dans votre devise]], où que vous soyez",
            "lead": "Nos prix sont fixés en dollars américains (USD). Vous payez dans votre monnaie : la conversion est faite automatiquement par votre banque ou le prestataire de paiement, et les fonds arrivent sur notre compte professionnel FNB.",
            "methods": {
                "carte": {"title": "Carte bancaire", "text": "Visa, Mastercard, Apple Pay et Google Pay. Cliquez, saisissez votre carte sur la page sécurisée : c'est payé, depuis n'importe quel pays.", "button": "Payer par carte"},
                "payshap": {"title": "PayShap", "text": "Paiement instantané depuis l'application de votre banque sud-africaine (FNB, Absa, Capitec, Nedbank, Standard Bank…) avec notre ShapID.", "button": "Voir notre ShapID"},
                "eft": {"title": "EFT / virement local", "text": "Virement EFT ou instantané depuis toute banque sud-africaine vers notre compte FNB.", "button": "Voir les coordonnées"},
                "cash": {"title": "Espèces (cash)", "text": "Déposez des espèces à un guichet automatique (ATM) ou une agence FNB, avec notre numéro de compte et votre numéro de devis en référence.", "button": "Voir les coordonnées"},
                "mobile": {"title": "Mobile Money", "text": "M-Pesa, Airtel Money, Orange Money, MTN MoMo : envoyez depuis votre portefeuille vers notre compte FNB avec un service de transfert (WorldRemit, Mukuru…). Écrivez-nous, nous vous guidons.", "button": "Payer via WhatsApp"},
                "swift": {"title": "Virement international", "text": "Virement SWIFT depuis n'importe quelle banque dans le monde vers notre compte FNB.", "button": "Voir les coordonnées"},
                "paypal": {"title": "PayPal", "text": "Payez avec votre compte PayPal ou votre carte, depuis plus de 200 pays et dans votre devise.", "button": "Payer avec PayPal"},
                "wise": {"title": "Wise", "text": "Taux de change réel et frais réduits depuis plus de 160 pays, directement vers notre compte FNB.", "button": "Payer avec Wise"},
            },
            "bank_title": "Coordonnées bancaires FNB",
            "bank_lead": "Pour PayShap, EFT, dépôt d'espèces, Mobile Money et virements internationaux (SWIFT).",
            "bank_fields": {
                "banque": "Banque", "titulaire": "Titulaire du compte", "numero": "Numéro de compte", "shapid": "ShapID (PayShap)",
                "type": "Type de compte", "code_agence": "Code agence (branch code)", "swift": "Code SWIFT / BIC",
                "adresse_banque": "Adresse de la banque", "reference": "Référence du paiement",
            },
            "reference_value": "Votre numéro de devis ou votre nom",
            "steps_title": "Comment payer",
            "steps": [
                "Recevez votre devis ou votre facture en dollars (USD).",
                "Choisissez le moyen de paiement qui vous convient et payez dans votre devise.",
                "Indiquez votre numéro de devis en référence.",
                "Envoyez la preuve de paiement sur WhatsApp : nous confirmons sous 24 h.",
            ],
            "safety": "Nous ne vous demanderons jamais vos codes, mots de passe ou code PIN bancaires.",
            "wa_message": "Bonjour Baraza All Services, je souhaite payer par",
        },
        "faq": {
            "eyebrow": "Questions fréquentes",
            "title": "Vous avez des [[questions ?]]",
            "items": [
                {"q": "Dans quelle devise dois-je payer ?", "a": "Nos prix sont fixés en dollars américains (USD), mais vous payez dans votre propre devise : rand, euro, franc congolais, franc CFA, shilling, naira… La conversion est faite par votre banque, le paiement par carte ou le service de transfert au taux du jour."},
                {"q": "Quelle est la différence entre l'abonnement mensuel et le paiement unique ?", "a": "Avec l'abonnement, vous payez des frais de mise en place réduits puis un montant mensuel qui inclut l'hébergement, le SSL, la maintenance et des modifications de contenu. Avec le paiement unique, le site vous appartient après paiement ; l'hébergement et la maintenance peuvent être ajoutés séparément."},
                {"q": "Combien de temps faut-il pour créer mon site ?", "a": "Comptez en général 5 à 10 jours ouvrés pour une landing page ou un site vitrine, et 2 à 6 semaines pour une boutique en ligne ou une application sur mesure, selon la rapidité de réception des contenus."},
                {"q": "Comment se passe le paiement d'un projet ?", "a": "Pour un projet unique : 50 % d'acompte à la commande et 50 % à la mise en ligne. Pour un abonnement : les frais de mise en place à la commande, puis un paiement mensuel."},
                {"q": "Le nom de domaine est-il inclus ?", "a": "Nous nous occupons de l'enregistrement ou du transfert de votre nom de domaine. Le coût du domaine lui-même (environ 10 à 20 $ par an) est facturé à prix coûtant."},
                {"q": "Travaillez-vous avec des clients à l'étranger ?", "a": "Oui. Tout se fait à distance : appels vidéo, WhatsApp et email. Nous accompagnons des entreprises en Afrique, en Europe et ailleurs."},
            ],
        },
        "quote": {
            "eyebrow": "Devis gratuit",
            "title": "Parlons de [[votre projet]]",
            "lead": "Remplissez le formulaire : nous vous répondons sous 24 h ouvrées avec une proposition claire et un prix fixe. Vous préférez discuter directement ? Écrivez-nous sur WhatsApp.",
            "contact_whatsapp": "WhatsApp", "contact_email": "Email", "contact_zone": "Zone",
            "zone": "Afrique du Sud · Clients dans le monde entier",
            "f_name": "Nom complet", "p_name": "Ex. Marie Dupont",
            "f_email": "Adresse email", "p_email": "vous@entreprise.com",
            "f_phone": "Téléphone / WhatsApp", "p_phone": "+27 00 000 0000",
            "f_company": "Entreprise", "p_company": "Nom de votre entreprise",
            "f_country": "Pays", "p_country": "Ex. RDC, Afrique du Sud, France…",
            "f_offer": "Offre qui vous intéresse", "o_offer": "Choisissez une offre",
            "f_budget": "Budget estimé (USD)", "o_budget": "Sélectionnez (facultatif)",
            "budgets": ["Moins de 500 $", "500 à 1 500 $", "1 500 à 3 000 $", "3 000 à 10 000 $", "Plus de 10 000 $"],
            "f_message": "Votre projet", "p_message": "Décrivez votre activité, vos objectifs et vos délais…",
            "f_consent": "J'accepte d'être recontacté(e) au sujet de ma demande.",
            "optional": "(facultatif)",
            "submit": "Envoyer ma demande",
            "note": "Gratuit et sans engagement. Vos données ne sont utilisées que pour répondre à votre demande.",
            "err_name": "Merci d'indiquer votre nom.",
            "err_email": "Merci d'indiquer un email valide.",
            "err_offer": "Merci de choisir une offre.",
            "err_message": "Décrivez votre projet (10 caractères minimum).",
            "err_consent": "Votre accord est nécessaire pour que nous puissions vous répondre.",
            "ok_sent": "Merci {name} ! Votre demande a bien été envoyée. Nous vous répondons sous 24 h ouvrées.",
            "ok_whatsapp": "Merci {name} ! WhatsApp s'ouvre avec votre demande déjà rédigée, il ne reste qu'à l'envoyer.",
            "wa_intro": "Bonjour, je souhaite un devis.",
            "conseil": "Je ne sais pas encore, conseillez-moi",
            "offer_monthly": "Abonnement {name} — {price}/mois",
            "offer_oneoff": "{name} — {price} (paiement unique)",
            "offer_custom": "{name} — sur devis",
            "offer_app": "Application : {name}",
        },
        "final": {
            "title": "Prêt à mettre votre entreprise en ligne ?",
            "lead": "Sites professionnels dès 29 $/mois. Lancement rapide, tarifs clairs, paiement dans votre devise.",
            "cta": "Obtenir mon site",
            "whatsapp": "Discuter sur WhatsApp",
        },
        "footer": {
            "about": "Sites web, boutiques en ligne, applications et logiciels sur mesure pour les entreprises qui veulent grandir.",
            "services": "Nos services", "contact": "Contact", "info": "Informations clients",
            "links": ["Sites vitrines", "E-commerce", "Applications", "Paiement"],
            "info_links": ["Moyens de paiement", "Tarifs", "Questions fréquentes", "Conditions générales",
                           "Remboursements & annulations", "Garantie & support", "Confidentialité"],
            "reg": "N° d'enregistrement",
            "call": "Appeler",
        },
        "hours": {
            "title": "Heures d'ouverture",
            "lines": ["Lundi – vendredi : 08:00 – 17:00", "Samedi : sur rendez-vous", "Hors jours fériés sud-africains"],
            "note": "Rendez-vous en ligne ou sur place, sur réservation. Sur WhatsApp, nous répondons aussi en dehors de ces horaires.",
        },
        "trust": {
            "items": ["Paiement en ligne sécurisé par carte", "PayShap, EFT, espèces et Mobile Money",
                      "Clients en Afrique du Sud et à l'international", "Support et maintenance après livraison",
                      "Devis gratuit sous 24 h"],
            "registered": "Entreprise enregistrée en Afrique du Sud",
        },
        "legal": {
            "updated": "Dernière mise à jour : novembre 2026",
            "back": "← Retour à l'accueil",
            "contact_title": "Une question ?",
            "contact_text": "Contactez-nous, nous répondons sous 24 h ouvrées.",
            "terms": {
                "title": "Conditions générales",
                "sections": [
                    {"h": "1. Objet", "p": "Les présentes conditions s'appliquent à toutes les prestations de Baraza All Services : création de sites web, boutiques en ligne, applications, logiciels, hébergement, maintenance et abonnements. Toute commande vaut acceptation de ces conditions."},
                    {"h": "2. Devis et commande", "p": "Chaque projet fait l'objet d'un devis gratuit en dollars US (USD), valable 30 jours. La commande est confirmée par l'acceptation écrite du devis (email ou WhatsApp) et le paiement de l'acompte."},
                    {"h": "3. Prix et paiement", "p": "Les prix sont fixés en USD. Le client peut payer dans sa devise ; la conversion et les éventuels frais bancaires ou de change sont à sa charge. Pour les projets à prix fixe : 50 % d'acompte avant le début des travaux, 50 % à la mise en ligne. Les abonnements sont payables chaque mois, d'avance."},
                    {"h": "4. Délais", "p": "Les délais indiqués dans le devis commencent à la réception de l'acompte et de tous les contenus nécessaires (textes, images, logo, accès). Un retard dans la remise des contenus décale la livraison d'autant."},
                    {"h": "5. Obligations du client", "p": "Le client fournit des contenus dont il détient les droits et qui respectent la loi. Il reste responsable des textes, images et informations publiés sur son site."},
                    {"h": "6. Propriété", "p": "Pour les projets à prix fixe, le site et ses contenus appartiennent au client après paiement complet. Pour les abonnements, le site est mis à disposition tant que l'abonnement est actif ; le client peut racheter son site à tout moment selon le devis fourni."},
                    {"h": "7. Abonnements et résiliation", "p": "Les abonnements sont sans engagement de durée sauf mention contraire dans le devis. Ils peuvent être résiliés avec un préavis de 30 jours, par email ou WhatsApp."},
                    {"h": "8. Responsabilité", "p": "Nous mettons tout en œuvre pour fournir un service fiable et sécurisé. Notre responsabilité est limitée au montant payé pour la prestation concernée. Nous ne sommes pas responsables des pannes de services tiers (hébergeur, prestataire de paiement, fournisseur de domaine)."},
                    {"h": "9. Droit applicable", "p": "Ces conditions sont régies par le droit sud-africain, notamment le Consumer Protection Act et l'Electronic Communications and Transactions Act. En cas de litige, une solution amiable est recherchée en priorité."},
                ],
            },
            "refunds": {
                "title": "Remboursements & annulations",
                "sections": [
                    {"h": "Délai de réflexion", "p": "Vous pouvez annuler votre commande sans frais dans les 7 jours suivant le paiement, tant que le travail n'a pas commencé. L'acompte est alors remboursé intégralement."},
                    {"h": "Annulation après le début des travaux", "p": "Si vous annulez après le début des travaux, le travail déjà réalisé est facturé au prorata et le reste de l'acompte est remboursé. Les frais déjà engagés pour vous (nom de domaine, licences, thèmes payants) ne sont pas remboursables."},
                    {"h": "Abonnements", "p": "Un abonnement peut être résilié avec un préavis de 30 jours. Le mois en cours reste dû ; aucun remboursement n'est fait pour un mois déjà commencé."},
                    {"h": "Si le résultat ne correspond pas au devis", "p": "Si la livraison ne correspond pas à ce qui était prévu dans le devis, nous corrigeons gratuitement. Si nous ne pouvons pas corriger, nous remboursons la partie concernée."},
                    {"h": "Comment demander un remboursement", "p": "Envoyez votre demande par email ou WhatsApp avec votre numéro de devis. Le remboursement est fait sous 14 jours ouvrés, par le même moyen de paiement lorsque c'est possible."},
                ],
            },
            "warranty": {
                "title": "Garantie & support",
                "sections": [
                    {"h": "Garantie de 30 jours", "p": "Après la mise en ligne, nous corrigeons gratuitement pendant 30 jours tout défaut de fonctionnement lié à notre travail (lien cassé, affichage incorrect, formulaire qui ne marche pas)."},
                    {"h": "Abonnements : support inclus", "p": "Avec un abonnement mensuel, l'hébergement, les mises à jour de sécurité, les sauvegardes et les petites modifications prévues dans votre formule sont inclus tant que l'abonnement est actif."},
                    {"h": "Ce qui n'est pas couvert", "p": "Les nouvelles fonctionnalités, les changements de design, les problèmes causés par une modification faite par une autre personne, ou les pannes de services tiers. Ces demandes font l'objet d'un devis."},
                    {"h": "Comment nous contacter", "p": "Par WhatsApp ou par email, du lundi au vendredi de 08:00 à 17:00. Les problèmes bloquants (site inaccessible) sont traités en priorité."},
                ],
            },
            "privacy": {
                "title": "Politique de confidentialité",
                "sections": [
                    {"h": "Qui sommes-nous", "p": "Baraza All Services est responsable du traitement de vos données personnelles, conformément au Protection of Personal Information Act (POPIA) d'Afrique du Sud."},
                    {"h": "Données collectées", "p": "Uniquement ce que vous nous envoyez : nom, email, téléphone, entreprise, pays et message (formulaire de devis, WhatsApp ou email). Le site ne crée pas de compte et ne collecte pas vos données de carte bancaire."},
                    {"h": "Utilisation", "p": "Vos données servent uniquement à répondre à votre demande, préparer votre devis, réaliser la prestation et vous facturer. Elles ne sont jamais vendues ni utilisées pour de la publicité sans votre accord."},
                    {"h": "Paiements", "p": "Les paiements par carte sont traités par notre prestataire de paiement sécurisé (Yoco). Nous ne voyons ni ne stockons jamais vos numéros de carte."},
                    {"h": "Hébergement et cookies", "p": "Le site est hébergé par Netlify. Il ne place pas de cookies publicitaires ; il mémorise seulement dans votre navigateur votre langue, votre thème et votre devise."},
                    {"h": "Conservation", "p": "Nous conservons vos données le temps nécessaire à la relation commerciale et aux obligations comptables (en général 5 ans), puis nous les supprimons."},
                    {"h": "Vos droits", "p": "Vous pouvez demander à consulter, corriger ou supprimer vos données à tout moment par email ou WhatsApp. Vous pouvez aussi déposer une plainte auprès de l'Information Regulator (South Africa)."},
                ],
            },
        },
    },

    "en": {
        "meta": {
            "title": "Baraza All Services — Websites, apps and custom software",
            "description": "Business websites, online stores, apps and custom software. Plans from $29/month or fixed-price projects. Pay in your own currency. Free quote within 24 hours.",
            "og_title": "Professional websites from $29/month — Baraza All Services",
        },
        "brand": {"tagline": "Web & Software Development"},
        "ui": {
            "skip": "Skip to content",
            "menu_open": "Open menu",
            "menu_close": "Close menu",
            "theme_dark": "Switch to dark mode",
            "theme_light": "Switch to light mode",
            "lang_switch": "Passer en français",
            "lang_label": "FR",
            "currency": "Currency",
            "currency_note": "Reference prices in US dollars. Amounts in other currencies are estimates (today's rate).",
            "copy": "Copy",
            "copied": "Copied!",
            "from": "from",
            "per_month": "/month",
            "quote_only": "Custom quote",
            "whatsapp": "Contact us on WhatsApp",
            "top": "Back to top ↑",
            "rights": "All rights reserved.",
        },
        "nav": {
            "services": "Services", "pricing": "Pricing", "apps": "Apps",
            "payment": "Payment", "faq": "FAQ", "cta": "Free quote",
        },
        "breadcrumb": {"home": "Home", "services": "Services", "current": "Web & Software Development"},
        "hero": {
            "eyebrow": "Web & software development",
            "title": "Professional websites built for [[growing businesses]]",
            "lead": "Launch a professional website, open an online store or streamline your operations with custom software. Choose an all-inclusive monthly plan or a fixed-price project, payable in your own currency from any country.",
            "cta_primary": "Explore our packages",
            "cta_secondary": "Request a free quote",
            "proof1": "per month, all inclusive",
            "proof2_value": "24 h",
            "proof2": "to receive your quote",
            "proof3_value": "15+",
            "proof3": "currencies accepted",
        },
        "strip": ["Web design & development", "Secure hosting", "Domain registration", "Ongoing support"],
        "challenges": {
            "eyebrow": "Digital challenges",
            "title": "Outdated digital systems can limit [[business growth]]",
            "lead": "Many businesses lose customers because of slow websites, disconnected tools, manual processes and a weak online presence.",
            "items": [
                {"title": "Outdated websites", "text": "Old, slow or poorly structured websites damage trust, reduce enquiries and weaken your online presence."},
                {"title": "Manual processes", "text": "Repetitive manual tasks waste time, increase errors and make it difficult to scale your operations."},
                {"title": "Disconnected systems", "text": "When systems don't talk to each other, teams rely on duplicate work, spreadsheets and fragmented information."},
                {"title": "Poor mobile experience", "text": "Customers expect fast, responsive experiences on desktop, tablet and mobile. Without it, they go to a competitor."},
                {"title": "Security gaps", "text": "Outdated plugins, missing backups and weak development practices expose your business to real risks."},
                {"title": "Limited scalability", "text": "A digital platform must support more users, services, integrations and content as your business grows."},
            ],
        },
        "services": {
            "eyebrow": "Development services",
            "title": "Web & software solutions built [[around your operations]]",
            "lead": "We build digital platforms that help you attract customers, automate workflows, manage information, sell online and operate more efficiently.",
            "items": [
                {"title": "Business websites", "text": "Professional websites designed to build credibility, communicate your value and turn visitors into enquiries."},
                {"title": "Online stores", "text": "Product catalogues, cart, online payments, order management and a checkout flow designed to sell."},
                {"title": "Custom software", "text": "Tools tailored to your internal processes: management, reporting, user roles and automation."},
                {"title": "Portals & client areas", "text": "Client portals, intranets, dashboards, request forms and secure document access."},
                {"title": "Integrations & APIs", "text": "Connecting your website to your tools: payments, CRM, email marketing, databases and third-party services."},
                {"title": "Responsive UX / UI design", "text": "Clean, user-friendly interfaces designed mobile-first and adapted to every screen."},
                {"title": "Web & mobile apps", "text": "Applications that solve a specific business need and improve operational efficiency."},
                {"title": "Security & maintenance", "text": "Updates, backups, monitoring, SSL certificate, fixes and continuous improvement."},
                {"title": "Performance & SEO", "text": "Loading speed, search engine optimisation, structure and reliability so you get found on Google."},
            ],
        },
        "pricing": {
            "eyebrow": "Website packages",
            "title": "Build your presence. [[Grow online.]]",
            "lead": "Choose the flexibility of an all-inclusive monthly plan or invest in a fixed-price project. Clear pricing, professional delivery and real support.",
            "tab_monthly": "Monthly plans",
            "tab_oneoff": "One-off projects",
            "aria_tabs": "Package type",
            "intro_monthly": "Hosting, SSL, maintenance and content updates included — a cost-effective way to get a professional website with ongoing support.",
            "intro_oneoff": "Prefer a one-off project? We build it for you, and you own the website.",
            "kicker": "Monthly plan",
            "popular": "Most popular",
            "setup": "one-off setup fee",
            "choose": "Choose",
            "order": "Order",
            "ask_quote": "Request a quote",
            "plans": {
                "starter": {"name": "Starter", "tagline": "To launch your online presence.", "features": ["Up to 3 responsive pages", "Hosting & SSL certificate", "Contact form & WhatsApp", "Basic SEO setup", "1 content update / month"]},
                "business": {"name": "Business", "tagline": "The best balance for small businesses.", "features": ["Up to 8 pages", "Hosting & SSL certificate", "Forms & visitor analytics", "Optimised basic SEO", "2 content updates / month"]},
                "business-pro": {"name": "Business Pro", "tagline": "For businesses that want more customers.", "features": ["Up to 15 pages", "Advanced forms", "Enhanced SEO", "Monthly performance report", "4 content updates / month"]},
                "ecommerce": {"name": "eCommerce", "tagline": "Sell online, 24/7.", "features": ["Online store (up to 30 products)", "Payment gateway setup", "Shipping configuration", "Managed hosting & backups", "4 content updates / month"]},
            },
            "packages": {
                "landing-page": {"name": "Landing page", "detail": "1 page, ideal for an ad campaign"},
                "site-vitrine": {"name": "Starter website", "detail": "Up to 5 pages"},
                "site-entreprise": {"name": "Business website", "detail": "Up to 10 pages"},
                "site-ecommerce": {"name": "eCommerce website", "detail": "Up to 30 products"},
                "sur-mesure": {"name": "Custom website / web application", "detail": "Specific features, business software"},
            },
            "guarantees": ["Mobile-friendly", "SSL security", "Reliable hosting", "Pay in your currency", "Dedicated support"],
        },
        "apps": {
            "eyebrow": "Ready-made applications",
            "title": "Apps that [[save you time from day one]]",
            "lead": "No need to start from scratch: these applications are already built. We install them and adapt them to your business in a few days.",
            "demo": "Request a demo",
            "items": {
                "app-reservation": {"name": "Online booking", "category": "Salons, practices, restaurants", "text": "Customers book a slot 24/7, receive automatic reminders, and you manage your calendar from a dashboard.", "features": ["Calendar & slots", "Email / SMS reminders", "Deposit payments"]},
                "app-facturation": {"name": "Quotes & invoicing", "category": "Tradespeople, freelancers, small businesses", "text": "Create quotes and invoices in a few clicks, track payments and export your accounts.", "features": ["Quote → invoice", "Unpaid tracking", "Accounting export"]},
                "app-stock": {"name": "Stock & sales management", "category": "Shops, wholesalers", "text": "Track stock in, stock out and sales in real time, with low-stock alerts and clear reports.", "features": ["Real-time inventory", "Low-stock alerts", "Sales reports"]},
            },
        },
        "process": {
            "eyebrow": "How it works",
            "title": "A simple process, [[no surprises]]",
            "items": [
                {"title": "Discovery call", "text": "A free 30-minute call to understand your business, goals and budget."},
                {"title": "Proposal & quote", "text": "You receive a clear proposal: pages, features, timeline and a fixed price in US dollars. No surprises."},
                {"title": "Deposit & design", "text": "You pay the deposit in your currency, we design the mock-up and you approve it."},
                {"title": "Build & launch", "text": "Development, testing on every screen, domain, SSL and SEO setup, then launch."},
                {"title": "Support & growth", "text": "Maintenance, backups, updates and new features as your needs evolve."},
            ],
        },
        "payment": {
            "eyebrow": "Payment methods",
            "title": "Pay [[in your own currency]], wherever you are",
            "lead": "Our prices are set in US dollars (USD). You pay in your own currency: the conversion is handled automatically by your bank or payment provider, and the funds land in our FNB business account.",
            "methods": {
                "carte": {"title": "Card payment", "text": "Visa, Mastercard, Apple Pay and Google Pay. Click, enter your card on the secure page and you're done, from any country.", "button": "Pay by card"},
                "payshap": {"title": "PayShap", "text": "Instant payment from your South African banking app (FNB, Absa, Capitec, Nedbank, Standard Bank…) using our ShapID.", "button": "View our ShapID"},
                "eft": {"title": "EFT / local transfer", "text": "EFT or instant transfer from any South African bank to our FNB account.", "button": "View bank details"},
                "cash": {"title": "Cash deposit", "text": "Deposit cash at any FNB ATM or branch using our account number, with your quote number as reference.", "button": "View bank details"},
                "mobile": {"title": "Mobile Money", "text": "M-Pesa, Airtel Money, Orange Money, MTN MoMo: send from your wallet to our FNB account with a transfer service (WorldRemit, Mukuru…). Message us and we'll guide you.", "button": "Pay via WhatsApp"},
                "swift": {"title": "International transfer", "text": "SWIFT transfer from any bank in the world to our FNB account.", "button": "View bank details"},
                "paypal": {"title": "PayPal", "text": "Pay with your PayPal account or card, from over 200 countries and in your own currency.", "button": "Pay with PayPal"},
                "wise": {"title": "Wise", "text": "Real exchange rate and low fees from over 160 countries, straight to our FNB account.", "button": "Pay with Wise"},
            },
            "bank_title": "FNB bank details",
            "bank_lead": "For PayShap, EFT, cash deposits, Mobile Money and international (SWIFT) transfers.",
            "bank_fields": {
                "banque": "Bank", "titulaire": "Account holder", "numero": "Account number", "shapid": "ShapID (PayShap)",
                "type": "Account type", "code_agence": "Branch code", "swift": "SWIFT / BIC code",
                "adresse_banque": "Bank address", "reference": "Payment reference",
            },
            "reference_value": "Your quote number or your name",
            "steps_title": "How to pay",
            "steps": [
                "Receive your quote or invoice in US dollars (USD).",
                "Choose the payment method that suits you and pay in your own currency.",
                "Use your quote number as the payment reference.",
                "Send the proof of payment on WhatsApp: we confirm within 24 hours.",
            ],
            "safety": "We will never ask for your banking codes, passwords or PIN.",
            "wa_message": "Hello Baraza All Services, I would like to pay by",
        },
        "faq": {
            "eyebrow": "Frequently asked questions",
            "title": "Got [[questions?]]",
            "items": [
                {"q": "Which currency do I pay in?", "a": "Our prices are set in US dollars (USD), but you pay in your own currency: rand, euro, Congolese franc, CFA franc, shilling, naira… The conversion is handled by your bank, the card payment or the transfer service at the day's rate."},
                {"q": "What is the difference between a monthly plan and a one-off project?", "a": "With a monthly plan, you pay a reduced setup fee and then a monthly amount that includes hosting, SSL, maintenance and content updates. With a one-off project, you own the website once paid; hosting and maintenance can be added separately."},
                {"q": "How long does it take to build my website?", "a": "Usually 5 to 10 working days for a landing page or business website, and 2 to 6 weeks for an online store or custom application, depending on how quickly we receive your content."},
                {"q": "How does project payment work?", "a": "For a one-off project: a 50% deposit when you order and 50% at launch. For a monthly plan: the setup fee when you order, then a monthly payment."},
                {"q": "Is the domain name included?", "a": "We handle registering or transferring your domain name. The domain itself (about $10 to $20 per year) is charged at cost."},
                {"q": "Do you work with clients abroad?", "a": "Yes. Everything is done remotely: video calls, WhatsApp and email. We work with businesses in Africa, Europe and beyond."},
            ],
        },
        "quote": {
            "eyebrow": "Free quote",
            "title": "Let's talk about [[your project]]",
            "lead": "Fill in the form and we'll reply within 24 working hours with a clear proposal and a fixed price. Prefer to chat directly? Message us on WhatsApp.",
            "contact_whatsapp": "WhatsApp", "contact_email": "Email", "contact_zone": "Location",
            "zone": "South Africa · Clients worldwide",
            "f_name": "Full name", "p_name": "e.g. Mary Smith",
            "f_email": "Email address", "p_email": "you@company.com",
            "f_phone": "Phone / WhatsApp", "p_phone": "+27 00 000 0000",
            "f_company": "Company", "p_company": "Your company name",
            "f_country": "Country", "p_country": "e.g. DRC, South Africa, Kenya…",
            "f_offer": "Package you're interested in", "o_offer": "Choose a package",
            "f_budget": "Estimated budget (USD)", "o_budget": "Select (optional)",
            "budgets": ["Under $500", "$500 to $1,500", "$1,500 to $3,000", "$3,000 to $10,000", "Over $10,000"],
            "f_message": "Your project", "p_message": "Describe your business, your goals and your timeline…",
            "f_consent": "I agree to be contacted about my request.",
            "optional": "(optional)",
            "submit": "Send my request",
            "note": "Free and no obligation. Your data is only used to reply to your request.",
            "err_name": "Please enter your name.",
            "err_email": "Please enter a valid email address.",
            "err_offer": "Please choose a package.",
            "err_message": "Please describe your project (at least 10 characters).",
            "err_consent": "We need your consent to be able to reply.",
            "ok_sent": "Thank you {name}! Your request has been sent. We'll reply within 24 working hours.",
            "ok_whatsapp": "Thank you {name}! WhatsApp is opening with your request ready to send.",
            "wa_intro": "Hello, I would like a quote.",
            "conseil": "I'm not sure yet, please advise me",
            "offer_monthly": "{name} plan — {price}/month",
            "offer_oneoff": "{name} — {price} (one-off)",
            "offer_custom": "{name} — custom quote",
            "offer_app": "App: {name}",
        },
        "final": {
            "title": "Ready to take your business online?",
            "lead": "Professional websites from $29/month. Fast launch, clear pricing, pay in your own currency.",
            "cta": "Get your website",
            "whatsapp": "Chat on WhatsApp",
        },
        "footer": {
            "about": "Websites, online stores, apps and custom software for businesses that want to grow.",
            "services": "Our services", "contact": "Contact", "info": "Customer information",
            "links": ["Business websites", "eCommerce", "Apps", "Payment"],
            "info_links": ["Payment methods", "Pricing", "FAQs", "Terms & Conditions",
                           "Refunds & cancellations", "Warranty & support", "Privacy policy"],
            "reg": "Registration No.",
            "call": "Call",
        },
        "hours": {
            "title": "Business hours",
            "lines": ["Monday – Friday: 08:00 – 17:00", "Saturday: by appointment", "Excluding South African public holidays"],
            "note": "Online or in-person meetings by appointment. On WhatsApp we also reply outside these hours.",
        },
        "trust": {
            "items": ["Secure online card payments", "PayShap, EFT, cash and Mobile Money",
                      "Clients in South Africa and worldwide", "Support and maintenance after launch",
                      "Free quote within 24 hours"],
            "registered": "Registered South African company",
        },
        "legal": {
            "updated": "Last updated: November 2026",
            "back": "← Back to home",
            "contact_title": "Any questions?",
            "contact_text": "Get in touch, we reply within 24 working hours.",
            "terms": {
                "title": "Terms & Conditions",
                "sections": [
                    {"h": "1. Scope", "p": "These terms apply to all Baraza All Services work: websites, online stores, apps, software, hosting, maintenance and subscriptions. Placing an order means you accept these terms."},
                    {"h": "2. Quotes and orders", "p": "Every project starts with a free quote in US dollars (USD), valid for 30 days. An order is confirmed when the quote is accepted in writing (email or WhatsApp) and the deposit is paid."},
                    {"h": "3. Prices and payment", "p": "Prices are set in USD. Clients may pay in their own currency; conversion and any bank or exchange fees are the client's responsibility. Fixed-price projects: 50% deposit before work starts, 50% at launch. Subscriptions are paid monthly in advance."},
                    {"h": "4. Timelines", "p": "Timelines in the quote start once the deposit and all required content (text, images, logo, access details) have been received. Late content delays delivery by the same amount of time."},
                    {"h": "5. Client responsibilities", "p": "The client provides content they own the rights to and that complies with the law. The client remains responsible for the text, images and information published on their site."},
                    {"h": "6. Ownership", "p": "For fixed-price projects, the site and its content belong to the client once paid in full. For subscriptions, the site is provided while the subscription is active; the client may buy out their site at any time based on the quote provided."},
                    {"h": "7. Subscriptions and cancellation", "p": "Subscriptions have no minimum term unless stated in the quote. They can be cancelled with 30 days' notice by email or WhatsApp."},
                    {"h": "8. Liability", "p": "We do everything we can to provide a reliable, secure service. Our liability is limited to the amount paid for the service concerned. We are not responsible for outages of third-party services (hosting, payment provider, domain registrar)."},
                    {"h": "9. Governing law", "p": "These terms are governed by South African law, including the Consumer Protection Act and the Electronic Communications and Transactions Act. Any dispute will first be settled amicably where possible."},
                ],
            },
            "refunds": {
                "title": "Refunds & cancellations",
                "sections": [
                    {"h": "Cooling-off period", "p": "You may cancel your order free of charge within 7 days of payment, as long as work has not started. The deposit is then refunded in full."},
                    {"h": "Cancelling after work has started", "p": "If you cancel after work has started, the work already done is charged pro rata and the rest of the deposit is refunded. Costs already incurred on your behalf (domain name, licences, paid themes) are non-refundable."},
                    {"h": "Subscriptions", "p": "A subscription can be cancelled with 30 days' notice. The current month remains payable; no refund is given for a month already started."},
                    {"h": "If the result doesn't match the quote", "p": "If the delivery doesn't match what was agreed in the quote, we fix it free of charge. If we can't fix it, we refund the part concerned."},
                    {"h": "How to request a refund", "p": "Send your request by email or WhatsApp with your quote number. Refunds are made within 14 working days, using the same payment method where possible."},
                ],
            },
            "warranty": {
                "title": "Warranty & support",
                "sections": [
                    {"h": "30-day warranty", "p": "For 30 days after launch, we fix free of charge any malfunction caused by our work (broken link, display issue, form not working)."},
                    {"h": "Subscriptions: support included", "p": "With a monthly subscription, hosting, security updates, backups and the small changes included in your plan are covered while the subscription is active."},
                    {"h": "What is not covered", "p": "New features, design changes, issues caused by changes made by someone else, or third-party outages. These requests are quoted separately."},
                    {"h": "How to reach us", "p": "By WhatsApp or email, Monday to Friday, 08:00 to 17:00. Critical issues (site down) are handled first."},
                ],
            },
            "privacy": {
                "title": "Privacy policy",
                "sections": [
                    {"h": "Who we are", "p": "Baraza All Services is responsible for processing your personal information, in line with South Africa's Protection of Personal Information Act (POPIA)."},
                    {"h": "Information we collect", "p": "Only what you send us: name, email, phone, company, country and message (quote form, WhatsApp or email). The site does not create accounts and does not collect your card details."},
                    {"h": "How we use it", "p": "Your information is used only to answer your request, prepare your quote, deliver the work and invoice you. It is never sold or used for advertising without your consent."},
                    {"h": "Payments", "p": "Card payments are processed by our secure payment provider (Yoco). We never see or store your card numbers."},
                    {"h": "Hosting and cookies", "p": "The site is hosted by Netlify. It sets no advertising cookies; it only remembers your language, theme and currency in your browser."},
                    {"h": "Retention", "p": "We keep your information for as long as needed for our business relationship and accounting obligations (usually 5 years), then delete it."},
                    {"h": "Your rights", "p": "You can ask to access, correct or delete your information at any time by email or WhatsApp. You may also lodge a complaint with the Information Regulator (South Africa)."},
                ],
            },
        },
    },
}
