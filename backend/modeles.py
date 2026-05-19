class Salle:
    def __init__(self, id_salle: int, nom: str, capacite: int, est_reservee: bool = False):
        self._id_salle: int = id_salle
        self._nom: str = nom
        self._capacite: int = capacite
        self._est_reservee: bool = est_reservee

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
        if not self._est_reservee:
            self._est_reservee = True
        else:
            raise ValueError(f"La salle {self._nom} est déjà réservée.")