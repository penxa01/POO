from ManejadorFlores import flores
from ManejadorRamos import ramos
import os

class menu:
    __op = None
    registrarRamo = 1
    mostrarModaFlores = 2
    floresMasVendidasPorTamaño = 3
    salir = 0

    __listadoFlores = None
    __registroRamos = None

    def __init__(self, op = 0):

        self.__op = op
        self.__listadoFlores = flores()
        self.__registroRamos = ramos()
    
    def opciones(self):
        self.__listadoFlores.cargarArchivoFlores()
        continuar = True

        while continuar:
            print("[{}] Registrar un ramo vendido".format(self.registrarRamo))
            print("[{}] Mostrar 5 flores mas pedidas de un ramo".format(self.mostrarModaFlores))
            print("[{}] Mostrar flores vendidas por tamaño de ramo".format(self.floresMasVendidasPorTamaño))
            print("[{}] Para salir del menu".format(self.salir))
            self.__op = int(input("Ingrese opcion que desea ejecutar\n"))
            os.system("cls")

            if(self.__op ==1):
                self.__registroRamos.agregarRamo(self.__listadoFlores)
                os.system("cls")
            elif(self.__op == 2):
                self.__listadoFlores.mostrarModaFlores()
                input("ENTER PARA CONTINUAR")
                os.system("cls")
            elif(self.__op == 3):
                tamañoPorTeclado = input("Ingrese el tamaño por teclado que desea analizar\n")
                self.__registroRamos.porTamaño(tamañoPorTeclado)
                input("ENTER PARA CONTINUAR")
                os.system("cls")
            elif(self.__op == 0):
                print("Muchas gracias")
                continuar = not continuar
            else:
                print("Opcion inexistente")