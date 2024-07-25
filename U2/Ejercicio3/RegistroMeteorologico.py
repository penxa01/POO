import os


class Registro:
    __Temperatura = 0.00
    __Humedad = 0
    __Presion = 0

    def __init__(self,temperatura,humedad,presion):
        self.__Temperatura = temperatura
        self.__Humedad = humedad
        self.__Presion = presion

    def __str__(self):
        return ("{}°C         {}%           {}".format(self.__Temperatura, self.__Humedad,self.__Presion))

    def getTemperatura(self):
        return self.__Temperatura
    
    def getHumedad(self):
        return self.__Humedad

    def getPresion(self):
        return self.__Presion