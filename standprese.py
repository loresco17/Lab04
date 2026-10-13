from stand import Stand
class StandPrese(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, prese, stato):
        self.__prese = prese
        super().__init__(codice, superficie, padiglione, prezzo, stato)

    def __str__(self):
        return f'{super().__str__()} {self.__prese}'