###############################################################################
## Jeu Boggle
## Voici une simulation python simplifiée du jeu "Boggle".
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
     "de26":["E", "H", "I", "F", "S", "E"],
     "de27":["T", "L", "I", "B", "R", "A"],
     "de28":["S", "P", "U", "L", "T", "E"],
     "de29":["A", "I", "M", "S", "O", "R"],
     "de30":["E", "N", "H", "R", "I", "S"],
     "de31":["A", "T", "S", "I", "O", "U"],
     "de32":["E", "I", "R", "E", "B", "C"],
     "de33":["S", "P", "U", "L", "T", "E"],
     "de34":["A", "C", "F", "L", "N", "E"],
     "de35":["R", "E", "C", "A", "L", "S"],
     "de36":["E", "N", "T", "D", "O", "S"],
     }

# Déclaration des points par mot selon la taille de la grille (donnés dans l"énoncé)
grille_4x4 = {"3":1,"4":2,"5":3,"6":5,"7":8,"8":10}
grille_5x5 = {"3":1,"4":2,"5":3,"6":4,"7":6,"8":10}
grille_6x6 = {"3":1,"4":2,"5":3,"6":5,"7":7,"8":10,"9":12}

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Déclaration des fonctions internes et calculs 

#Fonction qui prend en input le nombre de manches
def input_manches():
    nombre_manches=""
    while nombre_manches =="" or nombre_manches.isdigit()==False or int(nombre_manches)<1:
        nombre_manches = input("Veuillez entrer le nombre de manches: ").strip()
    return int(nombre_manches)

#Fonction qui prend en input le nombre de joueurs qui jouent
def input_joueurs():
    nombre_joueurs=""
    while nombre_joueurs =="" or nombre_joueurs.isdigit()==False or int(nombre_joueurs)<1:
        nombre_joueurs = input("Veuillez entrer le nombre de joueurs: ").strip()
    return int(nombre_joueurs)

#Fonction qui prend en input les noms des joueurs
def input_noms(nombre_joueurs):
    noms = [None]*nombre_joueurs
    for i in range(nombre_joueurs): 
        noms[i]= input(f"Veuillez entrer le nom du joueur {i+1}: ").strip()
        while noms[i] =="":
            noms[i] = input(f"Le nom ne peut être vide, veuillez entrer un nom valide pour le joueur {i+1}: ").strip()
    return noms

#Fonction qui prend en input la grandeur de la grille
def input_taille_grille():
    while True:
        taille_grille=input("Veuillez choisir une taille de grille (j x j) entre '4', '5' ou '6': ")
        if taille_grille == "4" or taille_grille == "5" or taille_grille == "6" :
            break
    return int(taille_grille)

#Fonction qui crée les statistiques des joueurs
def statistiques(input_noms):
    joueurs = [None]*len(input_noms)
    for i in range(len(input_noms)):
        joueurs[i] = {f"Joueur{i+1}":input_noms[i],"Mots":[],"Statut":[],"Pointage":[],"Total":0}
    return joueurs

#Fonction qui crée une liste de dés de manière aléatoire pour la création de la grille
#Changer le paramètre "taille" pour "input_taille_grille" pour mieux réfléter d'où la variable vient (d'un input)
def generer_grille(input_taille_grille):
    number_of_dices = input_taille_grille**2
    des_liste = []
    while len(des_liste)<number_of_dices:  
        random_number_liste = random.randint(1,number_of_dices)
        random_number_face = random.randint(0,5) 
        if (random_number_liste in des_liste):
            continue
        else:
            des_liste.append(des[f"de{random_number_liste}"][random_number_face])
    des_matrice=[]
    for i in range(input_taille_grille):
        des_sous_matrice=[]
        for j in range(input_taille_grille):
            des_sous_matrice.append(des_liste[input_taille_grille*i+j])
        des_matrice.append(des_sous_matrice)
    return [input_taille_grille,number_of_dices,des_matrice]

#Fonction qui affiche les statistiques des joueurs
def affichage_statistiques(statistiques):
    print("\nVoici les statistiques des joueurs:")
    for i in range(nombre_joueurs):
        print(statistiques[i])

#Fonction qui affiche la grille selon la taille demandée et en utilisant la matrice de dés aléatoires
def affichage_grille(generateur):
    print("\nVoici la grille de jeu:")
    for _ in range(generateur[0]*4):
        print("-",end="")
    print("-")
    for i in generateur[2]:
        for j in i:
            print("|",j,end=" ")
        print("|")
        for _ in range(generateur[0]*4):
            print("-",end="")
        print("-")

#Fonction qui détermine le tour de chaque joueur
def tour_jeu():
    global nombre_tour_counter
    nombre_tour_counter+=1

#Fonction ajoutant le joueur dans la liste d'abandon
def joueur_abandon(noms):
    global joueurs_abandon_matrice
    for i in range(nombre_joueurs):
        if nombre_tour_counter%nombre_joueurs == i :
            joueurs_abandon_matrice.append(noms[i])
            break
    print(f"{noms[i]} a abandonné, il ne peut plus ajouter des mots mais peut encore valider les mots du joueur précédent.")

#Fonction remplaçant les accents
def matching(letter):
    if letter in "éèêëàâùûîïôç" :
        if letter in "éèêë": return "e"
        if letter in "àâ": return "a"
        if letter in "ùû": return "u"
        if letter in "îï": return "i"
        if letter in "ô": return "o"
        if letter in "ç": return "c"
    else : return False

#Fonction qui reçoit les mots de chaque joueurs
def input_joueur_mot(noms):
    global mots_matrice
    global joueurs_abandon_matrice
    for i in range(nombre_joueurs):
        if nombre_tour_counter%nombre_joueurs == i :
            if noms[i] in joueurs_abandon_matrice:
                mot = ""
                return mot
            else:
                mot = input(f"{noms[i]}, veuillez entrer un mot de 3 lettres minimum:\n")
                if mot =="" : return mot
                mot_sans_accent =""
                for k in mot :
                    remplacement = matching(k)
                    if remplacement==False :
                        mot_sans_accent+=k
                    else : 
                        mot_sans_accent+=remplacement
                if mot_sans_accent in mots_matrice : 
                    mot_sans_accent = mot_sans_accent.upper()+" (REPEAT)"
                    return mot_sans_accent
                mots_matrice.append(mot_sans_accent)
    return mot_sans_accent.upper()

#Fonction faisant la transpose de notre matrice de dés (source : Louis-Edouard Lafontant, IFT-1015)
def transpose(matrice):
    matrice_trans = [None] * len(matrice[0])
    for i in range(len(matrice_trans)):
        matrice_trans[i] = []
        for j in range(len(matrice)):
            matrice_trans[i].append(matrice[j][i])
    return matrice_trans   

#Fonction vérifiant si le mot se retrouve dans la grille (remplace la fonction est_valide initiale du devoir)
#Changer les paramètres "grille" par "generateur", mais les fonctions de ces paramètres sont similaires
def est_dans_grille(mot,generateur):
    for i in range(generateur[0]):
        #Joindre la matrice pour les lignes et les lignes en reverse
        matrix_to_string_row = "".join(generateur[2][i])
        matrix_to_string_row_reverse = matrix_to_string_row[::-1]
        #Joindre la matrice pour les colonnes et les colonnes en reverse
        matrix_trans = transpose(generateur[2])
        matrix_to_string_col = "".join(matrix_trans[i])
        matrix_to_string_col_reverse = matrix_to_string_col[::-1]
        #Chercher le mot dans les lignes et colonnes
        find_word_row = matrix_to_string_row.find(mot)
        find_word_row_reverse = matrix_to_string_row_reverse.find(mot)
        find_word_col = matrix_to_string_col.find(mot)
        find_word_col_reverse = matrix_to_string_col_reverse.find(mot)
        if find_word_row == -1 and find_word_col == -1 and find_word_row_reverse  == -1 and find_word_col_reverse == -1:
           continue
        else :
           return True
    return False

#Fonction de vérification de mots par le système (légal ou illégal)
def est_legal(mot):
    mot= mot.strip()
    if mot.endswith("(REPEAT)"):
        affichage_est_legal("REPEAT")
        stats_append(mot,"ILLEGAL",0)
        return False
    if (mot.isalpha()==False or len(mot)<3 or len(mot)>generateur[0]):
        affichage_est_legal(" ")
        stats_append(mot,"ILLEGAL",0)
        return False
    elif est_dans_grille(mot,generateur)==False:
        affichage_est_legal(" ")
        stats_append(mot,"ILLEGAL",0)
        return False
    return True   

def affichage_est_legal(message):
    if message == "REPEAT":
        print("Le mot a déjà été entré par un joueur, vous avez perdu votre tour")
    else:
        print('Le mot est illégal')

#Fonction de vérification des mots par le joueur adverse (valide ou rejeté) (la fonction est_dans_grille sera la fonction est_valide du devoir)
#Nous avons une autre fonction "est_legal" qui va regarder si le mot est legal ou illegal selon les règles du jeu
def est_valide(noms, mot):
    decision = ""
    while (decision != "O" and decision!= "N"):
        for i in range(nombre_joueurs):
            if nombre_tour_counter%nombre_joueurs == nombre_joueurs-1 :
                decision = input(f"{noms[0]}, veuillez dire si le mot de {noms[nombre_joueurs-1]} est valide (O) ou rejeté (N) (O/N):\n").upper()
                break
            elif nombre_tour_counter%nombre_joueurs == i :
                decision = input(f"{noms[i+1]}, veuillez dire si le mot de {noms[i]} est valide (O) ou rejeté (N) (O/N):\n").upper()
                break
    if (decision == "O") :
        return True
    else:
        stats_append(mot,"REJETE",0)
        return False

#Fonction qui va mettre à jour les statistiques des joueurs pendant le jeu
def stats_append(mot,string,pointage):
     for i in range(nombre_joueurs):
        if nombre_tour_counter%nombre_joueurs == i :
            stats[i]["Mots"].append(mot)
            stats[i]["Statut"].append(string)
            stats[i]["Pointage"].append(pointage)
        else:
            continue

#Fonction de calcul des points selon la longueur des mots
#Changer les paramètres "grille" pour seulement inclure le mot et référer à la bonne matrice de points selon la taille de la grille
#Calculons le total dans une autre fonction, nous allons donc tester ces 2 fonctions dans la partie des tests unitaires
def calcul_point(mot,taille_grille):
    longueur_mot = len(mot)
    if longueur_mot <3 : 
        return
    if taille_grille == 4 : 
        return grille_4x4[f"{longueur_mot}"]
    elif taille_grille == 5 : 
        return grille_5x5[f"{longueur_mot}"]
    elif taille_grille == 6 : 
        return grille_6x6[f"{longueur_mot}"]

#Fonction de calcul des points totaux des statistiques de chaque joueur
def calcul_total(nombre_joueurs):
    for i in range(nombre_joueurs):
        stats[i]["Total"]=sum(stats[i]["Pointage"])

#Fonction principale en charge du déroulement du jeu/programme
def jouer():
    global nombre_manches, gagnants_totaux 
    #Affichage de la grille et des statistiques des joueurs
    affichage_statistiques(stats)
    affichage_grille(generateur)
    #Déroulement du jeu : input des joueurs sur les mots (appel aussi à la fonction qui regarde les tours des joueurs)
    while (nombre_tour_counter < nombre_tour_max):
        mot = input_joueur_mot(noms)
        if mot =="":
            joueur_abandon(noms)
            tour_jeu()
            continue
        if (est_legal(mot)==False):
            tour_jeu()
            continue
        elif (est_valide(noms,mot)==False):
            tour_jeu()
            continue
        else:
            points = calcul_point(mot,taille_grille)
            stats_append(mot,"ACCEPTE",points)
            tour_jeu()
    #Calcul des totaux à la fin du jeu
    calcul_total(nombre_joueurs)  
    #Affichage des statistiques de fin de jeu
    affichage_fin_jeu(stats)
    #Traitement de fin de jeu
    nombre_manches-=1
    gagnants_totaux.append(gagnant(stats))
    #Réinitialisation du jeu selon le nombre de manches
    if nombre_manches==0:
        affichage_gagnants_totaux(gagnants_totaux)
        return
    else:
        #Demande si les joueurs veulent continuer de jouer
        decision = input_continue_jouer()
        if decision == True :
            réinitialisation(noms,taille_grille)
            jouer()
        elif decision == False:
            return

#Demander aux joueurs s'ils veulent encore jouer
def input_continue_jouer():
    decision = ""
    while (decision != "O" and decision!= "N"):
        decision = input("Voulez-vous continuer de jouer? (O/N)").upper()
        if decision == "O":
            return True
        elif decision == "N": 
            return False

def affichage_gagnants_totaux(gagnants):
    print(f"Voici la liste des gagnants des manches :{gagnants}")

def gagnant(stats):
    highest_total = 0
    gagnants_manche_matrice = []
    for i in range(nombre_joueurs):
        current_total = stats[i]['Total']
        if current_total>highest_total:
            highest_total = current_total
    if highest_total == 0 :
        return gagnants_manche_matrice
    else:
        for j in range(nombre_joueurs):
            if stats[j]['Total'] == highest_total:
                gagnants_manche_matrice.append(stats[j][f"Joueur{j+1}"])
    return gagnants_manche_matrice

def affichage_fin_jeu(stats):
    for i in range(nombre_joueurs):
        print("\n")
        print(stats[i][f"Joueur{i+1}"])
        print("---------------------------------------")
        for j in range(len(stats[i]["Mots"])):
            mot = stats[i]['Mots'][j]
            space =" "*(16 - len(mot))
            pointage = stats[i]['Pointage'][j]
            if pointage == 0 :
                pointage = "x"
            statut = stats[i]['Statut'][j]
            if statut == "ACCEPTE":
                print(f"- {mot}{space}({pointage})")
            else:
                print(f"- {mot}{space}({pointage}) -- {statut}")
        print("=======================================")
        total = stats[i]["Total"]
        print(f"TOTAL: {total}")
    gagnants = gagnant(stats)   
    if len(gagnants)>1:
        for i in range(len(gagnants)):
            if i == len(gagnants)-1:
                print(f"{gagnants[i]} ",end="")
            else:
                print(f"{gagnants[i]}, ",end="")
        print("ont remporté la partie!")
    elif len(gagnants) == 0 :
        print("\nÉgalité!")
    else: 
        print(f"\n{gagnants[0]} a remporté la partie!")

#Pour réinitialiser une partie lorsque la manche est finie
def réinitialisation(noms,taille_grille):
    global nombre_tour_counter, mots_matrice, joueurs_abandon_matrice,stats,generateur
    nombre_tour_counter = 0
    mots_matrice = []
    joueurs_abandon_matrice = [None]*nombre_joueurs
    stats = statistiques(noms)
    generateur = generer_grille(taille_grille)
    return
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -# 

# Déclaration du code principal et Affichage

#Création des inputs nécessaires (noms et taille de la grille)
nombre_manches = input_manches()
nombre_joueurs = input_joueurs()
noms = input_noms(nombre_joueurs)
taille_grille = input_taille_grille()
#Création du compteur de tours et du nombre de tours maximum se basant sur le nombre de joueurs
nombre_tour_counter = 0
nombre_tour_max = 10*nombre_joueurs
#Initialisation de la matrice de mots déjà entrés,de la matrice d'abandon et de la matrice des gagnants totaux
mots_matrice = []
joueurs_abandon_matrice = [None]*nombre_joueurs
gagnants_totaux=[]
#Création des statistiques des joueurs
stats = statistiques(noms)
#Création du générateur de dés aléatoires
generateur = generer_grille(taille_grille)
#Déroulement du jeu
jouer()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -# 
#################################################################################
# Tests

def test():
#Test pour la fonction generer_grille
#Test 1 : Vérifier que les 2 grilles sont de mêmes dimensions
    def test_generer_grille_1(generer_grille_1, generer_grille_2):
        n = generer_grille_1[0] #Nous sommmes supposés avoir une grille de dimension "n" pour avoir la dimension "nxn"
        m = generer_grille_2[0] #Nous sommmes supposés avoir une grille de dimension "m" pour avoir la dimension "mxm"
        assert n == m , "Échec, les 2 grilles ne sont pas de mêmes dimensions"
                
    test_generer_grille_1(generer_grille(5),generer_grille(5)) #Test pour 2 matrices 5x5

#Test 2 : Vérifier que le nombre de dés est de nxn pour la grille de 2 dimensions
    def test_generer_grille_2(generer_grille):
        n = generer_grille[0]
        assert generer_grille[1] == n**2 , "Échec, le nombre de dés est erroné"
    
    test_generer_grille_2(generer_grille(6)) #Test pour une matrice 6x6, donc nous voulons 36 dés
       
#Test 3 : Vérifier que le tableau de 2 dimensions retourné est bien de dimension nxn (même longueur de matrice et sous-matrice "nxn")
    def test_generer_grille_3(generer_grille):
        n = generer_grille[0]
        assert len(generer_grille[2]) == n , "Échec, la dimension est erronée" #S'assure de la dimension des colonnes de la matrice est bien "n"
        for sous_matrice in generer_grille[2]:
            assert len(sous_matrice) == n , "Échec, la dimension est erronée" #S'assure de la dimension des lignes de la matrice est bien "n"
        return
    
    test_generer_grille_3(generer_grille(5)) #Test pour une matrice 5x5

#Test 4 : Vérifier que 2 appels successifs ne retournent pas la même grille (probabilité très basse)
    def test_generer_grille_4(generer_grille_1, generer_grille_2):
        n = generer_grille_1[0]
        count = 0
        for i in range(n):
            if generer_grille_1[2][i] == generer_grille_2[2][i] :
                count +=1
        assert count != n , "Échec, les 2 grilles sont identiques"
                
    test_generer_grille_4(generer_grille(5),generer_grille(5)) #Test pour 2 matrices 5x5

#Test 5 : Vérifier que les valeurs de la matrice sont des lettres de type string
    def test_generer_grille_5(generer_grille):
        n = generer_grille[0]
        for i in range(n):
            for j in range(n):
                assert isinstance(generer_grille[2][i][j],str), "Échec, il y a des valeurs de type non string dans la grille"

    test_generer_grille_5(generer_grille(6)) #Test pour une matrice 6x6

#Test pour la fonction est_dans_grille (qui équivaut la fonction "est_valide" du devoir)
#Test 1, 2 : Vérifie que la fonction retrouve un mots dans une colonne et dans une ligne
    def test_est_dans_grille_vrai(est_dans_grille):
        assert est_dans_grille, "Échec, le mot est dans la grille mais la fonction renvoie un false" 
#Pour une matrice 4x4
    test_est_dans_grille_vrai(est_dans_grille("dire",[4,16,[["d","v","x","l"],["i","s","e","a"],["r","n","u","a"],["e","s","t","g"]]]))
    test_est_dans_grille_vrai(est_dans_grille("est",[4,16,[["d","v","x","l"],["i","s","e","a"],["r","n","u","a"],["e","s","t","g"]]]))

#Test 3, 4: Vérifie que la fonction renvoie un false pour un mot qui n'est pas dans la grille (en colonne et en ligne)
    def test_est_dans_grille_faux(est_dans_grille):
        assert est_dans_grille == False, "Échec, le mot n'est pas dans la grille mais la fonction le trouve"        
#Pour une matrice 5x5
    test_est_dans_grille_faux(est_dans_grille("lire",[4,16,[["d","v","x","l","p"],["i","s","e","a","e"],["r","n","u","a","j"],["e","s","t","g","r"],["m","f","e","a","k"]]]))
    test_est_dans_grille_faux(est_dans_grille("esx",[4,16,[["d","v","x","l","p"],["i","s","e","a","e"],["r","n","u","a","j"],["e","s","t","g","r"],["m","f","e","a","k"]]]))

#Test 5, 6: Vérifie que la fonction trouve une mot en lisant à l'envers (colonne et ligne)
#Pour une matrice 4x4
    test_est_dans_grille_vrai(est_dans_grille("erid",[4,16,[["d","v","x","l"],["i","s","e","a"],["r","n","u","a"],["e","s","t","g"]]]))
    test_est_dans_grille_vrai(est_dans_grille("tse",[4,16,[["d","v","x","l"],["i","s","e","a"],["r","n","u","a"],["e","s","t","g"]]]))

#Test pour la fonction calcul_point
#Test 1 : Vérifier que le calcul des points sort un integer
    def test_calcul_point_1(calcul_point):
        assert isinstance(calcul_point,int) , "Échec, la fonction retourne un autre type que integer"
        
    test_calcul_point_1(calcul_point("habit",5))

#Test 2 : Vérifier que la valeur des points n'est pas un négatif
    def test_calcul_point_2(calcul_point):
        assert calcul_point>0, "Échec, mauvais calcul des points"

    test_calcul_point_2(calcul_point("oie",5))

#Test 3 : Vérifier que la valeur des points ne dépasse pas 12 points (selon la matrice de points donnée par l'énoncé du devoir)
    def test_calcul_point_3(calcul_point):
        assert calcul_point <=12, "Échec, mauvais calcul des points"

    test_calcul_point_3(calcul_point("oiseau",6))

#Test 4 : Vérifier que si on donne une taille de grille autre que 4, 5 ou 6, la fonction ne calculera pas de point
    def test_calcul_point_4(calcul_point):
        assert calcul_point == None, "Échec, la fonction calcule des points pour une grille de taille autre que 4, 5, 6"

    test_calcul_point_4(calcul_point("oiseaux",7))

#Test 5 : Vérifier que si on donne un mot de moins de 3 lettres, la fonction ne calculera pas de point
    def test_calcul_point_5(calcul_point):
        assert calcul_point == None, "Échec, la fonction calcule des points pour un mot de moins de 3 lettres"

    test_calcul_point_5(calcul_point("le",6))

test()
#################################################################################