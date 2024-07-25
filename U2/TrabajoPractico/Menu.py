from ManejadorNovedades import manejadorNovedades
from ManejadorPersonal import manejadorPersonal
import os


class menu:
    sueldoALiquidar = 1
    ListadoOrdenado = 2
    obtenerSueldoBajo = 3
    salir = 0
    __op = None

    def __init__(self, op = None):
        self.__op = op
        self.__Personal = manejadorPersonal()
        self.__Novedades = manejadorNovedades()

    def opciones(self):
        continuar = True
        self.__Personal.CargarPersonal()
        self.__Novedades.CargarNovedades(self.__Personal)

        while continuar:
            print("MENU".center(30,"-"))
            print("[{}] Ingrese legajo de una persona y obtenga sueldo a liquidar".format(self.sueldoALiquidar))
            print("[{}] Listar alfabeticamente el personal POR APELLIDO".format(self.ListadoOrdenado))
            print("[{}] Obtener el sueldo a cobrar mas bajo de todo el personal".format(self.obtenerSueldoBajo))
            print("[{}] Salir del menu".format(self.salir))
            self.__op = int(input("Ingrese opcion deseada\n"))
            os.system("cls")

            if(self.__op == 1):
                LegajoPersona = int(input("Ingrese legajo del que desea obtener sueldo a liquidar\n"))
                os.system("cls")
                self.__Personal.sueldoLiquidarLegajo(LegajoPersona,self.__Novedades)
            elif(self.__op == 2):
                self.__Personal.ordenar(self.__Novedades)
                input("Presione ENTER para continuar")
                os.system("cls")
            elif(self.__op == 3):
                self.__Personal.sueldoMasBajo(self.__Novedades)
                input("Presione ENTER para continuar")
                os.system("cls")
            elif(self.__op == 0):
                continuar = not continuar
                print("MUCHAS GRACIAS")
            else:
                print("Opcion inexistente")
            
