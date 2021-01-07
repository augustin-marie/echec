# coding: utf-8
#===============imports===============
import class_piece

#===============classes===============
class Pion(class_piece.Piece):
    def __init__(self,couleur):
        super().__init__(couleur, 'Pion')
    
    def mouvementPiece(self, grille, coord):
        choix=[]

        if coord[1]==6 and coord[1]-2>=0 and grille[coord[1]-2][coord[0]]==' ':
            choix.append([coord[0], coord[1]-2])
        
        if coord[1]-1>=0:
            if grille[coord[1]-1][coord[0]]==' ':
                choix.append([coord[0], coord[1]-1])
        
            if coord[0]+1<=7 and grille[coord[1]-1][coord[0]+1]!=' ':
                choix.append([coord[0]+1, coord[1]]-1)
        
            if coord[0]-1>=0 and grille[coord[1]-1][coord[0]-1]!=' ':
                choix.append([coord[0]-1, coord[1]-1])

        return choix