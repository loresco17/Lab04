class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo, stato):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo
        self.__stato = stato

    @property
    def cods(self):
        return self.__codice
    @cods.setter
    def cods(self, codice):
        self.__codice = codice

    @property
    def libs(self):
        return self.__stato
    @libs.setter
    def libs(self, stato):
        self.__stato = stato

    def __lt__(self, other):
        return self.__prezzo < other.__prezzo

    def __str__(self):
        return f'{self.__codice} {self.__padiglione} {self.__padiglione} {self.__prezzo} {self.__stato}'