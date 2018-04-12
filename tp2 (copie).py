
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
    #On choisi le plus petit dictionnaire pour le comparer avec le plus gros
    x = list()
    y = list()
    sommeX = 0
    sommeY = 0
    distance = 0

    if (d1._n < d2._n):
        plusPetit = d1
        plusGrand = d2
    else:
        plusPetit = d2
        plusGrand = d1

    for item in plusPetit.T:
        if item is not None:
            for element in item:
                elementG = plusGrand[element.cle]
                if (elementG and elementG.cle == element.cle):
                    x.append(element.valeur)
                    sommeX += element.valeur
                    y.append(elementG.valeur)
                    sommeY += elementG.valeur

    for i in range(len(x)):
        distance += (x[i] / sommeX - y[i]/ sommeY) ** 2

    distance = distance / len(x)
    return math.sqrt(distance)


def main():

    TEXTES = ["Balzac", "Hugo", "Segur", "Verne", "Voltaire", "Zola"]
    distances = {}

    avantAll = time.time()

    mystere = TextDict()
    mystere.treatText("./textes/mystere.txt")

    # none = 0
    # for i in range(len(mystere.dictionnaire.T)):
    #     if(mystere.dictionnaire.T[i] is not None):
    #         print(i, ":", len(mystere.dictionnaire.T[i]), "éléments")
    #     else:
    #         none += 1

    # print(none, "élements None sur", len(mystere._dictionnaire.T))

    for texte in TEXTES:
        textDict = TextDict()
        avant = time.time()
        textDict.treatText("./textes/" + texte.lower() + ".txt")
        distances[texte] = distance(mystere.dictionnaire, textDict.dictionnaire)
        apres = time.time()
        print(texte, "->", apres - avant, "secondes, distance :", distances[texte], ", collisions :", textDict.dictionnaire.collisions)
        #print(texte, "->", apres - avant, "secondes, collisions :", textDict.dictionnaire.collisions)
        #print(texte, "-> Collisions :", textDict.dictionnaire.collisions)

    apresAll = time.time()

    print("Temps total :", apresAll - avantAll, "secondes")


main()
