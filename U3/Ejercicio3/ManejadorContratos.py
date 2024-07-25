from ClaseContrato import contrato
import numpy as np
import os

class manejadorContratos:
    __dimension  = 1
    __cantidad = 0
    __incremento = 1
    __Contratos = None

    def __init__(self):
        self.__Contratos = np.empty(self.__dimension,dtype=contrato)

    def agregarContrato(self,NuevoContrato):
        if(self.__cantidad == self.__dimension):
            self.__dimension += self.__incremento
            self.__Contratos.resize(self.__dimension)
        self.__Contratos[self.__cantidad] = NuevoContrato
        self.__cantidad += 1
    
    def getLista(self):
        return self.__Contratos

    