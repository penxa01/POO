from abc import ABC
import abc

class personal(ABC):
    __cuil = None
    __apellido = None
    __nombre = None
    __sueldoBasico = None
    __antiguedad = None

    def __init__(self,cuil:str,apellido:str,nombre:str,sueldo:str,antiguedad:int,**kwargs):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = sueldo
        self.__antiguedad = antiguedad

    def __str__(self):
        return ("Apellido y Nombre:{} {}\n Cuil:{}\nSueldo Basico:${}\nAntiguedad:{}\n".format(self.__apellido,self.__nombre,self.__cuil,self.__sueldoBasico,self.__antiguedad))

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getNombreCompleto(self):
        return self.__nombre + " "+ self.__apellido
    
    def getCuil(self):
        return self.__cuil
    
    def getSueldoBasico(self):
        return self.__sueldoBasico
    
    @abc.abstractmethod
    def getSueldo(self):
        pass
    
    def getAntiguedad(self):
        return self.__antiguedad
    
    def toJson(self):
        diccionario = dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                cuil = self.__cuil,
                apellido = self.__apellido,
                nombre = self.__nombre,
                sueldo = self.__sueldoBasico,
                antiguedad = self.__antiguedad
            )
        )
        return diccionario
    
    def __gt__(self,otro):
        return self.__nombre > otro.getNombre()
    
    
    
    
