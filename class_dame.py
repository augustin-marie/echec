# coding: utf-8
#===============imports===============
import class_piece
import class_fou
import class_tour


#===============classes===============
class Dame(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Dame')
    
    def mouvementPiece(self, grille, coord):
        choix=[]
        mouvementTour=class_tour.Tour(self.getCouleur).mouvementPiece(grille, coord)
        mouvementFou=class_fou.Fou(self.getCouleur).mouvementPiece(grille, coord)
        for case in mouvementTour:
            choix.append(case)
        for case in mouvementFou:
            choix.append(case)

        return choix
        



#C'est pour sa que les tests sont fait avec [ligne][colone] mais on append [colone, ligne]
#on est obliger de faire comme sa sinon c'est le bordel ou en tout cas j'ai pas trouver
#d'autres solutions