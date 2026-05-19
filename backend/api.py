from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from modeles import GestionnaireSalles, Salle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

gestionnaire = GestionnaireSalles()
gestionnaire.ajouter_salle(Salle(1, "Salle A", 10))
gestionnaire.ajouter_salle(Salle(2, "Salle B", 20))

@app.get("/salles")
async def get_salles() -> list[dict]:
    return gestionnaire.lister_disponibles()

@app.post("/reserver/{id_salle}")
async def reserver(id_salle: int) -> dict:
    succes = gestionnaire.reserver_salle(id_salle)
    if not succes:
        raise HTTPException(status_code=400, detail="Salle non disponible")
    return {"success": True}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)