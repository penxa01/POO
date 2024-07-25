import os 
import csv
from ClaseFlor import flor
import numpy as np

class flores:
    __cantidad = 0
    __incremento = 1
    __dimension = 1
    __ListaFlores = None

    def __init__(self):
        self.__ListaFlores = np.empty(self.__dimension,dtype= flor)
    

    def agregarFlor(self,NuevaFlor):

        if(self.__cantidad == self.__dimension):
            self.__dimension += self.__incremento
            self.__ListaFlores.resize(self.__dimension)
        self.__ListaFlores[self.__cantidad] = NuevaFlor
        self.__cantidad += 1

    def cargarArchivoFlores(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "flores.csv")
        archivo =open(Archivo)
        reader = csv.reader(archivo,delimiter= ";")

        for comp in reader:

            instanciaNueva = flor(int(comp[0]),comp[1].capitalize(),comp[2].capitalize(),comp[3].capitalize())
            self.agregarFlor(instanciaNueva)
        
        archivo.close()
    
    def getLista(self):
        return self.__ListaFlores

    def buscarFlor(self,dato):
        
        i = 0
        bandera = False
        while (i < len(self.__ListaFlores)) and (bandera == False):
            if self.__ListaFlores[i].getNroFlor() == dato:
                bandera = True
            else:
                i+=1
        if bandera:
            print("Flor Encontrada")
        else:
            print("Flor no encontrada")
            i = -1
        return i

    
    def mostrarModaFlores(self):
        self.__ListaFlores.sort()
        print("Top 5 flores mas vendidas")
        for i in range(5):
            print("".center(20),"-")
            print(self.__ListaFlores[i])
            
    

    