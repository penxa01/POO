import os 
import csv
from PlanAhorro import PlanAhorro

class Manejador: 
    __ListaPlanes = []

    def __init__(self):
        self.__ListaPlanes = []

    def CargarPlanes(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "planes.csv")
        archivo = open(Archivo)
        reader = csv.reader(archivo,delimiter = ";")

        for comp in reader:
            Plan = PlanAhorro(int(comp[0]),comp[1],comp[2],float(comp[3]))
            self.__ListaPlanes.append(Plan)
        
        archivo.close()
    
    def listar(self):
        for i in range(len(self.__ListaPlanes)):
            print(self.__ListaPlanes[i])
            print("".center(20,"-"))
        return
    
    def ActualizarValor(self):

        for i in range(len(self.__ListaPlanes)):
            print("COD. PLAN: {}".format(self.__ListaPlanes[i].getCodigo()))
            print("MODELO: {}".format(self.__ListaPlanes[i].getModelo()))
            print("VERSION: {}".format(self.__ListaPlanes[i].getVersion()))
            ValorNuevo = float(input("Ingrese valor actualizado del vehiculo\n"))
            self.__ListaPlanes[i].modificarValor(ValorNuevo)
            print("Valor actualizado")
            input("Presione ENTER para continuar")
            os.system("cls")

        return    
    
    def cuotasMenores(self):
        Comparar = float(input("Ingrese valor de cuota a comparar\n"))
        print("Vehiculos con valor de cuota menor a ${}".format(Comparar))
        print("".center(20,"-"))
        for i in range(len(self.__ListaPlanes)):
            valorCuotaPlan = ((self.__ListaPlanes[i].getValor()/ self.__ListaPlanes[i].retornaCuotas())+ self.__ListaPlanes[i].getValor()) * 0.10
            if (valorCuotaPlan< Comparar):
                print("COD. PLAN: {}".format(self.__ListaPlanes[i].getCodigo()))
                print("MODELO: {}".format(self.__ListaPlanes[i].getModelo()))
                print("VERSION: {}".format(self.__ListaPlanes[i].getVersion()))
                print("Valor de cuota: ${}".format(round(valorCuotaPlan,2)))
                print("".center(20,"-"))
            
        return
    
    def montoLicitar(self):

        for i in range(len(self.__ListaPlanes)):
            print(self.__ListaPlanes[i])
            valorCuotaPlan = ((self.__ListaPlanes[i].getValor()/ self.__ListaPlanes[i].retornaCuotas())+ self.__ListaPlanes[i].getValor()) * 0.10
            monto= self.__ListaPlanes[i].retornarCuotasLicitar()* valorCuotaPlan
            print("MONTO PARA LICITAR VEHICULO: ${}".format(round(monto,2)))
            print("".center(20,"-"))
        return

    def buscar(self,codigo):
        i = 0

        while (self.__ListaPlanes[i].getCodigo() != codigo):
            i += 1
        if(self.__ListaPlanes[i].getCodigo() == codigo):
            plan = self.__ListaPlanes[i]
            print("Plan encontrado")
            print(plan)
        else:
            print("Plan no existente")
        return plan


            
