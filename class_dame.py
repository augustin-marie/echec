# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Dame(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Dame')
    
    def mouvementPiece(self, grille, coord):
        print("Dame")