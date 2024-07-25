import os
from ClaseListaEnlazada import Lista
from ClaseAparatos import aparato
from ClaseTelevisor import Televisor
from ClaseHeladera import Heladera
from ClaseLavaropa import Lavarropa
from ObjectEncoder import ObjetcEncoder
from InterfazLista import ILista

class menu:
    __op = None
    __manejador = None
    __ObjEncoder = None

    def __init__(self,op = 0):
        self.__op = op 
        self.__ObjEncoder = ObjetcEncoder()
    
    def setLista(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "aparatoselectronicos.json")

        diccionario = self.__ObjEncoder.leerJSONArchivo(Archivo)
        NuevaLista = self.__ObjEncoder.decodificarDiccionario(diccionario)
        self.__manejador = NuevaLista
    
    def guardarLista(self):
        diccionario = self.__manejador.aJson()
        self.__ObjEncoder.guardarJSONArchivo(diccionario,"aparatoselectronicos.json")
    
    def opciones(self):
        continuar = True

        while continuar:
            self.mostrarOpciones()
            self.__op = int(input("Ingrese opcion deseada\n"))
            os.system("cls")

            if (self.__op == 1):
                self.op1()
            elif(self.__op == 2):
                self.op2()
            elif(self.__op == 3):
                self.op3()
            elif(self.__op == 4):
                self.op4()
            elif(self.__op == 5):
                self.op5()
            elif(self.__op == 6):
                self.op6()
            elif(self.__op == 7):
                continuar = not continuar
                print("Muchas Gracias")
                self.guardarLista()
            else:
                print("Opcion inexistente")
    
    def op1(self):
        NuevoAparato = self.ingresador()
        if NuevoAparato != None:
            
            indice = int(input("Ingrese posicion en la que desea agregar el aparato\n"))
            os.system("cls")
            try:
                self.__manejador.insertarAparato(NuevoAparato,indice)
            except ValueError:
                print("Ingrese un valor entero")
        else:
            print("El aparato no se genero correctamente, la carga NO se realizo")        
    def op2(self):
        Aparatex =self.ingresador()
        self.__manejador.agregarAparato(Aparatex)
        print("Aparato agregado con exito")
        input("ENTER PARA CONTINUAR")
        os.system("cls")

    def op3(self):
        indice = int(input("Ingrese posicion de la lista que desea ver el dato\n"))
        try:
            print(self.__manejador.mostrarAparato(indice))
        except IndexError:
            print("Fuera de indice")

    def op4(self):
        self.__manejador.aparatosPhillips()
    def op5(self):
        self.__manejador.mostrarLavarropas()
    def op6(self):
        self.__manejador.mostrarTodosAparatos()
    
    def opcionesOpcion1(self):
        print("[1] Para insertar una TELEVISION")
        print("[2] Para insertar una HELADERA")
        print("[3] Para insertar un LAVARROPAS")
        print("[0] Para CANCELAR")

        
    def mostrarOpciones(self):
        print("MENU".center(30,"-"))
        print("[1] Insertar un elemento en una posicion determinada")
        print("[2] Agregar un aparato a la coleccion")
        print("[3] Dada la poscicion de la lista, mostrar el tipo de objeto que se encuentra en la posicion")
        print("[4] Mostrar la cantidad de cada aparato de marca Phillips que haya en la coleccion")
        print("[5] Mostrar todos los lavarropas que tienen carga superior")
        print("[6] Mostrar todos los aparatos que la empresa tiene a la venta(Marca,Pais de fabricacion e importe)")
        print("[7] Para guardar el archivo y SALIR del menu")
    
    def ingresador(self):
        continuar = True
        NuevoAparato = None
        retorno = None
        print("Datos generales del aparato\n")
        marca = input("Ingrese marca del aparato -->").capitalize()
        modelo = input("Ingrese modelo del aparato -->").capitalize()
        color = input("Ingrese color -->").capitalize()
        pais = input("Ingrese pais de fabricacion -->").capitalize()
        try:
            precioBase = float(input("Ingrese precio base -->"))
            try:
                os.system("cls")
                while continuar:
                    self.opcionesOpcion1()
                    opcion = int(input("Ingrese opcion deseada\n"))
                    os.system("cls")
                    try:
                        if(opcion == 1):
                            try:
                                tipoPantalla = input("Ingrese tipo de pantalla que posee la TV\n").upper()
                                os.system("cls")
                                pulgadas = int(input("Ingrese pulgadas del TV\n"))  
                                os.system("cls")
                                definicion = input("Ingrese definicion de la TV\n").upper()
                                os.system("cls")
                                conexion = input("Posee conexion a internet? SI/NO\n").lower()

                                if(conexion == "si"):
                                    conexion = True
                                else:
                                    conexion = False
                                NuevoAparato = Televisor(marca,modelo,color,pais,precioBase,tipoPantalla,pulgadas,definicion,conexion)
                                continuar = not continuar
                            except ValueError:
                                print("Valores del televisor erroneos")

                        elif(opcion == 2):
                            try:
                                capacidad = int(input("Ingrese capacidad de la heladera\n"))
                                os.system("cls")
                                freezer = input("Tiene freezer?Si/No\n").lower()
                                os.system("cls")
                                ciclica = input("La heladera es ciclica? Si/No\n").lower()
                                os.system("cls")

                                if(freezer == "si"):
                                    freezer = True
                                else:
                                    freezer = False
                                NuevoAparato = Heladera(marca,modelo,color,pais,precioBase,capacidad,freezer,ciclica)
                                continuar = not continuar
                            except ValueError:
                                print("Valores ingresados INCORRECTOS")

                        elif(opcion == 3):
                                        
                            capacidadLitros=int("Ingrese capacidad del lavarropas\n")
                            os.system("cls")
                            velocidad = int("Ingrese velocidad de centrifugado\n")
                            os.system("cls")
                            cantidadProg = int(input("Ingrese la cantidad de programas\n"))
                            os.system("cls")
                            tipoCargas = input("Que tipo de carga tiene? Frontal/Superior").capitalize()
                            os.system("cls")
                            try:
                                NuevoAparato = Lavarropa(marca,modelo,color,pais,precioBase,capacidadLitros,velocidad,cantidadProg,tipoCargas)
                                continuar = not continuar
                            except ValueError:
                                print("Los valores ingresados son incorrectos")
                        elif(opcion == 0):
                            print("Cancelo la opcion")
                            input("ENTER PARA CONTINUAR")
                            os.system("cls")
                            continuar = not continuar
                        retorno = NuevoAparato
                    except ValueError:
                        print("El valor ingresado de opcion es incorrecto")
            except ValueError:
                print("Un valor ingresado es erroneo")
        except ValueError:
            print("El precio base es erroneo")
        return retorno