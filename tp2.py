
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


def distance(d1, d2):
    #On choisi le plus petit dictionnaire pour le comparer avec le plus gros 
    plusPetit = null
    plusGrand = null
    x = []
    y = []
    sommeX = 0
    sommeY = 0
    distance = 0

    if (d1._n < d2._n):
        plusPetit = d1
        plusGrand = d2
    else:
        plusPetit = d2
        plusGrand = d1
    
    for (item in plusPetit): 
        if item is not None:
            for element in item:
                elementG = plusGrand[element.cle]
                if (elementG and elementG.cle == element.cle):
                    x.add(element.valeur)
                    sommeX += x
                    y.add(elementG.valeur)
                    sommeY += y
    
    for i in range(len(x)):
        distance += (x[i] / sommeX - y[i]/ sommeY) ** 2

    distance = distance / len(x)
    return math.sqrt(distance)





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


def main():

    TEXTES = ["Balzac", "Hugo", "Segur", "Verne", "Voltaire", "Zola"]
    distances = {}

    avant = time.time()

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
        #avant = time.time()
        textDict.treatText("./textes/" + texte + ".txt")
        #distances[texte] = textDict.distance(mystere)
        #apres = time.time()
        #print(texte, "->", apres - avant, "secondes, distance :", distances[texte], ", collisions :", textDict.dictionnaire.collisions)
        #print(texte, "->", apres - avant, "secondes, collisions :", textDict.dictionnaire.collisions)
        print(texte, "-> Collisions :", textDict.dictionnaire.collisions)

    apres = time.time()

    print("Temps total :", apres - avant)
        

main()
