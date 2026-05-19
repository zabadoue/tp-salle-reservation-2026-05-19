# tp-python-backendbackendrequirementstxt-2026-05-19

> Projet généré automatiquement par **TP_maker** — Usine Logicielle Multi-Agents IA

## Stack
- **Langage principal** : Python (Backend) et HTML/CSS (Frontend)
- **Généré le** : 2026-05-19

## Tâches implémentées
- [BACKEND:backend/requirements.txt] Contenu du fichier : fastapi, uvicorn
- [BACKEND:backend/modeles.py] Classe Salle : attributs privés _id_salle: int, _nom: str, _capacite: int, _est_reservee: bool. Constructeur __init__(self, id_salle: int, nom: str, capacite: int) -> None. Classe GestionnaireSalles : attribut privé _salles: list[Salle]. Méthodes : ajouter_salle(self, salle: Salle) -> None, lister_disponibles(self) -> list[dict], reserver_salle(self, id_salle: int) -> bool. La méthode lister_disponibles doit retourner une liste de dictionnaires contenant id, nom, capacite pour chaque salle où _est_reservee est False.
- [BACKEND:backend/api.py] Importer FastAPI, CORSMiddleware, uvicorn et les classes de modeles.py. Configurer CORSMiddleware avec allow_origins=['*'], allow_methods=['*'], allow_headers=['*']. Instance globale 'gestionnaire' de GestionnaireSalles. Route GET '/salles' retournant list[dict]. Route POST '/reserver/{id_salle}' retournant dict avec clé 'success': bool. Lancer le serveur via uvicorn.run sur host='0.0.0.0', port=8000.
- [FRONTEND:frontend/index.html] Structure HTML5 avec lien vers style.css. Conteneur <div id='app'> contenant <h1>Gestion des Salles</h1> et <div id='liste-salles'>. Inclure un bloc <script> : au chargement, fetch('http://localhost:8000/salles') pour générer dynamiquement des cartes dans #liste-salles. Chaque carte doit contenir le nom, la capacité et un bouton avec id='btn-{id_salle}' qui déclenche fetch('http://localhost:8000/reserver/'+id, {method: 'POST'}) et rafraîchit la liste.
- [FRONTEND:frontend/style.css] Appliquer font-family: sans-serif. Body avec background-color: #f4f7f6, display: flex, justify-content: center. Cartes avec background: #ffffff, box-shadow: 0 4px 6px rgba(0,0,0,0.1), padding: 20px, margin: 10px, border-radius: 8px.

## Fichiers générés
- `.github/workflows/ci.yml`
- `.gitignore`
- `backend/api.py`
- `backend/modeles.py`
- `backend/requirements.txt`
- `frontend/index.html`
- `frontend/style.css`
- `requirements.txt`
- `tests/test_smoke.py`

## Architecture
```
Voici le plan technique pour le projet de gestion de salles.

### 1. ARBORESCENCE
```text
project_root/
├── backend/
│   ├── __init__.py
│   ├── modeles.py      # Classes Salle et GestionnaireSalles
│   └── api.py          # Serveur FastAPI
└── frontend/
    ├── index.html
    └── style.css
```

### 2. SPECS BACKEND (backend/modeles.py)
```python
class Salle:
    def __init__(self, id_salle: int, nom: str, capacite: int):
        self._id_salle: int = id_salle
        self._nom: str = nom
        self._capacite: int = capacite
        self._est_reservee: bool = False

class GestionnaireSalles:
    def __init__(self):
        self._salles: list[Salle] = []

    def ajouter_salle(self, salle: Salle) -> None:
        pass

    def lister_disponibles(self) -> list[dict]:
        pass

    def 
```

---
*Généré par [TP_maker](https://github.com/) · 2026-05-19*
