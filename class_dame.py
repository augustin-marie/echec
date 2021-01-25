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
        #Pour la Dame, on simule les mouvements d'une tour et d'un fou qui serait a son emplacement
        #Ensuite on dit que les déplacement possibles de la Dame est la somme des déplacements possibles dans les deux simulations

        #simultaions
        mouvementTour=class_tour.Tour(self.getCouleur()).mouvementPiece(grille, coord)
        mouvementFou=class_fou.Fou(self.getCouleur()).mouvementPiece(grille, coord)

        #somme des mouvements
        for case in mouvementTour:
            choix.append(case)
        for case in mouvementFou:
            choix.append(case)

        return choix
