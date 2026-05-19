# tp-python (backend) et html/css (frontend)-backend-crer-la-classe-salle-a-2026-05-19

> Projet généré automatiquement par **TP_maker** — Usine Logicielle Multi-Agents IA

## Stack
- **Langage principal** : Python (Backend) et HTML/CSS (Frontend)
- **Généré le** : 2026-05-19

## Tâches implémentées
- BACKEND : Créer la classe Salle avec les attributs id_salle, nom, capacite et est_reservee.
- BACKEND : Créer la classe GestionnaireSalles avec des méthodes pour ajouter une salle, lister les salles disponibles, et réserver une salle par son id.
- FRONTEND : Créer le fichier index.html principal qui affiche le titre de l'application et la structure de base (div conteneurs).
- FRONTEND : Créer le fichier style.css pour rendre l'interface esthétique (couleurs, ombres, flexbox).

## Fichiers générés
- `backend/gestionnaire.py`
- `frontend/index.html`
- `frontend/style.css`

## Architecture
```
Voici le plan technique structuré pour le projet de gestion de salles.

### 1. ARBORESCENCE
```text
project_root/
├── backend/
│   ├── __init__.py
│   └── gestionnaire.py
├── frontend/
│   ├── index.html
│   └── style.css
└── main.py (Point d'entrée API/Interface)
```

### 2. SPECS BACKEND (`backend/gestionnaire.py`)
L'encapsulation est assurée par des propriétés `@property` pour l'accès aux attributs privés.

```python
from typing import List, Optional

class Salle:
    def __init__(self, id_salle: int, nom: str, capacite: int):
        self._id_salle: int = id_salle
        self._nom: str = nom
        self._capacite: int = capacite
        self._est_reservee: bool = False

    # Getters et Setters via propriétés
    @property
    def id_salle(self) -> int: return self._id_salle

    @pr
```

---
*Généré par [TP_maker](https://github.com/) · 2026-05-19*
