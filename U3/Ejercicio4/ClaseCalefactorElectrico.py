from ClaseCalefactor import calefactor

class calefactorElectrico(calefactor):
    __potenciaMaxima = None

    def __init__(self,marca,modelo,potencia):
        super().__init__(marca,modelo)
        self.__potenciaMaxima = potencia
    
    def __str__(self):
        cadena = ""
        cadena += super().__str__() +("\nPotencia Maxima:{} watts".format(self.__potenciaMaxima))
        return cadena 
    
    def getPotencia(self):
        return self.__potenciaMaxima
    
    def __lt__(self,otro):
        return self.__potenciaMaxima< otro.getPotencia()

