import os
import numpy as np
from Persona import persona
import csv

class manejadorPersonal:
    __incremento = 5
    __cantidad = 0
    __dimension = 0
    __personal = None

    def __init__(self,dimension = 4, incremento = 2):
        self.__incremento = incremento
        self.__personal = np.empty(dimension,dtype = persona)
    
    def agregarPersonal(self,p):

        if (self.__cantidad == self.__dimension):
            self.__dimension += self.__incremento
            self.__personal.resize(self.__dimension)
        self.__personal[self.__cantidad] = p
        self.__cantidad += 1

    def CargarPersonal(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "personal.csv")
        archivo = open(Archivo)

        reader = csv.reader(archivo,delimiter = ";")
        cabeza = True

        for comp in reader:
            if cabeza:
                cabeza = not cabeza
            else:
                NuevaPersona = persona(comp)
                self.agregarPersonal(NuevaPersona)
        
        print("Personal cargado con exito")
        
        archivo.close()
    
    def buscarPersonal(self,legajo):
        i = 0
        bandera = False
        while (i < len(self.__personal)) and (bandera == False):
            if self.__personal[i].getLegajo() == legajo:
                bandera = True
            else:
                i+=1
        if bandera:
            print("Personal existente")
        else:
            i = -1
        
        return i
    
    def sueldoLiquidarLegajo(self,legajoIngresado,Novedades):
        busqueda = self.buscarPersonal(legajoIngresado)
        if(busqueda == -1):
            print("El legajo ingresado es inexistente")
        else:
            sueldoALiquidar = self.__personal[busqueda].getSueldoBasico()
            print("Sueldo Basico".format(sueldoALiquidar))
            print("Buscando Novedades".center(30,"-"))
            Nov = Novedades.getLista()
            for novedad in Nov:
                if(legajoIngresado == novedad.getLegajo()):
                    print("Novedad hallada")
                    if(novedad.getCodigo() == "A"):
                        sueldoALiquidar += novedad.getImporte()
                    elif(novedad.getCodigo() == "D"):
                        sueldoALiquidar-= novedad.getImporte()
                    print("Concepto:{}".format(novedad.getConcepto()))
            
            print("El sueldo a liquidar del legajo {} es de ${}".format(legajoIngresado,sueldoALiquidar))
        
        input("Presione ENTER para continuar")
    
    def ordenar(self,Novedades):

        self.__personal.sort()
        print("Listado del personal".center(30,"-"))
        for persona in self.__personal:
            print("".center(20,"-"))
            print(persona)
            Novedades.mostrarNovedades(persona.getLegajo(),persona.getSueldoBasico())
    
    def sueldoMasBajo(self,Novedades):
        sueldoMasBajo = 1000000

        for persona in self.__personal:
            for nov in Novedades.getLista():
                if(nov.getLegajo() == persona.getLegajo()):
                    persona.modificarSueldo(nov.getCodigo(),nov.getImporte())
                    #Sobrecargo metodo __lt__ 
                    if(persona < sueldoMasBajo):
                        sueldoMasBajo = persona.getSueldoACobrar()
        print("El sueldo mas bajo es de ${}".format(sueldoMasBajo))
