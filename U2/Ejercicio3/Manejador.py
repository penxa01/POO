import os
import csv
from RegistroMeteorologico import Registro

 
class Manejador:
    __Lista = []

    def __init__(self):
        for i in range(30):
            self.__Lista.append([])
            for j in range(24):
                Reg = Registro(0,0,0)
                self.__Lista[i].append(Reg)
    
    def mostrar(self):
        for dia in range(30):
            for hora in range (24):
                print(self.__Lista[dia][hora],end=" ")
            print("\n")

    def CargarDatos(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "DatosClima.csv")
        archivo =open(Archivo)
        reader= csv.reader(archivo, delimiter = ";")
        cabecera = True
        for comp in reader:
            if cabecera:
                cabecera = not cabecera
            else:
                RegNuevo = Registro(float(comp[2]),int(comp[3]),float(comp[4]))
                self.__Lista[int(comp[0])-1][int(comp[1])-1] = RegNuevo
        archivo.close()

    
    def mostrarRegistroDiario(self,dia):
        print("Dia: {}".format(dia))
        print("Hora     Temperatura     Humedad     Presion")
        for hora in range(24):
            print("{}hs       {}".format(hora,self.__Lista[dia-1][hora]))

    def DHMinimoMaximoVar(self):
        minTemp = 99
        MaxTemp = 0
        minHumed = 100
        MaxHumed = 0
        minPresion = 100
        MaxPresion = 0
        for dia in range(30):
            for hora in range(24):
                if (self.__Lista[dia][hora].getTemperatura()> MaxTemp):
                    MaxTemp = self.__Lista[dia][hora].getTemperatura()
                    RegistroMaxTempD = dia
                    RegistroMaxTempH = hora
                if (self.__Lista[dia][hora].getTemperatura()< minTemp):
                    minTemp = self.__Lista[dia][hora].getTemperatura()
                    RegistrominTempD = dia
                    RegistrominTempH = hora
                if(self.__Lista[dia][hora].getHumedad() > MaxHumed):
                    MaxHumed = self.__Lista[dia][hora].getHumedad()
                    RegistroMaxHumedD = dia
                    RegistroMaxHumedH = hora
                if(self.__Lista[dia][hora].getHumedad()< minHumed):
                    minHumed = self.__Lista[dia][hora].getHumedad()
                    RegistrominHumedD= dia
                    RegistrominHumedH= hora
                if(self.__Lista[dia][hora].getPresion()> MaxPresion):
                    MaxPresion =self.__Lista[dia][hora].getPresion()
                    RegistroMaxPresionD = dia
                    RegistroMaxPresionH = hora
                if(self.__Lista[dia][hora].getPresion()< minPresion):
                    minPresion = self.__Lista[dia][hora].getPresion()
                    RegistrominPresionD = dia
                    RegistrominPresionH = hora


        print("El dia {} a las {}hs se registro la maxima temperatura de {}°C".format(RegistroMaxTempD+1,RegistroMaxTempH+1,MaxTemp))
        print("El dia {} a las {}hs se registro la minima temperatura de {}°C" .format(RegistrominTempD+1,RegistrominTempH+1,minTemp))           
        print("El dia {} a las {}hs se registro la maxima humedad de {}%".format(RegistroMaxHumedD+1,RegistroMaxHumedH+1,MaxHumed))     
        print("El dia {} a las {}hs se registro la minima humedad de {}%".format(RegistrominHumedD+1,RegistrominHumedH+1,minHumed))
        print("El dia {} a las {}hs se registro la maxima presion de {}".format(RegistroMaxPresionD+1,RegistroMaxPresionH+1,MaxPresion))
        print("El dia {} a las {}hs se registro la minima presion de {}".format(RegistrominPresionD+1,RegistrominPresionH+1,minPresion))
    
    def Promedio(self):
        acumulador = 0
        for hora in range(24):
            for dia in range(30):
                acumulador += self.__Lista[dia][hora].getTemperatura()
            acumulador /= 30
            print("La temperatura promedio mensual es de {}°C a las {}hs".format(round(acumulador,2),hora+1))
            print("".center(20,"-"))
            acumulador = 0
