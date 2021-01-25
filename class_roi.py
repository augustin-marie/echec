# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Roi(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Roi')
    
    def mouvementPiece(self, grille, coord):
        choix=[]

        for chgmtLigne in range (-1,2):
            for chgmtColone in range (-1,2):
                if coord[0]+chgmtLigne<=7 and coord[0]+chgmtLigne>=0 and coord[1]+chgmtColone<=7 and coord[1]+chgmtColone>=0:
                    if chgmtColone!=0 or chgmtLigne!=0:
                        if grille[coord[1]+chgmtColone][coord[0]+chgmtLigne]==' ' or self.getCouleur()!=grille[coord[1]+chgmtColone][coord[0]+chgmtLigne].getCouleur():
                            choix.append([coord[0]+chgmtLigne, coord[1]+chgmtColone])
        
        return choix
