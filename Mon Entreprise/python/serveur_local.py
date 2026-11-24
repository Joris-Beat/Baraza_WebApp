"""
Serveur local pour tester le site avant de le publier.

Utilisation (depuis le dossier « Mon Entreprise ») :
    python python/serveur_local.py
Puis ouvrez http://localhost:8000 dans votre navigateur (ouverture automatique).
Arrêt : Ctrl + C
"""
import functools
import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8000
DOSSIER_SITE = Path(__file__).resolve().parent.parent / "site"


def main() -> None:
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DOSSIER_SITE))
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), handler) as serveur:
        url = f"http://localhost:{PORT}"
        print(f"Site disponible sur {url}  (Ctrl + C pour arrêter)")
        webbrowser.open(url)
        try:
            serveur.serve_forever()
        except KeyboardInterrupt:
            print("\nServeur arrêté.")


if __name__ == "__main__":
    main()
