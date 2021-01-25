# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Tour(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Tour')
    
    def mouvementPiece(self, grille, coord):
        choix=[]
        #On vérifie les 4 lignes/colones en prenant toutes les cases jusqu'à ce qu'on tombe sur les bords du plateau ou une pièce
        #Si la pièce appartiens a l'adversaire, on rajoute sa case dans les déplacement possible


        #ligne +
        ligne=coord[1]
        while ligne<7 and grille[ligne+1][coord[0]]==' ':
            ligne+=1
            choix.append([coord[0], ligne])

        if ligne!=7:
            if self.getCouleur()!=grille[ligne+1][coord[0]].getCouleur():
                choix.append([coord[0], ligne+1])

        #ligne -
        ligne=coord[1]
        while ligne>0 and grille[ligne-1][coord[0]]==' ':
            ligne-=1
            choix.append([coord[0], ligne])

        if ligne!=0:
            if self.getCouleur()!=grille[ligne-1][coord[0]].getCouleur():
                choix.append([coord[0], ligne-1])

        #colone +
        colone=coord[0]
        while colone<7 and grille[coord[1]][colone+1]==' ':
            colone+=1
            choix.append([colone, coord[1]])

        if colone!=7:
            if self.getCouleur()!=grille[coord[1]][colone+1].getCouleur():
                choix.append([colone+1, coord[1]])

        #colone -
        colone=coord[0]
        while colone>0 and grille[coord[1]][colone-1]==' ':
            colone-=1
            choix.append([colone, coord[1]])

        if colone!=0:
            if self.getCouleur()!=grille[coord[1]][colone-1].getCouleur():
                choix.append([colone-1, coord[1]])

        return choix
