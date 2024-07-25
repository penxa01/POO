import numpy as np
from ClaseCamas import Cama
from ClaseMedicamentos import medicamento
import os
import csv
from datetime import date


class ManejadorCamas():
    __incremento = 5
    __cantidad = 0
    __dimension = 30
    __camas = None

    def __init__(self,dimension = 30, incremento = 5):
        self.__incremento = incremento
        self.__camas = np.empty(dimension,dtype = Cama)
    
    def agregarCamas(self,C):

        if (self.__cantidad == self.__dimension):
            self.__dimension += self.__incremento
            self.__camas.resize(self.__dimension)
        self.__camas[self.__cantidad] = C
        self.__cantidad += 1
    
    def CargarCamas(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "camas.csv")
        archivo = open(Archivo)
        reader = csv.reader(archivo,delimiter = ";")
        cabeza = True
        for comp in reader:
            if cabeza:
                cabeza = not cabeza
            else:
                NuevaCama = Cama(int(comp[0]),int(comp[1]),bool(comp[2]),comp[3],comp[4],comp[5])
                self.agregarCamas(NuevaCama)
        
        archivo.close()

    def BuscarPaciente(self,Nombre):
        i = 0
        while (i < 30) and (self.__camas[i].getNyA().lower() != Nombre.lower()):
            i += 1
        if i == 30:
            i = -1
        return i

    def DarAlta(self,Medicamentos):
        paciente = input("Ingrese paciente que desea dar de alta\n")
        indicePaciente = self.BuscarPaciente(paciente)
        if( indicePaciente != -1)and (self.__camas[indicePaciente].getEstado()):
            print("PACIENTE ENCONTRADO".center(20,"-"))
            fecha = date.today()
            fecha = ("{}/{}/{}".format(fecha.day,fecha.month,fecha.year))
            self.__camas[indicePaciente].regAlta(fecha)
            print("".center(20,"-"))
            print("Paciente:{}     Cama:{}     Habitacion:{}\nDiagnostico:{}       Fecha de internacion:{}\nFecha de Alta:{}".format(self.__camas[indicePaciente].getNyA(),self.__camas[indicePaciente].getID(),self.__camas[indicePaciente].getNroH(),self.__camas[indicePaciente].getDiagnostico(),self.__camas[indicePaciente].getInternacion(),self.__camas[indicePaciente].getAlta()))
            print("".center(20,"-"))
            print("Medicamento/monodroga                Presentacion                    Cantidad              Precio")
            Total = 0
            for i in range(len(Medicamentos)):
                if(Medicamentos[i].getIdCama() == self.__camas[indicePaciente].getID()):
                    print("{0:^30}{1:^30}{2:^30}{3:^7}".format(Medicamentos[i].getMonodroga(),Medicamentos[i].getPresentacion(),Medicamentos[i].getCantidadAplicada(),Medicamentos[i].getPrecio()))
                    Total += Medicamentos[i].getPrecio()
            print("Total Adeudado:{0:82}".format(Total))
        else:
            print("Paciente no existente")

            



    def Listar(self):
        diagnostico = input("Ingrese diagnostico que desea\n")
        os.system("cls")
        print("Pacientes con diagnostico de {}".format(diagnostico).lower())
        for i in range(30):
            if(self.__camas[i] != None):
                if (self.__camas[i].getEstado() == True):
                    if(self.__camas[i].getDiagnostico().lower() == diagnostico):
                        print("".center(20,"-"))
                        print(self.__camas[i])
                        print("".center(20,"-"))

