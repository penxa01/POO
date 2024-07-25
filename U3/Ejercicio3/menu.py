from ManejadorEquipo import manejadorEquipos
from ManejadorContratos import manejadorContratos
from ManejadorJugadores import manejadorJugadores
from ClaseJugador import jugador
from ClaseContrato import contrato
import os
from datetime import date
import csv

class Menu:
    __op = None
    __Jugadores = None
    __Contratos  = None
    __Equipos = None
    
    def __init__(self,manejadorJugadores = None,manejadorContratos = None,manejadorEquipo = None,op = 0):
        self.__op = op
        self.__Jugadores = manejadorJugadores
        self.__Contratos = manejadorContratos
        self.__Equipos = manejadorEquipo

    
    def opciones(self):
        print("Se cargan datos de los equipos")
        self.__Equipos.cargarArchivo()

        continuar = True

        while continuar:
            input("ENTER PARA CONTINUAR")
            os.system("cls")
            print("MENU".center(20,"-"))
            print("[1] Generar contrato para un jugador")
            print("[2] Consultar jugadores contratados")
            print("[3] Consultar contratos")
            print("[4] Obtener importe de contratos de un equipo")
            print("[5] Guardar informacion de los contratos en un archivo y SALIR del menu")


            self.__op = int(input("Ingrese opcion deseada\n"))

            if(self.__op == 1):
                self.opcion1()
            elif(self.__op == 2):
                self.opcion2()
            elif(self.__op == 3):
                self.opcion3()
            elif(self.__op == 4):
                self.opcion4()
            elif(self.__op == 5):
                self.opcion5("Contratos.csv",self.__Contratos.getLista())
                continuar = not continuar
                print("Muchas gracias")
            else: 
                print("Opcion inexistente, ingrese nuevamente")
    
    def opcion1(self):
        print("CARGA DE DATOS DEL JUGADOR".center(40,"-"))
        nombrePila = input("Ingrese nombre de pila del jugador\n".capitalize())
        os.system("cls")
        apellido = input("Ingrese apellido del jugador\n".capitalize())
        os.system("cls")
        nombreJugador = nombrePila+" "+apellido
        dni = int(input("Ingrese documento nacional de identidad(DNI)\n"))
        os.system("cls")
        city = input("Ingrese ciudad natal\n")
        os.system("cls")
        contry = input("Ingrese pais de origen\n")
        os.system("cls")
        print("Ingrese fecha de nacimiento del jugador")
        dia = input("DIA--> ")
        mes = input("MES--> ")
        año = input("AÑO--> ")
        fecha = date(int(año),int(mes),int(dia))
        os.system("cls")
        NuevoJugador = jugador(nombreJugador,dni,city,contry,fecha)

        equipoDeContrato = input("Ingrese nombre del equipo con el cual se realizara el contrato\n")
        buscar = self.__Equipos.buscarEquipo(equipoDeContrato)
        while(buscar == -1):
            equipoDeContrato = input("El equipo ingresado no existe o esta mal escrito, INGRESE NUEVAMENTE\n")
            buscar = self.__Equipos.buscarEquipo(equipoDeContrato)
        
        print("Equipo ingresado encontrado")
        print(self.__Equipos.getEquipo(buscar))
        input("ENTER PARA CONTINUAR")
        os.system("cls")

        print("CREAR CONTRATO".center(20,"-"))
        print("Ingrese fecha de inicio de contrato")
        dia = input("DIA--> ")
        mes = input("MES--> ")
        año = int(input("AÑO--> "))
        fechaInicio = date(año,int(mes),int(dia))
        os.system("cls")
        """print("El contrato finalizara 2 años pasados el inicio del mismo")
        año += 2"""
        print("Ingrese fecha de fin de contrato")
        dia = input("DIA--> ")
        mes = input("MES--> ")
        año = int(input("AÑO--> "))
        fechaFin = date(año,int(mes),int(dia))
        os.system("cls")
        pago = float(input("Ingrese pago mensual del jugador\n"))
        contratoNuevo = contrato(fechaInicio,fechaFin,pago,NuevoJugador,self.__Equipos.getEquipo(buscar))
        
        #Seteamos el contrato en cada clase
        self.__Contratos.agregarContrato(contratoNuevo)
        NuevoJugador.setContrato(contratoNuevo)
        self.__Jugadores.agregarJugador(NuevoJugador)
        self.__Equipos.setContrato(buscar,contratoNuevo)


    def opcion2(self):
        DniJugador = int(input("Ingrese DNI del jugador que desea buscar\n"))
        busqueda = self.__Jugadores.buscarJugador(DniJugador)
        while(busqueda == -1):
            DniJugador = input("El DNI ingresado no existe o esta mal escrito, INGRESE NUEVAMENTE\n")
            busqueda = self.__Equipos.buscarEquipo(DniJugador)
        
        print("Jugador encontrado")
        print("EQUIPO".center(20,"-"))
        print("{}".format(self.__Jugadores.getEquipo(busqueda)))
        print("Fecha de finalizacion de contrato:{}".format(self.__Jugadores.getFechaFin(busqueda)))

    def opcion3(self):
        equipoContratos = input("Ingrese equipo del cual quiere consultar contratos\n")
        buscar = self.__Equipos.buscarEquipo(equipoContratos)
        while(buscar == -1):
            equipoContratos = input("El equipo ingresado no existe o esta mal escrito, INGRESE NUEVAMENTE\n")
            buscar = self.__Equipos.buscarEquipo(equipoContratos)
        
        print("Equipo ingresado encontrado")
        equipoIngresado = self.__Equipos.getEquipo(buscar)
        print(equipoIngresado)
        input("ENTER PARA CONTINUAR")
        os.system("cls")
        equipoIngresado.contratosVencimiento()

    def opcion4(self):
        equipoContratos = input("Ingrese equipo del cual quiere consultar importe total en jugadores\n")
        buscar = self.__Equipos.buscarEquipo(equipoContratos)
        while(buscar == -1):
            equipoContratos = input("El equipo ingresado no existe o esta mal escrito, INGRESE NUEVAMENTE\n")
            buscar = self.__Equipos.buscarEquipo(equipoContratos)

        print("Equipo ingresado encontrado")
        equipoIngresado = self.__Equipos.getEquipo(buscar)
        print(equipoIngresado)
        input("ENTER PARA CONTINUAR")
        os.system("cls")
        equipoIngresado.getImporteTotal()

        

    def opcion5(self,nombreArchivo,listaContratos):
        archivo = open(nombreArchivo, "w")
        writer = csv.writer(archivo, delimiter=";")
        for contr in listaContratos:

            nombreEquipo = contr.getEquipo().getNombre()
            fechaInicio = contr.getFechaInicio()
            fechaFin = contr.getFechaFin()
            pagoMensual = contr.getPago()
            dni = contr.getJugador().getDNI()
            writer.writerow([dni, nombreEquipo, "{}/{}/{}".format(fechaInicio.day, fechaInicio.month, fechaInicio.year), "{}/{}/{}".format(fechaFin.day, fechaFin.month, fechaFin.year), pagoMensual])

