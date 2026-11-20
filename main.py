"""Jouer aux dames à deux dans le terminal : chaque joueur tape son coup, comme c3 d4."""
from dames import Partie
from exceptions import ErreurDames


def lire_coup(texte: str) -> tuple[str, str]:
    """« c3 d4 », « c3-d4 » ou « d4xf6 » donnent ("c3", "d4"). Sinon ValueError."""
    cases = texte.replace("-", " ").replace("x", " ").split()
    if len(cases) != 2:
        raise ValueError("tapez deux cases, par exemple c3 d4")
    depart, arrivee = cases
    return depart, arrivee


def main() -> int:
    partie = Partie()
    print(partie.plateau)
    while (gagnant := partie.gagnant) is None:
        texte = input(f"{partie.trait} > ").strip()
        if texte == "quitter":
            print("Partie abandonnée.")
            return 0
        try:
            depart, arrivee = lire_coup(texte)
            coup = partie.jouer(depart, arrivee)
        except (ErreurDames, ValueError) as erreur:
            print(f"Refusé : {erreur}")
            continue
        print(coup)
        print(partie.plateau)

    print(f"Les {gagnant}s gagnent !")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
