from ManejadorCalefactores import manejadorCalefactores
from ClaseCalefactorGas import calefactorGas
from ClaseCalefactorElectrico import calefactorElectrico
import os

class menu:
    __op = None
    __Calefactores = None

    def __init__(self,dimension,op = 0):
        self.__op = op
        self.__Calefactores = manejadorCalefactores(dimension)

    def opciones(self):
        continuar = True
        self.__Calefactores.carfarCalefactoresElectricos()
        self.__Calefactores.cargarCalefactoresGas()
        costoCalefactorGas = 0 
        costoCalefactorElectrico = 0

        while continuar:
            print("MENU".center(20,"-"))
            print("[1] Ingresar por teclado costo y cantidad por m³")
            print("[2] Ingresar por teclado costo del kilowatt")
            print("[3] Mostrar tipo de calefactor y sus datos")
            print("[0] Para salir del menu")
            self.__op = int(input("Ingrese opcion deseada\n"))
            os.system("cls")

            if(self.__op == 1):
                GasMenorC = self.opcion1(costoCalefactorGas)
            elif(self.__op == 2):
                ElectricoMenorC = self.opcion2(costoCalefactorElectrico)
            elif(self.__op == 3):
                self.opcion3(costoCalefactorGas,costoCalefactorElectrico,GasMenorC,ElectricoMenorC)
            elif(self.__op == 0):
                continuar = not continuar
                print("muchas gracias")
            else:
                print("opcion incorrecta, pruebe de nuevo")

    def opcion1(self,costoCalefactorGas):
        costom = int(input("Ingrese el costo por m³\n"))
        cantidadm = int(input("Ingrese cantidad que se estima consumir por m³\n"))
        CalefactorMenorConsumo = self.__Calefactores.getCalefactorGasMenorConsumo()
        costoCalefactorGas = CalefactorMenorConsumo.getCalorias()*costom*cantidadm
        print("El calefactor de menor consumo es de la marca: {} modelo: {} y tiene un costo de ${}".format(CalefactorMenorConsumo.getMarca(),CalefactorMenorConsumo.getModelo(),costoCalefactorGas))
        return CalefactorMenorConsumo
        
    def opcion2(self,ConsumoCalefElec):
        costok = int(input("Ingrese el costo del kilowatt/h\n"))
        cantidadH = int(input("Ingrese cantidad estimada a consumir por hora\n"))
        CalefactoElectricoMenorConsumo = self.__Calefactores.getCalefactorElectricoMenorConsumo()
        ConsumoCalefElec = (CalefactoElectricoMenorConsumo.getPotencia())*costok*cantidadH  
        print("El calefactor electrico de menor consumo es de marca:{} modelo:{} y tiene un costo de ${}".format(CalefactoElectricoMenorConsumo.getMarca(),CalefactoElectricoMenorConsumo.getModelo(),CalefactoElectricoMenorConsumo.getPotencia()*costok*cantidadH ))
        return CalefactoElectricoMenorConsumo

    def opcion3(self,costoGas,costoElectrico,CalefGas,CalefElec):
        
        if (costoGas<costoElectrico):
            print("Calefactor de menor consumo es de gas:")
            print(CalefGas)
        else:
            print("Calefactor de menor consumo es electrico:")
            print(CalefElec)