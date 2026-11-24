# Mettre le site en ligne

Deux hébergeurs gratuits au choix. **Netlify est recommandé** : le formulaire de devis y fonctionne sans rien coder.

Avant de commencer : personnalise `python/contenu.py`, lance `python python\construire_site.py` puis `python python\verifier_site.py`. Pour les paiements, voir `PAIEMENTS.md`.

---

## Option A — Netlify (recommandé)

### Méthode 1 : glisser-déposer (5 minutes, sans installation)

1. Crée un compte gratuit sur https://app.netlify.com/signup.
2. Dans le tableau de bord : **Add new site → Deploy manually**.
3. Fais glisser **le dossier `site`** (pas le dossier `Mon Entreprise`) dans la zone indiquée.
4. Ton site est en ligne à une adresse du type `https://nom-aleatoire.netlify.app`.
5. **Site configuration → Change site name** pour choisir un nom, par exemple `baraza-all-services` → `https://baraza-all-services.netlify.app`.

Pour mettre à jour : **Deploys → glisser à nouveau le dossier `site`**.

### Méthode 2 : avec GitHub (mise à jour automatique)

1. Mets le dossier `Mon Entreprise` dans un dépôt GitHub.
2. Netlify : **Add new site → Import an existing project → GitHub**, choisis le dépôt.
3. Laisse *Build command* vide. *Publish directory* : `site` (déjà indiqué dans `netlify.toml`).
4. **Deploy**. Chaque `git push` met le site à jour automatiquement.

### Méthode 3 : en ligne de commande

```
npm install -g netlify-cli
netlify login
netlify deploy --prod
```
(À lancer dans le dossier `Mon Entreprise` ; Node.js requis : https://nodejs.org)

### Recevoir les demandes de devis par email

1. Netlify : **Site configuration → Forms → Enable form detection**, puis redéploie le site.
2. Le formulaire **devis** apparaît dans l'onglet **Forms**.
3. **Forms → Form notifications → Add notification → Email notification** → ton email.

Le plan gratuit inclut 100 demandes par mois.

---

## Option B — Firebase Hosting

1. Installe **Node.js** (version LTS) : https://nodejs.org.
2. Crée un projet sur https://console.firebase.google.com → **Ajouter un projet** (Google Analytics facultatif). Note l'**ID du projet** (ex. `baraza-all-services-4f2a1`).
3. Ouvre `.firebaserc` et remplace `baraza-all-services` par ton ID de projet.
4. Ouvre un terminal dans le dossier `Mon Entreprise` (barre d'adresse → `cmd` → Entrée) :
   ```
   npm install -g firebase-tools
   firebase login
   firebase deploy --only hosting
   ```
5. Le site est en ligne sur `https://TON-ID.web.app` et `https://TON-ID.firebaseapp.com`.

Pour mettre à jour : relance `firebase deploy --only hosting`.

Pour tester avant de publier : `firebase emulators:start --only hosting` puis http://localhost:5000.

> `firebase.json` indique déjà que le dossier publié est `site` : **ne lance pas `firebase init`**,
> ou, si tu le fais, réponds `site` au dossier public et **Non** à « overwrite index.html ».

Sur Firebase, le formulaire de devis ouvre WhatsApp avec la demande déjà rédigée.

---

## Nom de domaine personnalisé (ex. monentreprise.com)

1. Achète le domaine (Namecheap, OVH, Google Domains/Squarespace, etc.).
2. **Netlify** : *Domain management → Add a domain*, puis suis les instructions DNS.
   **Firebase** : *Hosting → Ajouter un domaine personnalisé*, puis ajoute les enregistrements DNS indiqués.
3. Le certificat HTTPS (cadenas) est créé automatiquement, en quelques minutes à quelques heures.
4. Mets ensuite ton domaine dans `python/contenu.py` (`site_url`), dans `site/robots.txt` et `site/sitemap.xml`, puis lance `python python\construire_site.py`.

## Après la mise en ligne

- **Google** : ajoute le site dans https://search.google.com/search-console et envoie `sitemap.xml`.
- **Facebook / WhatsApp** : vérifie l'aperçu du lien sur https://developers.facebook.com/tools/debug/.
- **Publicités** : pour pointer vers une offre précise, utilise un lien du type
  `https://ton-site/?offre=business#devis` (l'offre est présélectionnée dans le formulaire).
