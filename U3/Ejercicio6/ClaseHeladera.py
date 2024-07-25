from ClaseAparatos import aparato
import json

class Heladera(aparato):
    __capacidad = None
    __freezer = None
    __ciclica = None

    def __init__(self,marca,modelo,color,pais,precio,capacidad:int,freezer:bool,ciclica:bool):
        super().__init__(marca,modelo,color,pais,precio)
        self.__capacidad = capacidad
        self.__freezer = freezer
        self.__ciclica = ciclica

    def __str__(self):
        cadena = ""
        cadena += super().__str__() + ("Capacidad de litros:{}\n Freezer:{}     Ciclica:{}".format(self.__capacidad,self.__freezer,self.__ciclica))
        return cadena

    def getCapacidad(self)->int:
        return self.__capacidad

    def getFreezer(self)->bool:
        return self.__freezer

    def getCiclica(self)->bool:
        return self.__ciclica

    def getImporte(self):
        importe = self.getPrecio()

        if self.__freezer:
            importe += importe* 0.05
        else:
            importe += importe*0.01
        
        if self.__ciclica:
            importe += self.getPrecio()*0.1
        
        return importe
    
    def toJson(self):
        diccionarioHeladera = dict(__class__ = self.__class__.__name__, 
        __atributos__ = dict(
            marca = self.getMarca(),
            modelo = self.getModelo(),
            color = self.getColor(),
            pais = self.getPais(),
            precio = self.getPais(),
            capacidad = self.__capacidad,
            freezer = self.__freezer,
            ciclica = self.__ciclica)
        )
        return diccionarioHeladera