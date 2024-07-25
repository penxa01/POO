from Novedades import novedades
import os
import csv

class manejadorNovedades:
    __Novedades = []

    def __init__(self):
        self.__Novedades = []

    def CargarNovedades(self,personal):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "novedades.csv")
        archivo = open(Archivo)

        reader = csv.reader(archivo,delimiter = ";")
        cabeza = True

        for comp in reader:
            if cabeza:
                cabeza = not cabeza
            else:
                busqueda = personal.buscarPersonal(int(comp[0]))
                if(busqueda == -1):
                    print("El legajo {} es inexistente, no se añadira a la lista de novedades".format(comp[0]))
                else:
                    print("El legajo {} se añadira a la lista de novedades".format(comp[0]))
                    NuevaNovedad = novedades(comp)
                    self.__Novedades.append(NuevaNovedad)

        print("Novedades cargadas con exito")
        archivo.close()
    
    def getLista(self):
        return self.__Novedades
    
    def mostrarNovedades(self,legajo,sueldobasico):
        sueldoNeto= sueldobasico
        print("Codigo       Concepto                   Importe")
        for novedad in self.__Novedades:
            if(novedad.getLegajo() == legajo):
                if(novedad.getCodigo() =="A"):
                    sueldoNeto += novedad.getImporte()
                elif(novedad.getCodigo() == "D"):
                    sueldoNeto -=novedad.getImporte()    
                print("{:^5}       {:^12}      ${:^8}".format(novedad.getCodigo(),novedad.getConcepto(),novedad.getImporte()))
        print("Total a cobrar: ${}".format(sueldoNeto))
                
        