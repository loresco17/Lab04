class Espositore:
    def __init__(self, codice, nome, cognome, stato):
        self.__codice=codice
        self.__nome=nome
        self.__cognome=cognome
        self.__stato=stato

    @property
    def code(self):
        return self.__codice
    @code.setter
    def code(self, code):
        self.__codice = code

    @property
    def libe(self):
        return self.__stato
    @libe.setter
    def libe(self, stato):
        self.__stato = stato

    def __str__(self):
        if self.libe is not None:
            info_stand = self.libe.cods
        else:
            info_stand = "Disponibile"
        return f'{self.__codice} {self.__nome} {self.__cognome} {info_stand}'