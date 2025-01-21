import random


def afficher_plateau(plateau):
    print("  " + " ".join(map(str, range(8))))
    print("  " + "-" * 15)
    for i, ligne in enumerate(plateau):
        print(f"{i}|" + "|".join(ligne) + "|")
    print("  " + "-" * 15 + "\n")


def creer_plateau():
    plateau = [["." for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                if i < 3:
                    plateau[i][j] = "o"  # Pions de l'ordinateur
                elif i > 4:
                    plateau[i][j] = "x"  # Pions du joueur
    return plateau


def mouvements_possibles(plateau, joueur):
    directions = [(-1, -1), (-1, 1)] if joueur == "x" else [(1, -1), (1, 1)]
    captures = []
    mouvements = []

    for i in range(8):
        for j in range(8):
            if plateau[i][j] == joueur:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 8 and 0 <= nj < 8:
                        if plateau[ni][nj] == ".":
                            mouvements.append(((i, j), (ni, nj)))
                        elif plateau[ni][nj] != joueur and plateau[ni][nj] != ".":
                            # Vérifier saut
                            nni, nnj = ni + di, nj + dj
                            if (
                                0 <= nni < 8
                                and 0 <= nnj < 8
                                and plateau[nni][nnj] == "."
                            ):
                                captures.append(((i, j), (nni, nnj), (ni, nj)))
    return captures if captures else mouvements


def effectuer_mouvement(plateau, mouvement):
    if len(mouvement) == 3:  # Capture
        (i, j), (ni, nj), (ci, cj) = mouvement
        plateau[ci][cj] = "."
    else:
        (i, j), (ni, nj) = mouvement
    plateau[ni][nj] = plateau[i][j]
    plateau[i][j] = "."


def jeu():
    plateau = creer_plateau()
    joueur = "x"  # Le joueur commence

    while True:
        afficher_plateau(plateau)

        # Vérifier les mouvements possibles
        mouvements = mouvements_possibles(plateau, joueur)
        if not mouvements:
            if joueur == "x":
                print("Vous avez perdu !")
            else:
                print("Vous avez gagné !")
            break

        if joueur == "x":
            # Tour du joueur
            print(
                "Vos pions sont 'x'. Entrez votre mouvement sous la forme 'ligne,colonne -> ligne,colonne' (par ex. 5,0 -> 4,1):"
            )
            entree = input()
            try:
                deplacement = entree.split("->")
                debut = tuple(map(int, deplacement[0].strip().split(",")))
                fin = tuple(map(int, deplacement[1].strip().split(",")))
                for mvt in mouvements:
                    if len(mvt) == 3 and (debut, fin, mvt[2]) == mvt:
                        effectuer_mouvement(plateau, mvt)
                        joueur = "o"
                        break
                    elif len(mvt) == 2 and (debut, fin) == mvt:
                        effectuer_mouvement(plateau, mvt)
                        joueur = "o"
                        break
                else:
                    print("Mouvement invalide. Réessayez.")
            except Exception:
                print("Format invalide. Réessayez.")
        else:
            # Tour de l'ordinateur
            print("Tour de l'ordinateur...")
            mouvement = random.choice(mouvements)
            effectuer_mouvement(plateau, mouvement)
            joueur = "x"


jeu()
