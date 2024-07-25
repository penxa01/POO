import os
from Manejador import Manejador

class Menu:
    MaxMinVariables= 1
    promedioHoras = 2
    ListarXdia = 3
    Salir = 0
    __Registro = Manejador()
    __op = 0

    def __init__( self, op):
        self.__op = op

    def opciones(self):
        self.__Registro.CargarDatos()
        continuar = True
        while continuar :
            print("MENU".center(20,"-"))
            print("[{}]Mostrar hora y dia de menor y mayor valor".format(self.MaxMinVariables))
            print("[{}]Promedio de temperatura por horas".format(self.promedioHoras))
            print("[{}]Listado de valores por dia".format(self.ListarXdia))
            print("[{}]Salir del menu".format(self.Salir))
            print("".center(20,"-"))
            self.__op = int(input("Ingrese opcion deseada\n"))
            os.system("cls")

            if(self.__op == 1):
                self.__Registro.DHMinimoMaximoVar()
                print("".center(20,"-"))
                input("ENTER para continuar")
                os.system("cls")
            elif(self.__op == 2):
                self.__Registro.Promedio()
                print("".center(20,"-"))
                input("ENTER para continuar")
                os.system("cls")
            elif(self.__op ==3):
                dia= int(input("Ingrese el dia del cual desea ver el registro\n"))
                self.__Registro.mostrarRegistroDiario(dia)
                print("".center(20,"-"))
                input("ENTER para continuar")
                os.system("cls")
            elif(self.__op == 0):
                continuar = not continuar
            else: 
                print("Opcion inexistente")
                os.system("cls")
            
