
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

    def __init__(self, c = 11): #1000500 ou 6000500 p = 109345121
        self.T = c * [None]
        self._n = 0
        self._capacite = c
        self._premier = 109345121
        self._echelle = 1 + randrange(109345121 - 1)
        self._decalage = randrange(109345121)
        self.collisions = 0



    def __len__(self):
        return self._n


    def __getitem__(self, cle):
        index = self._hachage(cle)

        if(self.T[index] is not None):
            # for item in self.T[index]:
            #     if(item.cle == cle):
            #         return item
            if(self.T[index].cle == cle):
                return self.T[index]

            else:
                temp = index
                while(self.T[index].cle != cle):
                    index +=1

                    if(index > len(self.T) - 1):
                        index = 0

                    if(index == temp):
                        return False
            
                return self.T[index]

        return False


    def __setitem__(self, cle, valeur):
        doublet = False
        index = self._hachage(cle)

        # --------------------- LIST POUR COLLISIONS

        if(self.T[index] is None):
            self.T[index] = list()
            self.T[index].append(Signature(cle, valeur))

        else:
            for item in self.T[index]:
                if(item.cle == cle):
                    item.valeur += 1
                    doublet = True
                    #print(index, " -> ", item.cle, " : ", item.valeur )
                    break
            
            if(not doublet):
                self.collisions += 1
                self.T[index].append(Signature(cle, valeur))
        

        # ---------------------- LINEAR PROBING

        # # Si le trou est vide on ajoute.
        # if(self.T[index] is None):
        #     self.T[index] = Signature(cle, valeur)
        
        # else:
        #     # Si le trou est pas vide on test si c'est la même cle, si oui, on incrémente la valeur.
        #     if(self.T[index].cle == cle):
        #         self.T[index].valeur += 1

        #     # Sinon on doit trouver un prochain trou disponible.
        #     else:
        #         self.collisions += 1
                
        #         while(self.T[index] is not None):
        #             index +=1

        #             if(index > len(self.T) - 1):
        #                 index = 0
                
        #         if(self.T[index] is None):
        #             self.T[index] = Signature(cle, valeur)

        self._n += 1
        #print(str(index) + " -> " + str(self.T[index]))

        if(self._n > len(self.T) // 2):
            self._resize(8 * len(self.T) - 1)


    def __delitem__(self, cle):
        index = self._hachage(cle)

        tempI = index

        while(self.T[index].cle != cle):
            index +=1

            if(index > len(self.T) - 1):
                index = 0

            # Si on revient à l'index, la clé n'existe pas.
            if(index == tempI):
                return False
                
        temp = self.T[index]
        del self.T[index]
        self._n -= 1
        return temp


    def _hachage(self, cle):
        # code = 0
        # n = len(cle) - 1

        # for char in cle:
        #     #somme += (ord(char) * pow(33, n))
        #     code += (ord(char) * (33 ** n))
        #     n -= 1

        # return code % self._capacite
        # #return ((self._echelle * code + self._decalage) % self._premier) % self._capacite
    
        # Fonction Hashing DJB2 - Source : https://gist.github.com/mengzhuo/180cd6be8ba9e2743753
        code = 5381

        for char in cle:
            code = ((code << 5) + code) + ord(char)

        return code % self._capacite


    def _resize(self, nouvelleCapacite):
        #vieux = list(self.items())
        #print("--- RESIZE ---")
        vieux = list()
        for item in self.T:
            if(item is not None):
                vieux.append(item)

        self.T = nouvelleCapacite * [None]
        self._n = 0
        self._capacite = nouvelleCapacite
        self.collisions = 0

        # Si on gère les collisions avec une LIST.
        for item in vieux:
            for element in item:
                self[element.cle] = element.valeur

        # Si on gère avec PROBING.
        # for element in vieux:
        #     self[element.cle] = element.valeur

