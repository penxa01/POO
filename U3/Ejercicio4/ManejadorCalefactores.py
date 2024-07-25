import numpy as np 
import csv
import os
from ClaseCalefactor import calefactor
from ClaseCalefactorElectrico import calefactorElectrico
from ClaseCalefactorGas import calefactorGas

class manejadorCalefactores:
    __incremento = None
    __cantidad = None
    __dimension = None
    __Calefactores = None

    def __init__(self,dimensionPorTeclado):
        self.__cantidad = 0
        self.__incremento = 1
        self.__dimension = dimensionPorTeclado
        self.__Calefactores = np.empty(self.__dimension,dtype=calefactor)
    
    def agregarCalefactor(self,calefactor):
        if(self.__dimension == self.__cantidad):
            self.__dimension += self.__incremento
            self.__Calefactores.resize(self.__dimension)
        self.__Calefactores[self.__cantidad] = calefactor
        self.__cantidad+= 1
    
    def cargarCalefactoresGas(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "calefactorAGas.csv")
        archivo =open(Archivo)
        reader = csv.reader(archivo,delimiter=";")
        for comp in reader:

            NuevoCalef = calefactorGas(comp[0],comp[1],comp[2],int(comp[3]))
            self.agregarCalefactor(NuevoCalef)
        
        archivo.close()
    
    def carfarCalefactoresElectricos(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "calefactorElectricos.csv")
        archivo =open(Archivo)
        reader = csv.reader(archivo,delimiter=";")
        for comp in reader:

            NuevoCalef = calefactorElectrico(comp[0],comp[1],int(comp[2]))
            self.agregarCalefactor(NuevoCalef)
    
    def getIndiceCalefactorGas(self):
        i = 0
        while not isinstance(self.__Calefactores[i], calefactorGas) and i < self.__cantidad:
            i += 1
        if i == self.__cantidad:
            i = -1
        return i

    def getIndiceCalefactorElectrico(self):
        i = 0
        while not isinstance(self.__Calefactores[i], calefactorElectrico) and i < self.__cantidad:
            i += 1
        if i == self.__cantidad:
            i = -1
        return i
    
    def getCalefactorGasMenorConsumo(self):
        menor = self.__Calefactores[self.getIndiceCalefactorGas()]
        indiceCalefactorGas = self.getIndiceCalefactorGas()

        for i in range(indiceCalefactorGas,self.getIndiceCalefactorGas()):
            if(self.__Calefactores[i]< menor):
                menor = self.__Calefactores[i]
        
        return menor

    def getCalefactorElectricoMenorConsumo(self):
        menor = self.__Calefactores[self.getIndiceCalefactorElectrico()]

        for i in range(self.__cantidad):
            if isinstance(self.__Calefactores[i],calefactorElectrico):
                if(self.__Calefactores[i]<menor):
                    menor = self.__Calefactores[i]
        
        return menor




