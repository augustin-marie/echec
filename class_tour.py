# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Tour(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Tour')
        self.__dejaBouger=False
    
    def mouvementPiece(self, grille, coord):
        print('nop')