# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Pion(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Pion')
    
    def mouvementPiece(self, grille, coord):
        choix=[]
        #Le pion se déplace pas pareil en fonction de sa couleur
        direction=1
        if self.getCouleur()=='Noir':
            direction=-1

        #Si c'est le premier mouvement du pion, on peut le faire avancer de deux cases (on vérifie si il est sur sa ligne de départ)
        if direction==1:
            if coord[1]==6 and grille[coord[1]-(2*direction)][coord[0]]==' ':
                choix.append([coord[0], coord[1]-2])
        elif coord[1]==1 and grille[coord[1]+2][coord[0]]==' ':
            choix.append([coord[0], coord[1]+2])

        #Un pion peut avancer d'une case devant lui si celle ci est libre
        if coord[1]-direction>=0 and coord[1]-direction<=7:
            if grille[coord[1]-direction][coord[0]]==' ':
                choix.append([coord[0], coord[1]-direction])
        
            #Mais il prend les pièces adverses que sur les diagonales
            if coord[0]+1<=7 and grille[coord[1]-direction][coord[0]+1]!=' ':
                if self.getCouleur()!=grille[coord[1]-direction][coord[0]+1].getCouleur():
                    choix.append([coord[0]+1, coord[1]-direction])
        
            if coord[0]-1>=0 and grille[coord[1]-direction][coord[0]-1]!=' ':
                if self.getCouleur()!=grille[coord[1]-direction][coord[0]-1].getCouleur():
                    choix.append([coord[0]-1, coord[1]-direction])

        return choix