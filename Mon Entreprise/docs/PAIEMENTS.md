# Recevoir les paiements sur le compte FNB

Les prix du site sont en **dollars US**. Le client paie **dans sa propre devise** : la conversion est faite par sa banque
ou par le prestataire, et l'argent arrive en **rand (ZAR)** sur ton compte **FNB**.

Le site ne stocke **aucune** donnée de carte : chaque paiement se fait sur la page sécurisée du prestataire.

| Moyen | Pour qui | Arrive sur FNB ? | À configurer dans `python/contenu.py` |
|---|---|---|---|
| Carte (Visa, Mastercard, Apple/Google Pay) | Clients du monde entier | Oui, versement automatique | `LIENS_PAIEMENT["carte"]` |
| PayPal | Clients du monde entier | Oui, retrait vers FNB | `LIENS_PAIEMENT["paypal"]` |
| Wise | Clients de 160+ pays | Oui, directement | `LIENS_PAIEMENT["wise"]` (facultatif) |
| Virement international SWIFT | Toute banque dans le monde | Oui | `COMPTE_FNB` |
| EFT / paiement instantané | Afrique du Sud | Oui | `COMPTE_FNB` |
| Mobile Money | RDC, Kenya, etc. | Via un service de transfert | rien (WhatsApp) |

Tant qu'un lien est vide, le bouton correspondant ouvre WhatsApp avec un message prérempli (« je souhaite payer par… »).
Pour Wise, sans lien, le bouton affiche les coordonnées FNB (le client envoie via Wise vers ton compte).

---

## 1. Coordonnées FNB (obligatoire)

Dans `python/contenu.py`, bloc `COMPTE_FNB` :

- `numero` : ton numéro de compte (remplace `À COMPLÉTER`) ;
- `code_agence` : **250655** est le code universel FNB ;
- `swift` : **FIRNZAJJ** est le code SWIFT/BIC de FNB ;
- `type`, `titulaire` et `adresse_banque` : vérifie-les dans l'app FNB (*Accounts → ton compte → Account details / Share account details*).

**Virements internationaux entrants** : FNB te demandera de confirmer chaque paiement reçu de l'étranger
(motif du paiement, déclaration à la Banque centrale). Tu le fais dans l'app FNB ou sur fnb.co.za
(rubrique *Forex / Global Payments → Inward payments*). Garde la facture correspondante.

## 2. Paiement par carte (recommandé)

Choisis **un** prestataire sud-africain ; tous versent l'argent sur un compte FNB et acceptent les cartes étrangères :

- **PayFast** (payfast.io) — *Payment links* / *Pay Now button*.
- **Yoco** (yoco.com) — *Payment links*, très simple, versement rapide.
- **Paystack** (paystack.com, Afrique du Sud) — *Payment pages*.

Étapes (exemple PayFast, similaires ailleurs) :
1. Crée un compte marchand (pièce d'identité, justificatif d'adresse, coordonnées FNB ; enregistrement CIPC si tu es une société).
2. Ajoute ton compte FNB comme compte de versement.
3. Crée un **lien de paiement** (montant libre, ou un lien par offre).
4. Colle-le dans `LIENS_PAIEMENT["carte"]`, puis lance `python python\construire_site.py`.

Le client étranger paie avec sa carte dans sa devise ; sa banque convertit, tu reçois des rands.

## 3. PayPal

1. Crée un compte **PayPal Business** (paypal.com/za).
2. Associe ton compte FNB : sur fnb.co.za, rubrique **PayPal** (*Forex → PayPal*), suis les étapes de liaison.
3. Crée ton lien **paypal.me** (ex. `https://paypal.me/BarazaAllServices`).
4. Colle-le dans `LIENS_PAIEMENT["paypal"]`.

Les clients paient en dollars (ou dans leur devise) ; tu retires ensuite le solde vers FNB.

## 4. Wise

- Le client peut envoyer de l'argent avec Wise **directement vers tes coordonnées FNB**, sans compte Wise de ton côté.
- Si tu ouvres un compte Wise, crée ton lien de paiement (`wise.com/pay/me/...`) et colle-le dans `LIENS_PAIEMENT["wise"]`.

## 5. Mobile Money (M-Pesa, Airtel Money, Orange Money, MTN MoMo)

Le Mobile Money ne peut pas être envoyé directement sur un compte FNB. Le client passe par un service de transfert
international qui accepte son portefeuille mobile et verse vers un compte bancaire sud-africain (vérifie la disponibilité
dans son pays : Wise, WorldRemit, Mukuru…). Le bouton du site ouvre WhatsApp pour que tu le guides au cas par cas.

## 6. Bonnes pratiques

- Envoie toujours un **devis / une facture** en USD avec un numéro, et demande ce numéro en **référence** de paiement.
- Demande l'acompte **avant** de commencer (50 %), le solde à la mise en ligne.
- Confirme chaque paiement par WhatsApp ou email dès qu'il arrive.
- Ne communique jamais tes codes, mots de passe ou OTP FNB : aucun client n'en a besoin pour te payer.
- Renseigne-toi auprès d'un comptable sur la TVA et l'impôt sur le revenu (SARS).
