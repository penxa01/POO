from ClaseLista import ListaEnlazada
from NuevasInterfaces import IDirector, ITesorero
from ObjectEncoder import ObjectEncoder
from ClasePersonal import personal
from ClaseDocente import docente
from ClaseInvestigador import investigador
from ClasePersonalApoyo import personalApoyo
from ClaseDocenteInvestigador import docenteInvestigador
import os

class menu:
    __manejador = None
    __encoder = None
    __op = None

    def __init__(self,op = 0):
        self.__encoder = ObjectEncoder()
        self.__manejador = None
    
    def setLista(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "personal.json")

        diccionario = self.__encoder.leerJSONArchivo(Archivo)
        self.__manejador = self.__encoder.decodificarDiccionario(diccionario)
    
    def muestraMenu(self):
        print("MENU".center(30,"-"))
        print("[1] Insertar personal en una posicion de la lista")
        print("[2] Agregar personal a la lista")
        print("[3] Dada una posicion, mostrar el tipo de personal que se encuentra")
        print("[4] Ingresa nombre de carrera y listar ordenado")
        print("[5] Dada un area de investigacion, contar docente investigador y investigadores")
        print("[6] Ordenar por nombre la coleccion")
        print("[7] Dada una categoria, listar datos y total de dinero a solicitar")
        print("[8] Mas opciones...")
        print("[0] Para guardar los datos en un archivo.json")
    
    def guardarLista(self):
        diccionario = self.__manejador.toJson()
        self.__encoder.guardarJSONArchivo(diccionario,"personal.json")
    
    def op1(self):
        NuevoPersonal = self.ingresador()
        if isinstance(NuevoPersonal,personal):
            indice = int(input("Ingrese posicion donde desea insertar\n"))
            os.system("cls")
            self.__manejador.insertarPersonal(NuevoPersonal,indice)
        else:
            raise(ValueError("No se genero el personal, NO se realizo la carga"))
    def op2(self):
        NuevoPersonal = self.ingresador()
        self.__manejador.agregarPersonal()
    def op3(self):
        try:
            indice = int(input("Ingrese posicion que desea ver\n"))
            self.__manejador.mostrarTipo(indice)
        except ValueError:
            print("El indice es erroneo")

    def op4(self):
        self.__manejador.ordenarPersonal()
        carrera = input("Ingrese carrera para emitir listado\n")
        self.__manejador.mostrarDICarrera(carrera)
    def op5(self):
        area = input("Ingrese area de investigacion que desea analizar\n")
        self.__manejador.contarAgentes(area)

    def op6(self):
        self.__manejador.recorrerMostrar()
    def op7(self):
        categ = input("Ingrese categoria  docente investigador que desea ver(I,II,III,IV,V)\n")
        os.system("cls")
        self.__manejador.montoDocentesI(categ)
    
    def op8(self):
        continuar = True
        while continuar:
            print("[1] Ingrese como administrador(Tesorero/Director)")
            print("[0] Para volver al menu principal")
            opcion = int(input("Ingrese opcion\n"))
            os.system("cls")
            if (opcion == 1):
                user = input("Ingrese usuario\n")
                password = input("Ingrese contraseña\n")
                if(user == "uTesoreso" and password == "ag@74ck"):
                    print("Datos correctos. Permisos de TESORERO activos")
                    continuar = self.tesorero(ITesorero(self.__manejador))
                elif(user == "uDirector" and password == "ufC77#!1"):
                    print("Datos correctos.Permiso de DIRECTOR activos")
                    continuar = self.director(IDirector(self.__manejador))
                else:
                    print("Datos incorrectos")
                    input("ENTER PARA CONTINUAR")
                    os.system("cls")
            elif(opcion == 0):
                continuar = not continuar

    def tesorero(self,manejador:ITesorero):
        input("ENTER PARA VER OPCIONES")
        continuar = True
        while continuar:
            os.system("cls")
            print("[1] Para ver gastos de empleado por CUIL")
            print("[0] Volver al menu principal")
            opcionT = int(input("Ingrese opcion deseada\n"))
            if(opcionT == 1):
                cuil = input("Ingrese cuil que desea ver\n")
                manejador.gastosSueldoPorEmpleado(cuil)
                input("ENTER PARA CONTINUAR")
            elif(opcionT == 0):
                continuar = not continuar
            else:
                print("Opcion inexistente, ingrese de nuevo")
                input("ENTER PARA CONTINUAR")
        return continuar
    
    def director(self,manejador:IDirector):
        input("ENTER PARA VER OPCIONES")
        continuar = True
        while continuar:
            os.system("cls")
            print("[1] Modificar sueldo basico")
            print("[2] Modificar cargo")
            print("[3] Modificar Categoria")
            print("[4] Modificar Importe extra de docente investigador")
            print("[0] Para volver al menu principal")
            op = int(input("Ingrese opcion deseada\n"))
            if( op == 1):
                cuil = input("Ingrese cuil que desea modificar\n")
                sueldo = int(input("Ingrese nuevo sueldo basico\n"))
                manejador.modificarBasico(cuil,sueldo)
            elif (op ==2):
                cuil = input("Ingrese cuil que desea modificar\n")
                cargo = input("Ingrese nuevo cargo(simple,semiexclusivo,exclusivo)\n")
                manejador.modificarPorcentajeporcargo(cuil,cargo)
            elif (op ==3):
                cuil = input("Ingrese cuil que desea buscar\n")
                tipoCategoria = self.categoriaDirec()
                manejador.modificarPorcentajeporcategoría(cuil,tipoCategoria)
            elif(op == 4):
                cuil = input("Ingrese cuil que desea buscar\n")
                importeNuevo = float(input("Ingrese nuevo importe extra\n"))
                manejador.modificarImporteExtra(cuil,importeNuevo)
            elif(op == 0):
                continuar = not continuar
            else:
                print("Opcion inexistente, ingrese de nuevo")
                input("ENTER PARA CONTINUAR")
        return continuar

                
    def categoriaDirec(self):
        continuar = True
        categ = None
        while continuar:
            print("[1] Categoria de Personal de apoyo")
            print("[2] Categoria de docente investigador")
            op = int(input("Ingrese opcion deseada\n"))
            os.system("cls")
            if(op == 1):
                try:
                    categ = int(input("Ingrese nueva categoria\n"))
                except ValueError:
                    print("No es un entero, ingrese nuevamente")
                else:
                    continuar = not continuar
            elif(op ==2):
                categ = input("Ingrese categoria de docente investigador(I,II,III,IV,V)\n")
                continuar = not continuar
            else:
                print("Opcion incorrecta")
        return categ
        
    def ingresador(self):
        personalNuevo = None
        try:
            nombre = input("Ingrese nombre del personal\n")
            os.system("cls")
            apellido = input("Ingrese apellido\n")
            os.system("cls")
            cuil = input("Ingrese CUIL\n")
            os.system("cls")
            sueldo = float(input("Ingrese sueldo basico\n"))
            os.system("cls")
            antiguedad = int(input("Cuantos años de antiguedad posee?\n"))

            self.opcionesPersonal()
            print("".center(20,"-"))
            tipo = int(input("Ingrese el tipo de personal que desea ingresar\n"))
            os.system("cls")
            
            if( tipo == 1):
                carrera = input("Carrera en la que dicta clases\n")
                os.system("cls")
                cargo = input("Ingrese cargo que posee\n")
                os.system("cls")
                catedra =input("Ingrese catedra\n")
                os.system("cls")
                personalNuevo = docente(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra)
            elif(tipo == 2):
                area = input("Ingrese area de investigacion\n")
                os.system("cls")
                tipo = input("Ingrese tipo de investigacion\n")
                os.system("cls")
                personalNuevo = investigador(cuil,apellido,nombre,sueldo,antiguedad,area,tipo)
            elif(tipo ==3):
                categoria = input("Ingrese categoria\n")
                os.system("cls")
                personalNuevo = personalApoyo(cuil,apellido,nombre,sueldo,antiguedad,categoria)
            elif(tipo == 4):
                carrera = input("Carrera en la que dicta clases\n")
                os.system("cls")
                cargo = input("Ingrese cargo que posee\n")
                os.system("cls")
                catedra =input("Ingrese catedra\n")
                os.system("cls")
                area = input("Ingrese area de investigacion\n")
                os.system("cls")
                tipo = input("Ingrese tipo de investigacion\n")
                os.system("cls")
                categoriaI = input("Ingrese categoria del investigador\n")
                os.system("cls")
                importeExtra = float(input("Ingrese importe extra\n"))
                os.system("cls")
                personalNuevo = docenteInvestigador(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,area,tipo,categoriaI,importeExtra) 
            else:
                print("Opcion Incorrecta")                   
        except ValueError:
            print("Los datos son erroneos")
        else:
            print("Personal instanciado con exito")
        return personalNuevo

    def opcionesPersonal(self):
        print("[1] Registrar Docente")
        print("[2] Registrar Investigador")
        print("[3] Registrar Personal de apoyo")
        print("[4] Registrar Docente Investigador")

    def opciones(self):
        continuar = True

        try:
            while continuar:
                self.muestraMenu()
                self.__op = int(input("Ingrese opcion deseada\n"))
                os.system("cls")

                if(self.__op == 0):
                    continuar = not continuar
                    self.guardarLista()
                    print("Muchas gracias")
                elif(self.__op == 1):
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
                    self.op7()
                elif(self.__op == 8):
                    self.op8()
                
                else:
                    print("Opcion inexistente")
        except ValueError:
            print("Algun dato ingresado es erroneo")        