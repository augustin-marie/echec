# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Tour(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Tour')
        self.__dejaBouger=False
    
    def mouvementPiece(self, grille, coord):
        choix=[]
        ligne=coord[1]
        while ligne<7 and grille[ligne+1][coord[0]]==' ':
            choix.append([coord[0], ligne+1])
            ligne+=1

        if ligne!=7:
            choix.append([coord[0], ligne+1])


        ligne=coord[1]
        while ligne>0 and grille[ligne-1][coord[0]]==' ':
            choix.append([coord[0], ligne-1])
            ligne-=1

        if ligne!=0:
            choix.append([coord[0], ligne-1])


        colone=coord[0]
        while colone<7 and grille[coord[1]][colone+1]==' ':
            choix.append([colone+1, coord[1]])
            colone+=1

        if colone!=7:
            choix.append([colone+1, coord[1]])


        colone=coord[0]
        while colone>0 and grille[coord[1]][colone-1]==' ':
            choix.append([colone+1, coord[1]])
            colone-=1

        if colone!=0:
            choix.append([colone-1, coord[1]])

        
        if choix!=[]:
            self.__dejaBouger=True

        return choix

#le aDejaBouger sert a programmer le rock pour pas qu'on puisse retourner a la pos de départ et que sa marche
#même si on a déjà bouger