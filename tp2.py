
'''
  Fichier : Main
  Projet  : TP2
  Cours   : IFT2015 - Stuctures de données
  Auteurs : Olivier Provost (20101738)
            Moïka Sauvé     (20090119)
'''


from TextDict import TextDict
from Dictionnaire import Dictionnaire
import time
import math


def distance(d1, d2):
<<<<<<< HEAD
    #On choisi le plus petit dictionnaire pour le comparer avec le plus gros
    x = list()
    y = list()
=======
    #On choisi le plus petit dictionnaire pour le comparer avec le plus gros 
    plusPetit = null
    plusGrand = null
    x = []
    y = []
>>>>>>> 7a6914332abbe2127872a541b9d62425a69dda59
    sommeX = 0
    sommeY = 0
    distance = 0

    if (d1._n < d2._n):
        plusPetit = d1
        plusGrand = d2
    else:
        plusPetit = d2
        plusGrand = d1
<<<<<<< HEAD

    for item in plusPetit.T:
=======
    
    for (item in plusPetit): 
>>>>>>> 7a6914332abbe2127872a541b9d62425a69dda59
        if item is not None:
            for element in item:
                elementG = plusGrand[element.cle]
                if (elementG and elementG.cle == element.cle):
<<<<<<< HEAD
                    x.append(element.valeur)
                    sommeX += element.valeur
                    y.append(elementG.valeur)
                    sommeY += elementG.valeur

=======
                    x.add(element.valeur)
                    sommeX += x
                    y.add(elementG.valeur)
                    sommeY += y
    
>>>>>>> 7a6914332abbe2127872a541b9d62425a69dda59
    for i in range(len(x)):
        distance += (x[i] / sommeX - y[i]/ sommeY) ** 2

    distance = distance / len(x)
    return math.sqrt(distance)
<<<<<<< HEAD
=======





        # frequence = 0
        # nbDoublet = 0

        # for indexM in mystere.dictionnaire:
        #     if(indexM is not None):
        #         for elementM in indexM:
        #             elementD = self.dictionnaire[elementM.cle]
        #             if(elementD and elementD.cle == elementM.cle):
        #                 frequence += math.pow(elementD.valeur - elementM.valeur, 2)
        #                 nbDoublet += 1

        # return math.sqrt(frequence / nbDoublet)
>>>>>>> 7a6914332abbe2127872a541b9d62425a69dda59


def main():

    TEXTES = ["Balzac", "Hugo", "Segur", "Verne", "Voltaire", "Zola"]
    distances = {}

    avantAll = time.time()

    mystere = TextDict()
    mystere.treatText("./textes/mystere.txt")


    for texte in TEXTES:
        textDict = TextDict()
        avant = time.time()
        textDict.treatText("./textes/" + texte.lower() + ".txt")
        distances[texte] = distance(mystere.dictionnaire, textDict.dictionnaire)
        apres = time.time()
        #print(texte, "->", apres - avant, "secondes, distance :", distances[texte])

    auteur = TEXTES[0]
    minimum = distances[auteur]

    for (texte, dist) in distances.items():
        print(texte, dist)

        if(dist < minimum):
            minimum = distance
            auteur = texte

    print("Auteur du texte mystère :", auteur)

    apresAll = time.time()

    print("Temps total :", apresAll - avantAll, "secondes")


main()
