from typing import List

class Salle:
    def __init__(self, id_salle: int, nom: str, capacite: int):
        self._id_salle: int = id_salle
        self._nom: str = nom
        self._capacite: int = capacite
        self._est_reservee: bool = False

    @property
    def id_salle(self) -> int:
        return self._id_salle

    @property
    def nom(self) -> str:
        return self._nom

    @property
    def capacite(self) -> int:
        return self._capacite

    @property
    def est_reservee(self) -> bool:
        return self._est_reservee

    def reserver(self) -> None:
        self._est_reservee = True

class GestionnaireSalles:
    def __init__(self):
        self._salles: List[Salle] = []

    def ajouter_salle(self, salle: Salle) -> None:
        self._salles.append(salle)

    def lister_disponibles(self) -> List[Salle]:
        return [salle for salle in self._salles if not salle.est_reservee]

    def reserver_salle(self, id_salle: int) -> bool:
        for salle in self._salles:
            if salle.id_salle == id_salle:
                if not salle.est_reservee:
                    salle.reserver()
                    return True
        return False