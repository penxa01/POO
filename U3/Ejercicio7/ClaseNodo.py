from ClasePersonal import personal as tipoObjeto

class nodo:
    __dato = None
    __siguiente = None

    def __init__(self,NuevoDato:tipoObjeto):
        self.__dato = NuevoDato
        self.__siguiente = None
    
    def setSiguiente(self,NuevoNodo):
        self.__siguiente = NuevoNodo
    
    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__dato
    
    def setPersona(self,dato):
        self.__dato = dato
