# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Fou(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Fou')

    def mouvementPiece(self, grille, coord):
        print("Fou")