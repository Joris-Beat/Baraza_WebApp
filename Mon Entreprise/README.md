# Baraza All Services — site « Développement Web & Logiciel »

Site pour vendre des sites web, des applications et des logiciels sur mesure.

- **Deux langues** : français / anglais (bouton `EN` / `FR`, détection automatique de la langue du navigateur)
- **Mode clair / sombre** (bouton soleil / lune, mémorisé ; suit le réglage de l'appareil par défaut)
- **Prix en dollars US ($)**, avec affichage de l'équivalent dans 18 devises (taux du jour)
- **Paiement** : carte, PayPal, virement international (SWIFT), EFT, Wise, Mobile Money → **compte FNB**
- Formulaire de devis, bouton WhatsApp, référencement Google

Site **statique** : il s'héberge gratuitement sur **Netlify** ou **Firebase Hosting**.

## Structure des dossiers

```
Mon Entreprise/
├── site/                     ← TOUT ce qui est publié en ligne
│   ├── index.html            ← page principale (générée)
│   ├── 404.html              ← page « introuvable »
│   ├── robots.txt, sitemap.xml
│   ├── css/
│   │   └── style.css         ← design, couleurs (mode sombre + mode clair)
│   ├── js/
│   │   ├── main.js           ← interactions : langue, thème, devises, paiement, formulaire
│   │   ├── i18n.js           ← traductions FR / EN (généré)
│   │   └── config.js         ← contact, devises, liens de paiement (généré)
│   └── images/
│       ├── favicon.svg, logo.svg
│       └── og-image.png      ← image affichée quand on partage le lien
├── python/                   ← outils (non publiés)
│   ├── contenu.py            ← ★ TEXTES, PRIX, CONTACT, PAIEMENT : le seul fichier à modifier
│   ├── construire_site.py    ← régénère index.html, i18n.js, config.js
│   ├── serveur_local.py      ← tester le site sur ton PC
│   └── verifier_site.py      ← vérifier liens et valeurs à remplacer
├── docs/
│   ├── DEPLOIEMENT.md        ← mettre en ligne (Netlify, Firebase)
│   └── PAIEMENTS.md          ← recevoir les paiements sur le compte FNB
├── netlify.toml, firebase.json, .firebaserc
└── README.md
```

> **Java ou JavaScript ?** Un site web utilise **JavaScript** (dossier `js/`), pas Java.
> Python n'est pas publié en ligne : il sert d'outil sur ton ordinateur pour générer et tester le site.

## Modifier le site (textes, prix, coordonnées)

1. Installe Python : https://www.python.org/downloads/ (coche « Add Python to PATH »).
2. Ouvre `python/contenu.py` avec **VS Code** et modifie :
   - `ENTREPRISE` : email, téléphone, numéro WhatsApp (ex. `27821234567`), adresse du site ;
   - `COMPTE_FNB` : **ton numéro de compte FNB** (et vérifie les autres champs) ;
   - `LIENS_PAIEMENT` : tes liens PayFast/Yoco/Paystack, PayPal, Wise (voir `docs/PAIEMENTS.md`) ;
   - `ABONNEMENTS`, `FORFAITS`, `APPLICATIONS` : tes prix en dollars ;
   - `TEXTES` : tous les textes, en français (`fr`) et en anglais (`en`).
3. Dans le dossier `Mon Entreprise`, ouvre un terminal (barre d'adresse de l'explorateur → `cmd` → Entrée) et lance :
   ```
   python python\construire_site.py
   python python\verifier_site.py
   ```

**Couleurs** : en haut de `site/css/style.css` (bloc mode sombre, puis bloc mode clair).

## Tester sur ton ordinateur

```
python python\serveur_local.py
```
Le site s'ouvre sur http://localhost:8000 (`Ctrl + C` pour arrêter).
Tu peux aussi double-cliquer sur `site/index.html`.

## Formulaire de devis

- **Sur Netlify** : les demandes sont enregistrées (Netlify Forms) et envoyées par email.
- **Sur Firebase ou en local** : la demande s'ouvre dans **WhatsApp**, déjà rédigée.

## Mettre en ligne / recevoir les paiements

- **[docs/DEPLOIEMENT.md](docs/DEPLOIEMENT.md)** — Netlify et Firebase, étape par étape
- **[docs/PAIEMENTS.md](docs/PAIEMENTS.md)** — carte, PayPal, Wise, SWIFT, EFT vers ton compte FNB
