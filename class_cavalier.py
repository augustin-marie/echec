# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Cavalier(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Cavalier')
    
    def mouvementPiece(self, grille, coord):
        print("Cavalier")
