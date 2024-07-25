from datetime import date
from ClaseContrato import contrato

class jugador:
    __Nombre = None
    __DNI = None
    __ciudadNatal = None
    __paisOrigen = None
    __fecha_nacimiento = None
    __contrato = None

    def __init__(self,name,dni:int,city,contry,date:date):
        self.__Nombre = name
        self.__DNI = dni
        self.__ciudadNatal = city
        self.__paisOrigen = contry
        self.__fecha_nacimiento = date
    
    def __str__(self):
        cadena = ("Nombre:{}\n".format(self.__Nombre))
        cadena += ("DNI:{}\n".format(self.__DNI))
        cadena += ("Ciudad Natal:{}     Pais de Origen:{}\n".format(self.__ciudadNatal,self.__paisOrigen))
        cadena += ("Fecha de nacimiento:{}".format(self.__fecha_nacimiento))
        return cadena
    
    def setContrato(self,contrato:contrato):
        self.__contrato = contrato

    def getNombre(self):
        return self.__Nombre
    
    def getDNI(self):
        return self.__DNI
    
    def getCiudad(self):
        return self.__ciudadNatal
    
    def getPais(self):
        return self.__paisOrigen
    
    def getFecha(self):
        return self.__fecha_nacimiento
    
    def getContrato(self):
        return self.__contrato