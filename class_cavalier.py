# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Cavalier(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Cavalier')
    
    def mouvementPiece(self, grille, coord):
        choix=[]

        for chgmtLigne in (-2,2):
            for chgmtColone in (-1,1):
                if coord[0]+chgmtLigne<=7 and coord[0]+chgmtLigne>=0:
                    if coord[1]+chgmtColone<=7 and coord[1]+chgmtColone>=0:
                        if chgmtColone!=0 or chgmtLigne!=0:
                            choix.append([coord[1]+chgmtColone,coord[0]+chgmtLigne])
        
        for chgmtLigne in (-1,1):
            for chgmtColone in (-2,2):
                if coord[0]+chgmtLigne<=7 and coord[0]+chgmtLigne>=0:
                    if coord[1]+chgmtColone<=7 and coord[1]+chgmtColone>=0:
                        if chgmtColone!=0 or chgmtLigne!=0:
                            choix.append([coord[1]+chgmtColone,coord[0]+chgmtLigne])

        return choix
