# tp-python-backend-crer-la-classe-salle-a-2026-05-19

> Projet généré automatiquement par **TP_maker** — Usine Logicielle Multi-Agents IA

## Stack
- **Langage principal** : Python (Backend) et HTML/CSS (Frontend)
- **Généré le** : 2026-05-19

## Tâches implémentées
- BACKEND : Créer la classe Salle avec les attributs id_salle, nom, capacite et est_reservee
- BACKEND : Créer la classe GestionnaireSalles avec des methodes pour ajouter une salle, lister les salles disponibles, et reserver une salle par son id
- BACKEND : Créer le serveur FastAPI (backend/api.py) avec les endpoints REST et la configuration CORS
- [FRONTEND] Creer le fichier index.html principal qui affiche le titre de l'application et la structure de base (div conteneurs)
- [FRONTEND] Creer le fichier style.css pour rendre l'interface esthetique (couleurs, ombres, flexbox)

## Fichiers générés
- `backend/api.py`
- `backend/modeles.py`
- `frontend/index.html`
- `frontend/style.css`

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
