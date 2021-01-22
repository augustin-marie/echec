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
                if coord[0]+chgmtLigne<=7 and coord[0]+chgmtLigne>=0 and coord[1]+chgmtColone<=7 and coord[1]+chgmtColone>=0:
                    if grille[coord[1]+chgmtColone][coord[0]+chgmtLigne]==' ' or grille[coord[1]+chgmtColone][coord[0]+chgmtLigne].getCouleur()!=self.getCouleur():
                        choix.append([coord[0]+chgmtLigne, coord[1]+chgmtColone])
        
        for chgmtLigne in (-1,1):
            for chgmtColone in (-2,2):
                if coord[0]+chgmtLigne<=7 and coord[0]+chgmtLigne>=0 and coord[1]+chgmtColone<=7 and coord[1]+chgmtColone>=0:
                    if grille[coord[1]+chgmtColone][coord[0]+chgmtLigne]==' ' or grille[coord[1]+chgmtColone][coord[0]+chgmtLigne].getCouleur()!=self.getCouleur():
                        choix.append([coord[0]+chgmtLigne, coord[1]+chgmtColone])

        return choix
