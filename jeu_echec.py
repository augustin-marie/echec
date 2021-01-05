# coding: utf-8
#===============imports===============

#======constantes et var globale======

#===============classes===============
class Piece:
    def __init__(self,c,nom):
        self.__couleur=c
        self.__nom=nom
        self.__caractere=nom[0]
    
    def __repr__(self):
        if self.__couleur=='Noir':
            return(gras(self.__caractere))
        else:
            return(self.__caractere)

class Pion(Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Pion')

class Tour(Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Tour')

class Cavalier(Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Cavalier')

class Fou(Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Fou')

class Dame(Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Dame')

class Roi(Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Roi')

class Plateau:
    def __init__(self):
        self.grille=[]
        for lignes in range (0,8):
            self.grille.append([' ',' ',' ',' ',' ',' ',' ',' '])
        
        for joueur in (0,7):
            if joueur==0:
                couleur='Noir'
                posPions=1
            else:
                couleur='Blanc'
                posPions=6
            self.grille[joueur][0]=Tour(couleur)
            self.grille[joueur][1]=Cavalier(couleur)
            self.grille[joueur][2]=Fou(couleur)
            self.grille[joueur][3]=Roi(couleur)
            self.grille[joueur][4]=Dame(couleur)
            self.grille[joueur][5]=Fou(couleur)
            self.grille[joueur][6]=Cavalier(couleur)
            self.grille[joueur][7]=Tour(couleur)
            for case in range (0,8):
                self.grille[posPions][case]=Pion(couleur)
        
    def __str__(self):
        return str(self.grille)


#==============fonctions==============
def gras(text):
    return '\033[1m'+text+'\033[0m'

def partie():
    plateauJeu=Plateau()
    print(plateauJeu)


#=========programme principal=========
if __name__=="__main__":
    partie()


