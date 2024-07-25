import os
class conjunto():
    __Conj = []

    def __init__(self):
        self.__Conj = []
    

    def mostrarConj(self):
        print (self.__Conj)
    
    def getV(self,indice):
        return self.__Conj[indice]
    
    def getlong(self):
        return len(self.__Conj)

    def __buscar(self, x):
        i = 0
        bandera = False
        while (i < len(self.__Conj)) and (bandera == False):
            if self.__Conj[i] == x:
                bandera = True
            i+=1
        return bandera
    
    def cargar(self):
        band = False
        x = int(input("Ingrese un valor entero al conjunto(Distinto de 0)\n"))
        while (x != 0):
            band = self.__buscar(x)
            if band != True:
                self.__Conj.append(x)
                print("Elemento cargado exitosamente!!")
            else:
                print("El elemento ya pertenece al conjunto")
            x = int(input("Ingrese siguiente valor que desea agregar: "))
            

    def BusCoincidencias(self,el,other):
        bandera = False
        indice = 0
        while (bandera == False) and (indice < other.getlong()):
            if el == other.getV(indice):
                bandera = not bandera
            indice += 1
        return bandera

    
    def __add__(self,otroConj):
        if type(self.__Conj) == type(otroConj.__Conj):
            suma = conjunto()
            i= 0
            n = 0
            for i in range(self.getlong()):
                suma.__Conj.append(self.getV(i))
            for n in range(otroConj.getlong()):
                if (self.BusCoincidencias(otroConj.getV(n),suma) == False):
                    suma.__Conj.append(otroConj.getV(n))
            
        return suma


    def __sub__(self,otroConj):
        if type(self.__Conj) == type(otroConj.__Conj):
            resta = conjunto()
            for i in range(self.getlong()):
                for j in range(otroConj.getlong()):
                    if self.BusCoincidencias(self.__Conj[i], otroConj) == False:
                         if self.BusCoincidencias(self.__Conj[i], resta) == False:
                            resta.__Conj.append(self.__Conj[i])
        return resta

    def __eq__(self, conjunto):
        bandera = False
        cont = 0
        if type(self.__Conj) == type(conjunto.__Conj):
            if(self.getlong() == conjunto.getlong()):
                for i in range(self.getlong()):
                    coincidencia = self.BusCoincidencias(self.__Conj[i],conjunto)
                    if coincidencia:
                        cont += 1
                if cont == self.getlong():
                    bandera = not bandera
                return bandera
                
            else:
                return bandera
