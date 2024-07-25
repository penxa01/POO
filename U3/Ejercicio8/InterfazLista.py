from zope.interface import Interface
from zope.interface import implementer

class ILista(Interface):

    def insertarAparato(elemento,posicion):
        pass
    
    def agregarAparato(elemento):
        pass

    def mostrarAparato(posicion):
        pass
    