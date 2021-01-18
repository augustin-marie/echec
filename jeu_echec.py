# coding: utf-8
#===============imports===============
import class_plateau
import time

#======constantes et var globale======
COULEURJOUEUR={1:'Blanc', 2:'Noir'}
TRADLETTRENOMBRE={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}

#==============fonctions==============
def tours(plateauJeu):
    joueur=1
    while True:
        print(f"Tour du joueur {joueur}, pour rappel, ces pions sont {COULEURJOUEUR[joueur]}")
        aJouer=False
        while aJouer==False:
            print(plateauJeu)
            aJouer=plateauJeu.mouvementJoueur(joueur, plateauJeu.choixPiece(joueur))
            class_plateau.clean()
        joueur=abs(joueur-3)
        

#Fonction qui gère la partie en général, c'est a dire l'initialisation du plateau, la gestion des tours et l'affichage du gagnant
def partie():
    plateauJeu=class_plateau.Plateau()
    tours(plateauJeu)


#=========programme principal=========
if __name__=="__main__":
    partie()
