# coding: utf-8
#===============imports===============
import class_pion as cp
import class_tour as ct
import class_fou as cf
import class_dame as cd
import class_roi as cr
import class_cavalier as cc
import time

#======constantes et var globale======
COULEURJOUEUR={1:'Blanc', 2:'Noir'}
TRADLETTRENOMBRE={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
TRADNOMBRELETTRE={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}

#===============classes===============
#Classe du plateau (principalement un tableau dans lequel on met des espaces ou des pièces)
class Plateau:
    def __init__(self):
        #on initialise la grille
        self.__grille=[]
        for lignes in range (0,8):
            self.__grille.append([' ',' ',' ',' ',' ',' ',' ',' '])
        
        #on installe les pièces
        for joueur in (0,7):
            if joueur==0:
                couleur='Noir'
                posPions=1
            else:
                couleur='Blanc'
                posPions=6
            self.__grille[joueur][0]=ct.Tour(couleur)
            self.__grille[joueur][1]=cc.Cavalier(couleur)
            self.__grille[joueur][2]=cf.Fou(couleur)
            self.__grille[joueur][3]=cd.Dame(couleur)
            self.__grille[joueur][4]=cr.Roi(couleur)
            self.__grille[joueur][5]=cf.Fou(couleur)
            self.__grille[joueur][6]=cc.Cavalier(couleur)
            self.__grille[joueur][7]=ct.Tour(couleur)
            for case in range (0,8):
                self.__grille[posPions][case]=cp.Pion(couleur)
            
    
    #Grosse fonction qui s'assure que le joueur entre quelque chose de valide (=une case avec une pièce qui lui appartiens)
    #Renvoie des coordonées sous la forme [trad de la lettre en chiffre,coordonnée de la ligne dans le tableau]
    def choixPiece(self, joueur):
        selectionValide=False
        while selectionValide==False:
            selectionValide=True
            print("Quelle pièce voulez vous jouer (entrez votre choix sous la forme a1)")
            choix=input()
            if len(choix)!=2:
                selectionValide=False
                print("Vous avez rentrer trop ou pas assez de caractères")
            else:
                try:
                    if choix[0] not in ['a','b','c','d','e','f','g','h']:
                        selectionValide=False
                        print("La première coordonée doit être une lettre entre a et h.")
                    if int(choix[1])<1 or int(choix[1])>8:
                        selectionValide=False
                        print("Choix hors plateau.")
                    else:
                        if self.__grille[int(choix[1])-1][TRADLETTRENOMBRE[choix[0]]]==' ':
                            selectionValide=False
                            print("Il n'y a rien sur cette case")
                        else:
                            if self.__grille[int(choix[1])-1][TRADLETTRENOMBRE[choix[0]]].getCouleur()!=COULEURJOUEUR[joueur]:
                                selectionValide=False
                                print("Cette pièce ne vous appartiens pas")
                except ValueError:
                    selectionValide=False
                    print("Vous devez entrer une lettre minuscule suivit d'un chiffre")
                except KeyError:
                    selectionValide=False
                    print("Vous devez entrer une lettre minuscule suivit d'un chiffre")
            if selectionValide==False:
                print("\nVous devez rentrer les coordonées de la pièce que vous voulez bouger")
                print("Celle ci doit vous appartenir (les pièces noires sont en gras)")
                print('Exemple de saisie correcte : "a1"')
                print('Appuyez sur une entrer pour continuer')
                input()
                clean()
                print(self)
        return [TRADLETTRENOMBRE[choix[0]],int(choix[1])-1]
    
    #Ne sert qu'à rediriger vers les directions de mouvements des différentes pièces (série de tests)
    #Les fonctions mouvement des pièces ne servent qu'à lister les mouvements qu'elles sont capables de faire
    def mouvementJoueur(self, joueur, coord):
        piece=self.__grille[coord[1]][coord[0]]
        listeMouvementsPossibles=piece.mouvementPiece(self.__grille, coord)
        return self.selectionMouvement(coord, listeMouvementsPossibles)
    

#Grosse fonction qui sert cette fois a s'assurer que l'endroit ou on veut bouger la pièce est valide et entrer
#Avec un bon forma
    def selectionMouvement(self, coords, listeMouvements):
        selectionValide=False
        while selectionValide==False:
            selectionValide=True
            clean()
            print(self)
            print("Où voulez vous déplacer votre pièce? (entrez votre choix sous la forme a1)")
            print("Taper exit permet de déplacer une autre pièce a la place")
            print("Taper help permet de voir la liste des coups jouables et retours permet de retourner a la sélection de pièce")
            choix=input()
            #Debut des tests, c'est long mais nécéssaire pour gérer tout les cas et les erreurs
            if choix=="help":
                if len(listeMouvements)!=0:
                    print("Liste des coups jouables :")
                    for coordonnees in listeMouvements:
                        print(TRADNOMBRELETTRE[coordonnees[0]] + str(coordonnees[1]+1), end='')
                        if listeMouvements.index(coordonnees)!=len(listeMouvements)-1:
                            print(", ", end='')
                    print()
                else:
                    print("Il n'y a aucun coups jouables avec cette pièce je vous conseil de tapper \"exit\".")
                selectionValide=False
                    
            if choix=="exit":
                print("Retours a la selection de la pièce")
                time.sleep(2)
                return False
         
            if len(choix)!=2:
                if choix!="help":
                    selectionValide=False
                    print("Vous avez rentrer trop ou pas assez de caractères")
            else:
                try:
                    if choix[0] not in ['a','b','c','d','e','f','g','h']:
                        selectionValide=False
                        print("La première coordonée doit être une lettre entre a et h.")
                    if int(choix[1])<1 or int(choix[1])>8:
                        selectionValide=False
                        print("Choix hors plateau.")
                    else:
                        if [TRADLETTRENOMBRE[choix[0]], int(choix[1])-1] not in listeMouvements:
                            selectionValide=False
                            print("Vous ne pouvez pas déplacer cette pièce ici")
                except ValueError:
                    selectionValide=False
                    print("Vous devez entrer une lettre minuscule suivit d'un chiffre")
                except KeyError:
                    selectionValide=False
                    print("Vous devez entrer une lettre minuscule suivit d'un chiffre")
            if selectionValide==False:
                if choix!="help":
                    print("\nVous devez rentrer les coordonées de l'endroit ou vous voulez bouger la piece")
                    print("La coordonnée doit être un mouvement valide")
                    print('Exemple de saisie correcte : "a1"')
                print('Appuyez sur une entrer pour continuer')
                input()
        #On bouge les pièces ici
        #(on duplique la pièce sur une autre case en écrasant la pièce potentiellement présente
        #puis on efface le duplicat de la pièce sur la case de départ)
        self.__grille[int(choix[1])-1][TRADLETTRENOMBRE[choix[0]]]=self.__grille[coords[1]][coords[0]]
        self.__grille[coords[1]][coords[0]]=' '
        self.testPromotion([int(choix[1])-1, TRADLETTRENOMBRE[choix[0]]])
        return True
    
    #Fonction de prommotion d'un pion
    def prommotion(self, coords):
        selectionValide=False
        couleur=self.__grille[coords[0]][coords[1]].getCouleur()
        print("Vous avez ammener votre pion jusqu'a la dernière ligne adverse.")
        print("La règle de la prommotion vous oblige a transformer se pion en n'importe quelle autre pièce sauf roi.")
        while selectionValide==False:
            print("Entrez en quel pièce vous voulez transformer votre pions.")
            print("(Dame, Cavalier, Tour, Fou)")
            try:
                selectionValide=True
                piece=input()
                piece=piece.upper()
                if piece=="DAME":
                    self.__grille[coords[0]][coords[1]]=cd.Dame(couleur)
                elif piece=="CAVALIER":
                    self.__grille[coords[0]][coords[1]]=cc.Cavalier(couleur)
                elif piece=="TOUR":
                    self.__grille[coords[0]][coords[1]]=ct.Tour(couleur)
                elif piece=="FOU":
                    self.__grille[coords[0]][coords[1]]=cf.Fou(couleur)
                else:
                    selectionValide=False
                    print("Selection non valide")
            except ValueError:
                selectionValide=False
                print("Selection non valide")


    #Recherche le roi du joueur couleur
    def rechercheRoi(self, couleur):
        for ligne in self.__grille:
            for case in ligne:
                if case!=' ' and case.getNom()=="Roi" and case.getCouleur()==couleur:
                    return True
        return False


    #Test la prommotion d'un pion
    def testPromotion(self, coords):
        if self.__grille[coords[0]][coords[1]].getNom()=="Pion":
            couleur=self.__grille[coords[0]][coords[1]].getCouleur()
            if couleur=="Blanc" and coords[0]==0:
                self.prommotion(coords)
            elif coords[0]==7:
                self.prommotion(coords)


    #redefinition du print() quand on veut afficher le plateau il suffit de faire print(plateau)
    def __str__(self):
        chaine='x a b c d e f g h\n'
        chaine+='- - - - - - - - -\n'
        for ligne in range(0,8):
            chaine+=str(ligne+1)+'|'
            for colone in range (0,8):
                if self.__grille[ligne][colone]==' ':
                    chaine+=' '
                else:
                    chaine+=str(self.__grille[ligne][colone])
                if colone!=7:
                    chaine+=' '
            chaine+='|\n'
        chaine+='- - - - - - - - -'
        return(chaine)

#==============fonctions==============
def clean():
    for i in range(0,50):
        print()