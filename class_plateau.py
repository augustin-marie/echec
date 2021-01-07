# coding: utf-8
#===============imports===============
import class_pion as cp
import class_tour as ct
import class_fou as cf
import class_dame as cd
import class_roi as cr
import class_cavalier as cc

#======constantes et var globale======
COULEURJOUEUR={1:'Blanc', 2:'Noir'}
TRADLETTRENOMBRE={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}

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
            self.__grille[joueur][3]=cr.Roi(couleur)
            self.__grille[joueur][4]=cd.Dame(couleur)
            self.__grille[joueur][5]=cf.Fou(couleur)
            self.__grille[joueur][6]=cc.Cavalier(couleur)
            self.__grille[joueur][7]=ct.Tour(couleur)
            for case in range (0,8):
                self.__grille[posPions][case]=cp.Pion(couleur)
    
    #Grosse fonction qui s'assure que le joueur entre quelque chose de valide (=une case avec une pièce qui lui appartiens)
    #Important, il faudra rajouter le test "cette pièce peut bouger" ou donner la possibilité de changer de pièces sinon garre au soft block
    #Renvoie des coordonées sous la forme [,]
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
                print(self)
        return [TRADLETTRENOMBRE[choix[0]],int(choix[1])-1]
    
    #Ne sert qu'à rediriger vers les directions de mouvements des différentes pièces (série de tests)
    def choixMouvement(self, coord):
        piece=self.__grille[coord[1]][coord[0]]
        piece.mouvementPiece(self.__grille, coord)



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

