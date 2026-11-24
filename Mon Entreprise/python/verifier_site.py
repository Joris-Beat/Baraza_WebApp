"""
Vérifie le site avant publication :
  - liens et images locaux introuvables (css/, js/, images/ ...)
  - valeurs d'exemple oubliées (numéro, email, adresse du site)

Utilisation (depuis le dossier « Mon Entreprise ») :
    python python/verifier_site.py
"""
import re
import sys
from pathlib import Path

DOSSIER_SITE = Path(__file__).resolve().parent.parent / "site"
VALEURS_EXEMPLE = ["27000000000", "+27 00 000 0000", "contact@example.com", "À COMPLÉTER", "baraza-all-services.netlify.app"]


def main() -> int:
    problemes = 0
    for page in sorted(DOSSIER_SITE.glob("*.html")):
        html = page.read_text(encoding="utf-8")
        for lien in re.findall(r'(?:href|src)="([^"#?]+)', html):
            if lien.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            cible = (DOSSIER_SITE / lien.lstrip("/")) if lien.startswith("/") else (page.parent / lien)
            if not cible.exists():
                print(f"[ERREUR] {page.name} : fichier introuvable -> {lien}")
                problemes += 1
        for valeur in VALEURS_EXEMPLE:
            if valeur in html:
                print(f"[A FAIRE] {page.name} : valeur d'exemple « {valeur} » -> modifiez python/contenu.py puis lancez python/construire_site.py")
    if problemes == 0:
        print("OK : aucun lien ou fichier manquant.")
    return 1 if problemes else 0


if __name__ == "__main__":
    sys.exit(main())
