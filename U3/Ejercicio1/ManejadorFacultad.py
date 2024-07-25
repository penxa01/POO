from ClaseFacultad import Facultad
import os
import csv
from ClaseCarrera import Carrera



class Manejador:
    __Facultades = []

    def __init__(self,facu = []):
        self.__Facultades = facu

    def cargar(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "info.csv")
        archivo =open(Archivo)
        reader = csv.reader(archivo,delimiter=",")

        puntero = next(reader)
        
        bandera = True
        while bandera:
            filaCarrera = next(reader)
            Facu = Facultad(int(puntero[0]),puntero[1],puntero[2],puntero[3],puntero[4])
            while bandera and (int(puntero[0]) == int(filaCarrera[0])):
                Facu.agregarCarrera(filaCarrera)
                try:
                    filaCarrera = next(reader)
                except StopIteration:
                    bandera = False
            self.__Facultades.append(Facu)
            puntero = filaCarrera
        archivo.close()


    def carga2(self):

        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "info.csv")
        archivo =open(Archivo)
        reader = csv.reader(archivo,delimiter=",")

        anterior =-1
        aux = 0
        for fila in reader:
            print(fila)
            
            aux = int(fila[0])

            if aux != anterior:
                self.__Facultades.append(Facultad(int(fila[0]),fila[1],fila[2],fila[3],fila[4]))
                anterior = aux
            else:
                if anterior == aux:
                    self.__Facultades[aux-1].agregarCarrera(fila)
                    anterior = aux
        
        archivo.close()

    def buscar(self,codigo):
        
        i = 0
        bandera = False
        while (i < len(self.__Facultades)) and (bandera == False):
            if self.__Facultades[i].getCodigo() == codigo:
                bandera = True
            else:
                i+=1
        if bandera:
            print("FACULTAD ENCONTRADA")
        else:
            print("Facultad no encontrada")
            i = -1
        return i

    def InfoCarrera(self,carreraIngresada):
        i = 0
        banderaFacu = False
        while(i <len(self.__Facultades) and (banderaFacu == False)):
            busqueda = self.__Facultades[i].buscarCarrera(carreraIngresada)
            if(isinstance(busqueda,Carrera)):
                banderaFacu = True
                print(busqueda)
            elif( busqueda == -1):
                print("Carrera inexistente en {}".format(self.__Facultades[i].getNombre()))
                print("".center(20,"-"))
                i +=1
            


    def listar(self,codigo):
        indice = self.buscar(codigo)
        if(indice == -1):
            print("Facultad no encontrada")
        else:
            print(self.__Facultades[indice])
            print("CARRERAS".center(20,"-"))
            self.__Facultades[indice].mostrarInfoCarreras()
        
        
            
