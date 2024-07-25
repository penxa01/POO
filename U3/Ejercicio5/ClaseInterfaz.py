from zope.interface import Interface
from zope.interface import implementer

class Iinterfaz(Interface):

    def insertarElemento(elemento,posicion):
        pass
    
    def agregarElemento(elemento):
        pass

    def mostrarElemento(posicion):
        pass
    