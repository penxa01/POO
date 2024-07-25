from ClaseNodo import nodo
from ClaseAparatos import aparato
from zope.interface import Interface
from zope.interface import implementer
from ClaseLavaropa import Lavarropa
from ClaseTelevisor import Televisor
from ClaseHeladera import Heladera
from InterfazLista import ILista
from typing import List

@implementer(ILista)
class Lista:
    __comienzo = None

    def __init__(self):
        self.__comienzo = None
        self.__actual =  None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            self.__indice+=1
            return dato

    
    def agregarAparato(self,aparato):
        NuevoNodo = nodo(aparato)
        NuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo = NuevoNodo
        self.__actual = self.__comienzo
        self.__tope += 1
    
    def getLongitud(self):
        return self.__tope
    
    def insertarAparato(self,aparato,indice):
        
        NodoAInsertar = nodo(aparato)
        i = 0
       
        if(indice == 1):
            self.agregarAparato(NodoAInsertar)
        
        while((i < indice-1) and (self.__actual.getSiguiente() is not None)):
            self.__actual = self.__actual.getSiguiente()
            i+=1
        if self.__actual.getSiguiente() == None:
            print("Se inserta el aparato al final de la lista")
            NodoAInsertar.setSiguiente(self.__actual.getSiguiente())
            self.__actual.setSiguiente(NodoAInsertar)
        else:
            NodoAInsertar.setSiguiente(self.__actual.getSiguiente())
            self.__actual.setSiguiente(NodoAInsertar)
        self.__actual = self.__comienzo
        
    def mostrarAparato(self,posicionBuscada):
        i = 0
        self.__actual = self.__comienzo
        if (posicionBuscada == 1):
            aparatoBuscado = self.__actual.getDato()
        
        while i < posicionBuscada-1 and self.__actual.getSiguiente() != None:
            i += 1
            self.__actual =self.__actual.getSiguiente()
        
        if i< posicionBuscada-1 or i > posicionBuscada-1:
            raise(IndexError("Fuera de indice"))
        
        aparatoBuscado = self.__actual.getDato()
        return aparatoBuscado


    def aJson(self):
        diccionarioLista = dict(
            __class__ = self.__class__.__name__,
            aparatos =[nuevoAparato.toJson() for nuevoAparato in self]
        )
        return diccionarioLista
    
    def aparatosPhillips(self):
        i = self.__tope
        contador = 0
        self.__actual = self.__comienzo
        while (i !=0) and self.__actual.getSiguiente() != None:
            if(self.__actual.getDato().getMarca() == "Philips"):
                contador +=1
            self.__actual = self.__actual.getSiguiente()
            i -=1
        print("Hay {} aparatos de marca Phillips".format(contador))
    
    def mostrarLavarropas(self):
        marcas:List[str] = []

        for dato in self:
            if isinstance(dato,Lavarropa) and (dato.getTipoCarga() == "Superior") and (dato.getMarca() not in [marca for marca in marcas]):
                print("".center(20,"-"))
                print(dato)

    def mostrarTodosAparatos(self):
        for dato in self:
            print("".center(20,"-"))
            print(dato.getMarca())
            print(dato.getPais())
            print("Importe:${}".format(dato.getImporte()))

           
        
        


