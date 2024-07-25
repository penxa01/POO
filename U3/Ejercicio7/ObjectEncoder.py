import json
from ClasePersonal import personal
from ClaseDocente import docente
from ClaseInvestigador import investigador
from ClasePersonalApoyo import personalApoyo
from ClaseDocenteInvestigador import docenteInvestigador
from ClaseLista import ListaEnlazada
from pathlib import Path

class ObjectEncoder:

    def decodificarDiccionario(self,diccionario):
        Manejador = None
        if "__class__" not in diccionario:
            Manejador = diccionario
        else:
            nombreClase =diccionario ["__class__"]
            clase = eval(nombreClase)

            if nombreClase == "ListaEnlazada":
                Personals = diccionario["personal"]
                ListaPersonal = clase()
                for i in range(len(Personals)):
                    dictPersonal = Personals[i]
                    nombreClass = dictPersonal.pop("__class__")
                    tipoClase = eval(nombreClass)
                    atributosObj = dictPersonal["__atributos__"]
                    NuevaPersona = tipoClase(**atributosObj)
                    ListaPersonal.agregarPersonal(NuevaPersona)
            Manejador = ListaPersonal
        return Manejador

    def guardarJSONArchivo(self, diccionario:dict, nombreArchivo:str):
        archivo = open(Path(nombreArchivo), "w", encoding="UTF-8")
        json.dump(diccionario, archivo, indent=4)
        archivo.close()


    def leerJSONArchivo(self, nombreArchivo):
        archivo = open(nombreArchivo)
        diccionario = json.load(archivo)
        archivo.close()
        return diccionario
        
