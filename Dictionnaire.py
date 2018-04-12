
'''
  Fichier : Dictionnaire
  Projet  : TP2
  Cours   : IFT2015 - Stuctures de données
  Auteurs : Olivier Provost (20101738)
            Moïka Sauvé     (20090119)
'''

from random import randrange
from math import pow

class Signature:

    def __init__(self, c, v):
        self.cle = c
        self.valeur = v


class Dictionnaire () :

    def __init__(self, c = 11):
        self.T = c * [None]
        self._n = 0
        self._capacite = c


    def __len__(self):
        return self._n


    def __getitem__(self, cle):
        # On va chercher l'index avec notre fonction de hachage.
        index = self._hachage(cle)

        # On retourne l'élément correspondant s'il existe.
        if(self.T[index] is not None):
            for item in self.T[index]:
                if(item.cle == cle):
                    return item

        # Sinon on retourne False.
        else:
            return False


    def __setitem__(self, cle, valeur):
        # On va chercher l'index avec notre fonction de hachage.
        index = self._hachage(cle)
        doublet = False

        # Si l'index est None, on ajoute directement.
        if(self.T[index] is None):
            self.T[index] = list()
            self.T[index].append(Signature(cle, valeur))

        else:
            # On va chercher si un élément de la List contient déjà la même clé.
            for item in self.T[index]:
                if(item.cle == cle):
                    item.valeur += 1
                    doublet = True
                    break

            # Si aucun doublet n'a été trouvé.
            if(not doublet):
                self.T[index].append(Signature(cle, valeur))

        self._n += 1

        # Si le nombre d'éléments est plus que la moitié de la longeur du tableau. On appelle resize.
        if(self._n > len(self.T) // 2):
            self._resize(8 * len(self.T) - 1)


    def __delitem__(self, cle):
        # On va chercher l'index avec notre fonction de hachage.
        index = self._hachage(cle)

        # Si l'index est pas None, on va chercher l'élément à supprimer dans la List.
        if(self.T[index] is not None):
            for element in self.T[index]:
                if(element.cle == cle):
                    temp = element
                    del elementG
                    self._n -= 1
                    return temp

        # Sinon on retourne False, l'élément n'existe pas.
        else:
            return False


    def _hachage(self, cle):
        # Fonction Hashing DJB2 - Source : https://gist.github.com/mengzhuo/180cd6be8ba9e2743753
        code = 5381

        for char in cle:
            code = ((code << 5) + code) + ord(char)

        return code % self._capacite


    def _resize(self, nouvelleCapacite):
        # On prend un backup des éléments du tableu.
        vieux = list()
        for item in self.T:
            if(item is not None):
                vieux.append(item)

        # On resize le tableau avec la nouvelleCapacite.
        self.T = nouvelleCapacite * [None]
        self._n = 0
        self._capacite = nouvelleCapacite
        self.collisions = 0

        # On ajoute tous éléments en backup dans le tableau.
        for item in vieux:
            for element in item:
                self[element.cle] = element.valeur
