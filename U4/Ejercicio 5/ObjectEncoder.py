import json
from pathlib import Path
from ManejadorPacientes import ManejadorPacientes
from ClasePaciente import Paciente
import os

class ObjectEncoder(object):
    __pathArchivo=None
    def __init__(self, pathArchivo):
        #PathArchivo == nombre del archivo
        self.__pathArchivo=pathArchivo
    #Decodifica,lee y graba informacion de/hacia Json
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='ManejadorPacientes':
                pacientes=d['pacientes']
                manejador=class_()
                for i in range(len(pacientes)):
                    dpaciente=pacientes[i]
                    class_name=dpaciente.pop('__class__')
                    class_=eval(class_name)
                    atributos=dpaciente['__atributos__']
                    unPaciente=class_(**atributos)
                    manejador.agregarPaciente(unPaciente)
            return manejador
    def guardarJSONArchivo(self, diccionario):
        archivo = open(Path(self.__pathArchivo), "w", encoding="UTF-8")
        json.dump(diccionario, archivo, indent=4)
        archivo.close()

    def leerJSONArchivo(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta,self.__pathArchivo)
        archivo =open(Archivo)
        diccionario = json.load(archivo)
        archivo.close()
        return diccionario