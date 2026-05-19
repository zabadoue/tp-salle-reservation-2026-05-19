from typing import List, Optional
from .modeles import Salle

class GestionnaireSalles:
    def __init__(self) -> None:
        self._salles: List[Salle] = []

    def ajouter_salle(self, salle: Salle) -> None:
        """Ajoute une instance de Salle au gestionnaire."""
        self._salles.append(salle)

    def lister_salles_disponibles(self) -> List[Salle]:
        """Retourne la liste des salles dont l'attribut est_reservee est False."""
        return [salle for salle in self._salles if not salle.est_reservee]

    def reserver_salle(self, id_salle: int) -> bool:
        """
        Recherche une salle par son ID et tente de la réserver.
        Retourne True si la réservation a réussi, False sinon.
        """
        for salle in self._salles:
            if salle.id_salle == id_salle:
                if not salle.est_reservee:
                    salle.reserver()
                    return True
                break
        return False