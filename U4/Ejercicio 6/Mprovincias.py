from Provincia import Provincia
#Manejador de provincias, permite manejar una coleccion de provincias
class ManejaProvincia(object):
    __Provincias=list
    def __init__(self):
        self.__Provincias=[]
    def agregar(self, provincia):
        if isinstance(provincia, Provincia):
            self.__Provincias.append(provincia)
    def getprovincias(self):
        return self.__Provincias
    def obtenerprovincia(self, provincia):
        i=0
        while i < len(self.__Provincias) and provincia != self.__Provincias[i]:
            i+=1
        if i<len(self.__Provincias):
            return i
#Permite decodificar un archivo JSON que posea un manejador de provincias
    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__,
            Elementos = [elemento.toJSON() for elemento in self.__Provincias]
        )
