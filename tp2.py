
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

def main():

    TEXTES = ["balzac", "hugo", "segur", "verne", "voltaire", "zola"]
    distances = {}

    mystere = TextDict()
    mystere.treatText("./textes/mystere.txt")

    for texte in TEXTES:
        textDict = TextDict()
        avant = time.time()
        textDict.treatText("./textes/" + texte + ".txt")
        distances[texte] = textDict.distance(mystere)
        apres = time.time()
        print(texte, "->", apres - avant, "secondes, distance :", distances[texte])

    #print(textDict._dictionnaire)

main()
