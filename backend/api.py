from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from modeles import GestionnaireSalles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

gestionnaire = GestionnaireSalles()

@app.get("/salles")
def get_salles() -> list[dict]:
    return gestionnaire.lister_disponibles()

@app.post("/reserver/{id_salle}")
def reserver(id_salle: int) -> dict:
    succes: bool = gestionnaire.reserver_salle(id_salle)
    return {"success": succes}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)