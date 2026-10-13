from stand import Stand
class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, posizione, stato):
        self.__posizione = posizione
        super().__init__(codice, superficie, padiglione, prezzo, stato)

    def __str__(self):
        return f'{super().__str__()} {self.__posizione}'