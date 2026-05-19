# tp-python-backendbackendmodelespy-dfinir-2026-05-19

> Projet généré automatiquement par **TP_maker** — Usine Logicielle Multi-Agents IA

## Stack
- **Langage principal** : Python (Backend) et HTML/CSS (Frontend)
- **Généré le** : 2026-05-19

## Tâches implémentées
- [BACKEND:backend/modeles.py] Définir la classe Salle avec les attributs privés : _id_salle: int, _nom: str, _capacite: int, _est_reservee: bool. Ajouter un constructeur __init__(self, id_salle: int, nom: str, capacite: int). Définir la classe GestionnaireSalles avec l'attribut privé _salles: list[Salle]. Méthodes : ajouter_salle(self, salle: Salle) -> None, lister_disponibles(self) -> list[dict] (retourne une liste de dictionnaires avec id, nom, capacite), reserver_salle(self, id_salle: int) -> bool (met à jour _est_reservee à True si trouvée et non réservée).
- [BACKEND:backend/api.py] Initialiser FastAPI avec CORSMiddleware (allow_origins=['*']). Instancier globalement GestionnaireSalles. Route GET '/salles' -> retourne list[dict] via gestionnaire.lister_disponibles(). Route POST '/reserver/{id_salle}' -> retourne dict {'success': bool} via gestionnaire.reserver_salle(id_salle). Configurer uvicorn pour écouter sur 0.0.0.0:8000.
- [BACKEND:requirements.txt] Contenu du fichier : fastapi, uvicorn[standard].
- [FRONTEND:frontend/index.html] Structure HTML5 avec un <header> contenant un titre. Un conteneur <main id='app'> pour l'injection dynamique. Inclure un bloc <script> : au chargement, fetch('http://localhost:8000/salles') pour générer des cartes HTML (div avec classe 'card') pour chaque salle. Chaque carte contient le nom, la capacité et un bouton avec id='btn-{id_salle}' qui déclenche un fetch('http://localhost:8000/reserver/' + id, {method: 'POST'}) et rafraîchit la liste.
- [FRONTEND:frontend/style.css] Appliquer un fond #f4f7f6. Utiliser Flexbox sur le body pour centrer un conteneur principal avec max-width: 800px. Définir la classe .card avec background: #ffffff, padding: 20px, margin: 10px, border-radius: 8px, box-shadow: 0 2px 5px rgba(0,0,0,0.1). Appliquer la couleur #3498db pour les boutons.

## Fichiers générés
- `.github/workflows/ci.yml`
- `.gitignore`
- `backend/api.py`
- `backend/modeles.py`
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
├── frontend/
│   ├── index.html
│   └── style.css
└── requirements.txt
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
 
```

---
*Généré par [TP_maker](https://github.com/) · 2026-05-19*
