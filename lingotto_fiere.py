import csv
from stand import Stand
from standprese import StandPrese
from standpremium import StandPremium
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        self.__nome = nome
        self.__stand=[]
        self.__espositori=[]

    @property
    def fiera(self):
        return self.__nome
    @fiera.setter
    def fiera(self, nome):
        self.__nome = nome

    def carica_file_dati(self, file_path):
        with open(file_path, "r") as file:
            r = csv.reader(file)
            for line in r:
                if line[0][0]=='S':
                    if len(line)==4:
                        s=Stand(line[0], int(line[1]), int(line[2]), float(line[3]), None)
                    else:
                        try:
                            prezzo=float(line[3])*(1+0.07*int(line[4]))
                            s=StandPrese(line[0], int(line[1]), int(line[2]), prezzo, int(line[4]), None)
                        except ValueError:
                            prezzo=float(line[3])*1.3
                            s=StandPremium(line[0], int(line[1]), int(line[2]), prezzo, line[4], None)
                    self.__stand.append(s)
                else:
                    e=Espositore(line[0], line[1], line[2], None)
                    self.__espositori.append(e)

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        stand_trovato = next((s for s in self.__stand if s.cods == codice_stand), None)
        espositore_trovato = next((e for e in self.__espositori if e.code == codice_espositore), None)
        if not stand_trovato:
            raise Exception("Lo stand non esiste nella fiera")
        if not espositore_trovato:
            raise Exception("L'espositore non esiste nella fiera")
        if stand_trovato.libs is not None:
            raise Exception("Lo stand richiesto è già occupato")
        if espositore_trovato.libe is not None:
            raise Exception("L'espositore ha già uno stand assegnato")
        stand_trovato.libs = espositore_trovato
        espositore_trovato.libe = stand_trovato
        for e in self.__espositori:
            fine=False
            if e.code == codice_espositore:
                for s in self.__stand:
                    if s.cods == codice_stand:
                        s.libs=e
                        e.libe=s
                        fine=True
                        break
            if fine:
                break

    def elenca_espositori(self):
        for e in self.__espositori:
            print(e)

    def stand_ordinati_per_prezzo(self):
        return sorted(self.__stand)