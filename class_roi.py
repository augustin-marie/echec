# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Roi(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Roi')
        self.__dejaBouger=False
    
    def mouvementPiece(self, grille, coord):
        choix=[]

        for chgmtLigne in range (-1,2):
            for chgmtColone in range (-1,2):
                if coord[0]+chgmtLigne<=7 and coord[0]+chgmtLigne>=0:
                    if coord[1]+chgmtColone<=7 and coord[1]+chgmtColone>=0:
                        if chgmtColone!=0 or chgmtLigne!=0:
                            choix.append([coord[1]+chgmtColone,coord[0]+chgmtLigne])
        
        if choix!=[]:
            self.__dejaBouger=True
        
        return choix


#le aDejaBouger sert a programmer le rock pour pas qu'on puisse retourner a la pos de départ et que sa marche
#même si on a déjà bouger