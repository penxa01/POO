from ClaseCalefactor import calefactor

class calefactorGas(calefactor):
    __matricula = None
    __calorias = None

    def __init__(self,marca,modelo,matricula,cal:int):
        super().__init__(marca,modelo)
        self.__matricula = matricula
        self.__calorias = cal

    def __str__(self):
        cadena = ""
        cadena += super().__str__() + ("Matricula: {}\nCalorias: {}kilocalorias/m³".format(self.__matricula,self.__calorias))

    def getMatricula(self):
        return self.__matricula
    
    def getCalorias(self):
        return self.__calorias
    
    def __lt__(self,otro):
        return self.__calorias < otro.getCalorias()