import json
from ClaseListaEnlazada import Lista
from ClaseAparatos import aparato
from ClaseTelevisor import Televisor
from ClaseHeladera import Heladera
from ClaseLavaropa import Lavarropa

class ObjetcEncoder:

    def decodificarDiccionario(self,diccionario):
        Manejador = None
        if "__class__" not in diccionario:
            Manejador = diccionario
        else:
            nombreClase =diccionario ["__class__"]
            clase = eval(nombreClase)

            if nombreClase == "Lista":
                aparatos = diccionario["aparatos"]
                ListaAparatos = clase()
                for i in range(len(aparatos)):
                    dictAparato = aparatos[i]
                    nombreClass = dictAparato.pop("__class__")
                    tipoClase = eval(nombreClass)
                    atributosObj = dictAparato["__atributos__"]
                    NuevoAparato = tipoClase(**atributosObj)
                    ListaAparatos.agregarAparato(NuevoAparato)
            Manejador = ListaAparatos
        return Manejador

    def guardarJSONArchivo(self, diccionario, nombreArchivo):
        archivo = open(nombreArchivo, "w", encoding="UTF-8")
        json.dump(diccionario, archivo, indent=4)
        archivo.close()
    

    def leerJSONArchivo(self, nombreArchivo):
        archivo = open(nombreArchivo)
        diccionario = json.load(archivo)
        archivo.close()
        return diccionario
        