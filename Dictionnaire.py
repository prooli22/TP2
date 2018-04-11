
'''
  Fichier : Dictionnaire
  Projet  : TP2
  Cours   : IFT2015 - Stuctures de données
  Auteurs : Olivier Provost (20101738)
            Moïka Sauvé     (20090119)
'''

from random import randrange
from math import pow
import collections

class Element:
    
    def __init__(self, c, v):
        self.cle = c
        self.valeur = v


class Dictionnaire (collections.MutableMapping) :

    def __init__(self, c = 6000500, p = 109345121):
        self.T = c * [None]
        self._n = 0
        self._capacite = c
        self._premier = p
        self._echelle = 1 + randrange(p - 1)
        self._decalage = randrange(p)
        self.collisions = 0


    def __iter__(self):
        for item in self.T:
            if item is not None:
                for cle in item:
                    yield cle


    def _hachage(self, cle):
        somme = 0
        n = len(cle) - 1

        for char in cle:
            somme += (ord(char) * pow(33, n))
            n -= 1

        return int(((self._echelle * somme + self._decalage) % self._premier) % self._capacite)


    def __len__(self):
        return self._n


    def __getitem__(self, cle):
        index = self._hachage(cle)
        return self.T[index]


    def __setitem__(self, cle, valeur):
        doublet = False
        index = self._hachage(cle)

        if(self.T[index] is None):
            self.T[index] = list()
            self.T[index].append(Element(cle, valeur))

        else:
            for item in self.T[index]:
                if(item.cle == cle):
                    item.valeur += 1
                    doublet = True
                    #print(index, " -> ", item.cle, " : ", item.valeur )
                    break
            
            if(not doublet):
                #self.collisions += 1
                self.T[index].append(Element(cle, valeur))

        self._n += 1
        #print(str(index) + " -> " + str(self.T[index]))

        if(self._n > len(self.T) // 2):
            self._resize(2 * len(self.T) - 1)


    def __delitem__(self, cle):
        index = self._hachage(cle)
        temp = self.T[index]

        if temp is not None:
            del self.T[index]
            self._n -= 1
            return temp

        else:
            return False


    # def __str__(self):
    #     for i in range(len(self.T)):
    #         if(self.T[i] is not None):
    #             print(str(i) + " : " + self.T[i])


    def _resize(self, nouvelleCapacite):
        #vieux = list(self.items())
        print("--- RESIZE ---")
        vieux = list()
        for item in self.T:
            if(item is not None):
                vieux.append(item)

        self.T = nouvelleCapacite * [None]
        self._n = 0
        self._capacite = nouvelleCapacite

        for item in vieux:
            for element in item:
                self[element.cle] = element.valeur

