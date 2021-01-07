# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Roi(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Roi')
    
    def mouvementPiece(self, grille, coord):
        print("Roi")