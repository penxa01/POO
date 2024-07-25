import abc
from abc import ABC

class aparato(ABC):
    __marca = None
    __modelo = None
    __color = None
    __pais = None
    __precio = None

    def __init__(self,marca:str,modelo:str,color:str,pais:str,precio:float):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__pais = pais
        self.__precio = precio

    def __str__(self):
        return("Marca:{}    Modelo:{}\nColor:{}\nPais de Fabricacion:{}\nPrecio de Base:${}\n".format(self.__marca,self.__modelo,self.__color,self.__pais,self.__precio))

    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getColor(self):
        return self.__color
    
    def getPais(self):
        return self.__pais
    
    def getPrecio(self):
        return self.__precio
    
    @abc.abstractclassmethod
    def getCapacidad(self):
        pass

    @abc.abstractclassmethod
    def getImporte(self):
        pass

    @abc.abstractclassmethod
    def toJson(self):
        pass