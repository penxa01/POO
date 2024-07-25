from ClaseEquipo import equipo
import numpy as np
import os
import csv

class manejadorEquipos:
    __Equipos = None
    __Cantidad = 0
    __dimension = 1
    __incremento = 1

    def __init__(self):
        self.__Equipos = np.empty(self.__dimension, dtype = equipo)
    
    
    def agregarEquipo(self,equipoNuevo):

        if(self.__Cantidad == self.__dimension):
            self.__dimension += self.__incremento
            self.__Equipos.resize(self.__dimension)
        self.__Equipos[self.__Cantidad] =equipoNuevo
        self.__Cantidad += 1
    
    def cargarArchivo(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "equipos.csv")
        archivo =open(Archivo)
        reader = csv.reader(archivo,delimiter= ";")
        cabecera =True
        for comp in reader:
            if cabecera:
                cantidadEquipos = int(comp[0])
                cabecera = not cabecera
            else:
                instanciaEquipo = equipo(comp[0],comp[1])
                self.agregarEquipo(instanciaEquipo)
                print("Equipo agregado con exito")
        
        archivo.close()
    
    def buscarEquipo(self,equipoIngresado):
        i = 0
        bandera = False

        while i < len(self.__Equipos) and  not bandera:
            if(equipoIngresado.lower() == self.__Equipos[i].getNombre().lower()):
                bandera = True
            else:
                i += 1 
        if(bandera == False):
           i =-1

        return i
    
    def getEquipo(self,i):
        return self.__Equipos[i]
    
    def setContrato(self,i,contrato):
        self.__Equipos[i].generarContrato(contrato)
        print("Contrato creado con exito")
