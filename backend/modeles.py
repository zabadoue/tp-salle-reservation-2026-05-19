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

    @est_reservee.setter
    def est_reservee(self, valeur: bool) -> None:
        self._est_reservee = valeur

    def to_dict(self) -> dict:
        return {
            "id_salle": self._id_salle,
            "nom": self._nom,
            "capacite": self._capacite,
            "est_reservee": self._est_reservee
        }

class GestionnaireSalles:
    def __init__(self):
        self._salles: list[Salle] = []

    def ajouter_salle(self, salle: Salle) -> None:
        self._salles.append(salle)

    def lister_disponibles(self) -> list[dict]:
        return [s.to_dict() for s in self._salles if not s.est_reservee]

    def reserver_salle(self, id_salle: int) -> bool:
        for salle in self._salles:
            if salle.id_salle == id_salle and not salle.est_reservee:
                salle.est_reservee = True
                return True
        return False