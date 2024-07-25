from ManejadorFacultad import Manejador
import os

class menu:

    __op = 0
    __mostrarCodigo = 1
    __mostrarCarrera = 2
    __salir = 0

    __Facultades = None

    def __init__(self,op = None):

        self.__op = op
        self.__Facultades = Manejador()

    def opciones(self):
        self.__Facultades.cargar()
        print("CARGA DE DATOS EXITOSA")
        continuar = True
        BandInt = False

        while continuar:
            input("Presione ENTER para continuar")
            os.system("cls")

            print("[{}] Para ingresar un codigo de facultad y listar".format(self.__mostrarCodigo))
            print("[{}] Ingresar nombre de carrera y mostrar datos".format(self.__mostrarCarrera))
            print("[{}] Para salir del menu".format(self.__salir))

        
            self.__op = int(input("Ingrese opcion deseada \n"))
            os.system("cls")

            if (self.__op == 1):
                codigo = int(input("Ingrese codigo de facultad que desea mostrar\n"))
                os.system("cls")
                self.__Facultades.listar(codigo)
            elif(self.__op == 2):
                carreraBuscar = input("Ingrese nombre de carrera deseada\n")
                os.system("cls")
                self.__Facultades.InfoCarrera(carreraBuscar)
            elif(self.__op == 0):
                print("Muchas gracias!")
            else:
                print("Opcion inexistente")

