###############################################################################
## Jeu Boggle
## Voici une simulation python simplifiée du jeu "Boggle" pour 2 joueurs.
## Le jeu consiste à trouver des mots jusqu`à un maximum de 10 mots
## Le pointage est calculé selon la taille de ces mots.
## Un mot est valide s'il est composé de minimum 3 lettres adjacentes sur une même ligne ou colonne.
###############################################################################
## Auteur: Maude Farmer et Casta Ung
## Copyright: 2023, Boggle
## Version: #1
## Date: 2023-03-26
###############################################################################

# Aucun import car le jeu est assez simple

# Déclaration des variables globales, constantes

# Déclaration des dés sous forme de dictionnaire (donnés dans l"énoncé)
des={"de1":["E", "T", "U", "K", "N", "O"],
     "de2":["E", "V", "G", "T", "I", "N"],
     "de3":["D", "E", "C", "A", "M", "P"],
     "de4":["I", "E", "L", "R", "U", "W"],
     "de5":["E", "H", "I", "F", "S", "E"],
     "de6":["R", "E", "C", "A", "L", "S"],
     "de7":["E", "N", "T", "D", "O", "S"],
     "de8":["O", "F", "X", "R", "I", "A"],
     "de9":["N", "A", "V", "E", "D", "Z"],
     "de10":["E", "I", "O", "A", "T", "A"],
     "de11":["G", "L", "E", "N", "Y", "U"],
     "de12":["B", "M", "A", "Q", "J", "O"],
     "de13":["T", "L", "I", "B", "R", "A"],
     "de14":["S", "P", "U", "L", "T", "E"],
     "de15":["A", "I", "M", "S", "O", "R"],
     "de16":["E", "N", "H", "R", "I", "S"],
     "de17":["A", "T", "S", "I", "O", "U"],
     "de18":["W", "I", "R", "E", "B", "C"],
     "de19":["Q", "D", "A", "H", "A", "U"],
     "de20":["A", "C", "F", "L", "N", "E"],
     "de21":["P", "R", "S", "T", "U", "G"],
     "de22":["J", "P", "R", "X", "E", "Z"],
     "de23":["E", "K", "V", "Y", "B", "E"],
     "de24":["A", "L", "C", "H", "E", "M"],
     "de25":["E", "D", "U", "F", "H", "K"],
     }

# Déclaration des fonctions internes et calculs 
# avec commentaires détaillés nécessaires seulement (optionnel)

#Fonction qui va prendre en valeur les noms des 2 joueurs et la grandeur de la grille
def inputjeu():
    name1=input("Veuillez entrez le nom du joueur 1: ")
    while name1 =="":
        name1=input("Le nom ne peut être vide, veuillez entrer un nom valide pour le joueur 1: ")
    name2=input("Veuillez entrez le nom du joueur 2: ")
    while name2 =="":
        name2=input("Le nom ne peut être vide, veuillez entrer un nom valide pour le joueur 2: ")
    name = {"name1":name1,"name2":name2}

    while True:
        grille=input("Veuillez choisir une taille de grille entre 4x4, 5x5 ou 6x6: ")
        if grille == "4x4" or grille == "5x5" or grille == "6x6" :
            break

    userinput = [name,grille]
    return userinput

# Déclaration du code principal et Affichage

def generer_grille(taille):
    if taille == "4x4":
        print('4x4')
        return
    elif taille == "5x5":
        print('5x5')
        return
    elif taille == "6x6":
        print('6x6')
        return
    
print(inputjeu())

# generateur = generer_grille(inputjeu())



def jouer():
    return
    
def est_valide(grille, mot):
    return

def calcul_point(grille, mots):
    return

#################################################################################
# Tests
def test() :
    return
#################################################################################