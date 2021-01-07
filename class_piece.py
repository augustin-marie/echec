# coding: utf-8
#===============imports===============

#===============classes===============
#Classe servant au print et aux caractéristiques communes entres les pièces
class Piece:
    def __init__(self,c,nom):
        self.__couleur=c
        self.__nom=nom
        self.__caractere=nom[0]
    
    #consulter la couleur en externe
    def getCouleur(self):
        return self.__couleur
    
    #consulter le nom en externe
    def getNom(self):
        return self.__nom
    
    #redefinition du str()
    def __repr__(self):
        if self.__couleur=='Noir':
            return(gras(self.__caractere))
        else:
            return(self.__caractere)

    #redefinition du print()
    def __str__(self):
        if self.__couleur=='Noir':
            return(gras(self.__caractere))
        else:
            return(self.__caractere)

#==============fonctions==============
#Permet de mettre en gras (utiliser pour différencier les pièces noires)
def gras(text):
    return '\033[1m'+text+'\033[0m'
