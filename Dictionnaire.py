
'''
    Fichier : Dictionnaire
    Projet  : TP2
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

from random import randrange
from math import pow

class Dictionnaire :

    def __init__(self, capicite = 100000000):
        self._T = capicite * [None]
        self._n = 0
        self._capacite = capicite


    def _hachage(self, cle):

        somme = 0
        n = len(cle) - 1

        for char in cle:
            somme += ord(char) * pow(2, n)
            n -= 1

        return int(somme)


    def __len__(self):
        return self._n


    def __getitem__(self, cle):
        item = self._hachage(cle)
        return self._T[item]

    def __setitem__(self, cle, valeur):
        item = self._hachage(cle)

        while(item > self._capacite):
            self._resize(2 * len(self._T) - 1)

        if(self._T[item] is None):
            self._T[item] = {cle : valeur}

        else:
            self._T[item][cle] += 1


    def __delitem__(self, cle):
        item = self._hachage(cle)
        temp = self._T[item]

        if temp is not None:
            del self._T[item]
            return temp

        else:
            return False

    def __str__(self):
        for i in range(len(self._T)):
            if(self._T[i] is not None):
                print(str(i) + " : " + self._T[i])


    def _resize(self, nouvelleCapacite):
        vieux = list(self.items())
        self._T = nouvelleCapacite * [None]
        self._n = 0
        self._capacite = nouvelleCapacite

        for(cle, valeur) in vieux:
            self[cle] = valeur
