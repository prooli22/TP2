
'''
  Fichier : TextDict
  Projet  : TP2
  Cours   : IFT2015 - Stuctures de données
  Auteurs : Olivier Provost (20101738)
            Moïka Sauvé     (20090119)
'''

PONC = ["!",'"',"'",")","(",",",".",";",":","?", "-", "_"]

from Dictionnaire import Dictionnaire


class TextDict:
    """
    Represents a text as a dictionary of word doublet frequencies.
    """

    def __init__(self):
        self.dictionnaire = Dictionnaire()


    def treatText(self, filename):
        """
        Represents text with doublet frequencies.
        """
        prevword = None
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                line = line.rstrip()
                if line == '': continue
                words = self.treatLine(line)

                if len(words) > 1 :
                    if(prevword is not None):
                        self.dictionnaire[str(prevword + " " + words[0])] = 1

                    for i in range(len(words) - 1):
                        #print(str(words[i] + " " + words[i + 1]))
                        self.dictionnaire[str(words[i] + " " + words[i + 1])] = 1

                    prevword = words[-1]


    def treatLine(self, line):
        """
        Separates words and removes punctuation.
        """
        noponc = ""
        for c in line:
            if c in PONC:
                noponc = noponc + " "
            else:
                noponc = noponc + c
        words = noponc.split()
        wlower = []
        for w in words:
            if len(w) > 2:
                wlower.append(w.lower())
        return wlower
