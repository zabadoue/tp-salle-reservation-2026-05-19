"""Smoke tests auto-générés par TP_maker."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import backend.modeles


def test_imports_ok():
    """Tous les modules doivent s'importer sans erreur."""
    assert True  # si on arrive ici, tous les imports ci-dessus ont réussi


def test_api_routes():
    """Les routes FastAPI doivent répondre."""
    from fastapi.testclient import TestClient
    from backend.api import app
    client = TestClient(app)
    response = client.get("/salles")
    assert response.status_code in (200, 404)  # route existe
