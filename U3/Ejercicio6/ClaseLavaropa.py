from ClaseAparatos import aparato
import json

class Lavarropa(aparato):
    __capacidad = None
    __velocidad = None
    __cantProgramas = None
    __tipoCarga =None

    def __init__(self,marca,modelo,color,pais,precio,capacidad:int,velocidad:int,cantProgramas:int,tipoCarga:str):
        super().__init__(marca,modelo,color,pais,precio)
        self.__capacidad = capacidad
        self.__velocidad = velocidad
        self.__cantProgramas = cantProgramas
        self.__tipoCarga = tipoCarga

    def __str__(self):
        cadena = ""
        cadena += super().__str__() + ("Capacidad de lavado:{}\nVelocidad de centrifugado:{}\nCantidad de programas:{}\nTipo de carga:{}".format(self.__capacidad,self.__velocidad,self.__cantProgramas,self.__tipoCarga))
        return cadena

    def getCapacidad(self)->int:
        return self.__capacidad
    
    def getVelocidad(self):
        return self.__velCentrifugado

    def getCantidad(self):
        return self.__cantProg
    
    def getTipoCarga(self):
        return self.__tipoCarga
    
    def getImporte(self):
        importe = self.getPrecio()

        if(self.__capacidad <= 5):
            importe += importe * 0.01
        else:
            importe += importe * 0.03
        return importe

    def toJson(self):
        diccionarioLavarropa = dict(__class__ = self.__class__.__name__, 
        __atributos__ = dict(
            marca = self.getMarca(),
            modelo = self.getModelo(),
            color = self.getColor(),
            pais = self.getPais(),
            precio = self.getPais(),
            capcidad = self.__capacidad,
            velocidadCentr = self.__velocidad,
            cantProg = self.__cantProgramas,
            tipoCarga = self.__tipoCarga)
        )
        return diccionarioLavarropa