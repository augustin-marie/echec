# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Fou(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Fou')


    def mouvementPiece(self, grille, coord):
        choix=[]
        #On vérifie les 4 diagonales en prenant toutes les cases jusqu'à ce qu'on tombe sur les bords du plateau ou une pièce
        #Si la pièce appartiens a l'adversaire, on rajoute sa case dans les déplacement possible

        #Diagonale +ligne +colone
        ligne=coord[1]
        colone=coord[0]
        while ligne<7 and colone<7 and grille[ligne+1][colone+1]==' ':
            ligne+=1
            colone+=1
            choix.append([colone, ligne])

        if ligne<7 and colone<7 and grille[ligne+1][colone+1].getCouleur()!=self.getCouleur():
            choix.append([colone+1, ligne+1])


        #Diagonale -ligne -colone
        ligne=coord[1]
        colone=coord[0]
        while ligne>0 and colone>0 and grille[ligne-1][colone-1]==' ':
            ligne-=1
            colone-=1
            choix.append([colone, ligne])

        if ligne>0 and colone>0 and grille[ligne-1][colone-1].getCouleur()!=self.getCouleur():
            choix.append([colone-1, ligne-1])


        #Diagonale +ligne -colone
        ligne=coord[1]
        colone=coord[0]
        while ligne<7 and colone>0 and grille[ligne+1][colone-1]==' ':
            ligne+=1
            colone-=1
            choix.append([colone, ligne])

        if ligne<7 and colone>0 and grille[ligne+1][colone-1].getCouleur()!=self.getCouleur():
            choix.append([colone-1, ligne+1])


        #Diagonale -ligne +colone
        ligne=coord[1]
        colone=coord[0]
        while ligne>0 and colone<7 and grille[ligne-1][colone+1]==' ':
            ligne-=1
            colone+=1
            choix.append([colone, ligne])

        if ligne>0 and colone<7 and grille[ligne-1][colone+1].getCouleur()!=self.getCouleur():
            choix.append([colone+1, ligne-1])

        return choix