from Manejador import Manejador
from PlanAhorro import PlanAhorro
import os

class Menu:
    Listar = 1
    ActualizarValor = 2
    CuotasMenores = 3
    MontoLicitar = 4
    ModCantCuotas = 5
    Salir = 0
    __op = 0

    def __init__(self,op = 0):
        self.__op = op
        self.__Planes = Manejador()
        self.__Planes.CargarPlanes()


    def opciones(self):
        continuar = True

        while continuar:
            print("Menu".center(20,"-"))
            print("{} Listar Planes".format(self.getOp1()))
            print("{} Actualizar valor de los planes".format(self.getOp2()))
            print("{} Cuotas menores a un valor ingresado por teclado".format(self.getOp3()))
            print("{} Monto necesario para poder licitar vehiculos ".format(self.getOp4()))
            print("{} Modificar cuotas para licitar auto de un plan".format(self.getOp5()))
            print("{} Salir".format(self.getSalir()))
            self.__op = int(input("INGRESE OPCION DESEADA \n"))
            os.system("cls")
            
            if(self.__op == 1):
                self.__Planes.listar()
                input("ENTER PARA CONTINUAR")
                os.system("cls")
            elif(self.__op == 2):
                self.__Planes.ActualizarValor()
                input( "ENTER PARA CONTINUAR")
                os.system("cls")
            elif(self.__op == 3):
                self.__Planes.cuotasMenores()
                input( "ENTER PARA CONTINUAR")
                os.system("cls")
            elif(self.__op == 4):
                self.__Planes.montoLicitar()
                input( "ENTER PARA CONTINUAR")
                os.system("cls")
            elif(self.__op == 5):
                cod = int (input("Ingrese codigo de plan que desea modificar\n"))
                planAModificar = self.__Planes.buscar(cod)
                if(planAModificar.getCodigo() == cod):
                    cuotas = int(input("Actualice cantidad de cuotas para solicitar el vehiculo\n Ingrese valor\n"))
                    planAModificar.modificarCuotasLicitar(cuotas)
                    planAModificar.mostrarCuotasLicitar()
                    input( "ENTER PARA CONTINUAR")
                    os.system("cls")
                else: 
                    print("No se puede ejecutar la opcion debido a que no se encontro el plan")
                    input( "ENTER PARA CONTINUAR")
                    os.system("cls")
    
            elif(self.__op == 0):
                continuar = not continuar
                print("MUCHAS GRACIAS".center(20,"-"))
            else:
                print("OPCION INEXISTENTE")
                input("ENTER PARA CONTINUAR")
                os.system("cls")


    @classmethod
    def getOp1(cls):
        return cls.Listar    
    @classmethod
    def getOp2(cls):
        return cls.ActualizarValor
    @classmethod
    def getOp3(cls):
        return cls.CuotasMenores
    @classmethod
    def getOp4(cls):
        return cls.MontoLicitar
    @classmethod
    def getOp5(cls):
        return cls.ModCantCuotas
    @classmethod
    def getSalir(cls):
        return cls.Salir