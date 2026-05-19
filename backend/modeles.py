class Salle:
    def __init__(self, id_salle: int, nom: str, capacite: int) -> None:
        self._id_salle: int = id_salle
        self._nom: str = nom
        self._capacite: int = capacite
        self._est_reservee: bool = False

    @property
    def id_salle(self) -> int:
        return self._id_salle

    @property
    def est_reservee(self) -> bool:
        return self._est_reservee

    def reserver(self) -> None:
        self._est_reservee = True

    def to_dict(self) -> dict:
        return {
            "id": self._id_salle,
            "nom": self._nom,
            "capacite": self._capacite
        }

class GestionnaireSalles:
    def __init__(self) -> None:
        self._salles: list[Salle] = []
        # Initialisation avec quelques données par défaut pour test
        self.ajouter_salle(Salle(1, "Salle A", 10))
        self.ajouter_salle(Salle(2, "Salle B", 20))

    def ajouter_salle(self, salle: Salle) -> None:
        self._salles.append(salle)

    def lister_disponibles(self) -> list[dict]:
        return [s.to_dict() for s in self._salles if not s.est_reservee]

    def reserver_salle(self, id_salle: int) -> bool:
        for salle in self._salles:
            if salle.id_salle == id_salle and not salle.est_reservee:
                salle.reserver()
                return True
        return False