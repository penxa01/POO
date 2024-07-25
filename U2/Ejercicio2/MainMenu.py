import os
from ManejadorViajeros import Manejador
from ViajeroFrecuente import ViajeroFrecuente


if __name__== "__main__":

    Lista = Manejador()
    Lista.GenerarLista()
    Lista.Listar()
    NroViaj= int(input("Ingrese nro de viajero del cual desea consultar\n"))
    Viajero= Lista.Buscar(NroViaj)
    
    continuar = True

    while continuar:
        print("MENU".center(20,"-"))
        print("[1] Para consultar cantidad de millas")
        print("[2] Para acumular millas")
        print("[3] Para canjear millas")
        print("[0] Para SALIR del menu")

        op = int( input("INGRESE OPCION POR TECLADO\n"))
        os.system("cls")
        if ( op == 1):
            print("".center(20,"-"))
            print("Consultar cantidad de millas\n")
            print(Viajero.cantidadTotalMillas())
        elif(op == 2):
            Acum = int(input("Ingrese cantidad de millas que desea acumular\n"))
            Viajero.acumularMillas(Acum)
        elif(op == 3):
            Canj = int(input("Ingrese millas que desea canjear\n"))
            Viajero.canjearMillas(Canj)
        elif(op == 0):
            continuar = not continuar
    

