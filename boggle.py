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

# Déclaration des imports et dépendances
import random

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -# 

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

#Déclaration d'un "flag" pour décider le tour de chaque joueur
tour_joueur_cle = True

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Déclaration des fonctions internes et calculs 

#Fonction qui prend en input les noms des 2 joueurs et la grandeur de la grille
def input_noms():
    name1 = input("Veuillez entrer le nom du joueur 1: ").strip()
    while name1 =="":
        name1 = input("Le nom ne peut être vide, veuillez entrer un nom valide pour le joueur 1: ").strip()
    name2 =input("Veuillez entrer le nom du joueur 2: ").strip()
    while name2 =="":
        name2 = input("Le nom ne peut être vide, veuillez entrer un nom valide pour le joueur 2: ").strip()
    return [name1,name2]

#Fonction qui prend en input la grandeur de la grille
def input_taille_grille():
    while True:
        taille_grille=input("Veuillez choisir une taille de grille (j x j) entre '4', '5' ou '6': ")
        if taille_grille == "4" or taille_grille == "5" or taille_grille == "6" :
            break
    return int(taille_grille)

#Fonction qui crée les statistiques des joueurs
def statistiques(input_noms):
    joueur1 = {"Joueur1":input_noms[0],"Mots":{},"Statut":{},"Pointage":{},"Total":0}
    joueur2 = {"Joueur2":input_noms[1],"Mots":{},"Statut":{},"Pointage":{},"Total":0}
    joueurs = [joueur1, joueur2]
    return joueurs

#Fonction qui crée une liste de dés de manière aléatoire pour la création de la grille 
def generer_grille(input_taille_grille):
    if (input_taille_grille== 4):
        number_of_dices = 16
    elif (input_taille_grille== 5):
        number_of_dices = 25
    elif (input_taille_grille== 6):
        number_of_dices = 36
    des_liste = []
    while len(des_liste)<number_of_dices:  
        random_number_liste = random.randint(1,number_of_dices)
        random_number_face = random.randint(0,5) 
        if (random_number_liste in des_liste):
            continue
        else:
            des_liste.append(des[f"de{random_number_liste}"][random_number_face])
    return [input_taille_grille,number_of_dices,des_liste]

#Fonction qui affiche les statistiques des joueurs
def affichage_statistiques(statistiques):
    print(f"\nVoici les statistiques de départ des joueurs:\n{statistiques[0]}\n{statistiques[1]}\n")

#Fonction qui affiche la grille selon la taille demandée et en utilisant les dés "randomized"
def affichage_grille(generateur):
    print("Voici la grille de jeu:")
    for j in range((generateur[0]*4)+1):
                if (j==generateur[0]*4):
                    print("-")
                else:
                    print("-",end="")
    for i in range(1,generateur[1]+1):
        if (i%generateur[0]==1):
            print("|",generateur[2][i-1],"|",end=" ")
        elif (i%generateur[0]==0):
            print(generateur[2][i-1],"|")
            for j in range((generateur[0]*4)+1):
                if (j==generateur[0]*4):
                    print("-")
                else:
                    print("-",end="")
        else:
            print(generateur[2][i-1],"|",end=" ")

#Fonction qui détermine le tour de chaque joueur
def tour_jeu():
    global tour_joueur_cle
    if (tour_joueur_cle == True):
        tour_joueur_cle = False
    else:
        tour_joueur_cle = True
    return tour_joueur_cle

#Fonction qui reçoit les mots de chaque joueurs
def input_joueur_mot(noms):
    tour_joueur = tour_jeu()
    if (tour_joueur == False) :
        mot = input(f"{noms[0]}, veuillez entrer un mot de 3 lettres minimum:\n")
    else:
        mot = input(f"{noms[1]}, veuillez entrer un mot de 3 lettres minimum:\n")
    return mot

#Fonction de vérification de mots par le système (légal ou illégal)
def est_illegal():
    return

#Fonction de vérification des mots par le joueur adverse (valide ou rejeté)
def est_valide(noms, mot):
    decision = ""
    while (decision != "o" and decision!= "n"):
        if (tour_joueur_cle == True) :
            decision = input(f"{noms[0]}, veuillez dire si le mot de {noms[1]} est valide ou rejeté (o/n):\n")
        else:
            decision = input(f"{noms[1]}, veuillez dire si le mot de {noms[0]} est valide ou rejeté (o/n):\n")
    # if (decision == "o") :
        
    return decision
#Si validé = Mot noté et indiqué comme accepté dans le dictionnaire des mots du joueur, ensuite appeler la fct calcul_point #
#Si refusé = Mot noté et indiqué comme refusé dans le dictionnaire des mots du joueur#  


#Fonction qui va mettre à jour les statistiques des joueurs pendant le jeu
def stats_append():
    return


def mot_verif():
    return
            #A ajouter:#
            #Variables requises: mot, joueur dont le tour est en cours, autre joueur#
            #Insérer un input de la part du joueur pour validation ou refus du mot retenu.# 

#Fonction de calcul des points de chaque joueur
def calcul_point(grille, mots):
    return
#VA CALCULER LES POINTS en regardant les stats des joueurs

#Fonction principale en charge du déroulement du jeu/programme
def jouer():
    #Création des inputs nécessaires
    noms = input_noms()
    taille_grille = input_taille_grille()
    #Création des statistiques des joueurs
    stats = statistiques(noms)
    #Création du générateur de dés aléatoires
    generateur = generer_grille(taille_grille)
    #Affichage de la grille et des statistiques des joueurs
    affichage_statistiques(stats)
    affichage_grille(generateur)
    #Déroulement du jeu : input des joueurs sur les mots (appel aussi la fonction qui regarde les tours des joueurs)
    mot = 'ift'
    while mot !="":
        mot = input_joueur_mot(noms)
        est_valide(noms,mot)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -# 

# Déclaration du code principal et Affichage
jouer()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -# 

#################################################################################
# Tests
def test() :
    return
#################################################################################
