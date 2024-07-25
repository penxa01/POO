from ClaseNodo import nodo
from zope.interface import Interface
from zope.interface import implementer
from ClasePersonal import personal
from ClaseDocenteInvestigador import docenteInvestigador
from ClaseInvestigador import investigador
from NuevasInterfaces import IDirector
from InterfazLista import ILista
from NuevasInterfaces import ITesorero 
from ClasePersonalApoyo import personalApoyo

@implementer(IDirector)
@implementer(ILista)
@implementer(ITesorero)

class ListaEnlazada:
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
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
        
    def agregarPersonal(self,personal):
        NuevoNodo = nodo(personal)
        NuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo = NuevoNodo
        self.__actual = self.__comienzo
        self.__tope += 1

    def getLongitud(self):
        return self.__tope
    
    def insertarPersonal(self,personal,indice):
        
        NodoAInsertar = nodo(personal)
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
            self.__tope += 1
        else:
            NodoAInsertar.setSiguiente(self.__actual.getSiguiente())
            self.__actual.setSiguiente(NodoAInsertar)
            self.__tope += 1
        self.__actual = self.__comienzo
        
    def mostrarPersonal(self,posicionBuscada):
        i = 0
        self.__actual = self.__comienzo
        if (posicionBuscada == 1):
            personalBuscado = self.__actual.getDato()
        
        while i < posicionBuscada-1 and self.__actual.getSiguiente() != None:
            i += 1
            self.__actual =self.__actual.getSiguiente()
        
        if i< posicionBuscada-1 or i > posicionBuscada-1:
            raise(IndexError("Fuera de indice"))
        
        personalBuscado = self.__actual.getDato()
        return personalBuscado
    
    def toJson(self):
        diccionarioLista = dict(
            __class__ = self.__class__.__name__,
            personalss =[nuevoPersonal.toJson() for nuevoPersonal in self]
        )
        return diccionarioLista
    
    def ordenarPersonal(self):
        
        if self.__comienzo != None:
            
            k = None
            cota = None
            
            while k != self.__comienzo:
                
                k = self.__comienzo
                self.__actual = self.__comienzo
                while self.__actual.getSiguiente() != cota:
                    

                    if self.__actual.getSiguiente().getDato() < self.__actual.getDato():
                        
                        unaPersona = self.__actual.getDato()
                        self.__actual.setPersona(self.__actual.getSiguiente().getDato())
                        self.__actual.getSiguiente().setPersona(unaPersona)
                        k = self.__actual
                    
                    self.__actual = self.__actual.getSiguiente()
                

                cota = k.getSiguiente()
    
    def mostrarTipo(self,indice):
        self.__actual = self.__comienzo
        i =indice
        while i-1 != 0 and self.__actual.getSiguiente is not None:
            self.__actual = self.__actual.getSiguiente()
            i-= 1
        print("En la posicion {} hay un {} ".format(indice,self.__actual.getDato().__class__.__name__))

    def mostrarDICarrera(self,carrera:str):
        print("Listado de docentes investigadores en la carrera de {}".format(carrera.upper()))
        i = self.__tope
        unNodo = self.__comienzo
        while i != 0:
            if isinstance(unNodo.getDato(),docenteInvestigador):
                if(unNodo.getDato().getCarrera().lower() == carrera.lower()):
                    print("".center(20,"-"))
                    print(unNodo.getDato())
            unNodo = unNodo.getSiguiente()

            i -= 1
        
    def contarAgentes(self,area):

        i = self.__tope
        contDI = 0
        contI = 0

        self.__actual = self.__comienzo

        while i !=0:
            if isinstance(self.__actual.getDato(),docenteInvestigador):
                if (self.__actual.getDato().getArea().lower() == area.lower()):
                    contDI += 1
            elif isinstance(self.__actual.getDato(),investigador):
                if (self.__actual.getDato().getArea().lower() == area.lower()):
                    contI += 1
            self.__actual = self.__actual.getSiguiente()
            i -=1
        print("En el area de investigacion de {} hay {} docentes investigadores y {} investigadores".format(area.capitalize(),contDI,contI))

    def recorrerMostrar(self):
        # Recorrer la colección y generar un listado que muestre nombre y apellido,
        #tipo de Agente y sueldo de todos los agentes, ordenado por Nombre.
        i = self.__tope
        self.__actual = self.__comienzo
        print("Datos Agentes".center(20,"-"))
        while i !=0:
            print("".center(20,"-"))
            print("Nombre y Apellido: {}".format(self.__actual.getDato().getNombreCompleto()))
            print("Tipo de agente: {}".format(self.__actual.getDato().__class__.__name__))
            print("Sueldo: ${}".format(self.__actual.getDato().getSueldo()))
            self.__actual = self.__actual.getSiguiente()
            i -= 1
    
    def montoDocentesI(self,categoria):
        i = self.__tope
        montoSolicitar= 0
        self.__actual = self.__comienzo
        print("Docentes investigadores de categoria {}".format(categoria.upper()))
        while i !=0:
            if isinstance(self.__actual.getDato(),docenteInvestigador):
                if(self.__actual.getDato().getCategoria().upper() == categoria.upper()):
                    print("".center(20,"-"))
                    print("Nombre y apellido: {}".format(self.__actual.getDato().getNombreCompleto()))
                    print("Importe extra por docencia: ${}".format(self.__actual.getDato().getimporteExtra()))
                    montoSolicitar += self.__actual.getDato().getimporteExtra()
            self.__actual = self.__actual.getSiguiente()
            i -= 1
        print("Monto total a solicitar al ministerio: ${}".format(montoSolicitar))

    def gastosSueldoPorEmpleado(self,cuil):
        i = self.__tope
        bandera =True
        self.__actual = self.__comienzo

        while i!= 0 and bandera:
            if(self.__actual.getDato().getCuil().lower() == cuil.lower()):
                bandera = False
                print("El agente de cuil {} genera un gasto de ${}".format(cuil,self.__actual.getDato().getSueldo()))
            self.__actual = self.__actual.getSiguiente()
            i -=1
        if bandera:
            print("El cuil ingresado no existe")

    def modificarBasico(self,cuil,nuevoBasico):
        i = self.__tope
        bandera = True
        self.__actual = self.__comienzo
        
        while i!= 0 and bandera:
            if(self.__actual.getDato().getCuil().lower() == cuil.lower()):
                bandera = False
                self.__actual.getDato().setSueldoBasico(nuevoBasico)
            self.__actual = self.__actual.getSiguiente()
            i -=1
        if bandera:
            print("El cuil ingresado no existe")   
    
    def modificarPorcentajeporcargo(self,cuil,nuevoPorcentaje):
        i = self.__tope
        bandera = True
        self.__actual = self.__comienzo
        
        while i!= 0 and bandera:
            if(self.__actual.getDato().getCuil().lower() == cuil.lower()):
                bandera = False
                self.__actual.getDato().setCargo(nuevoPorcentaje)
            self.__actual = self.__actual.getSiguiente()
            i -=1
        if bandera:
            print("El cuil ingresado no existe") 

    def modificarPorcentajeporcategoría(self,cuil,nuevoPorcentaje):
        i = self.__tope
        bandera = True
        self.__actual = self.__comienzo
        
        while i!= 0 and bandera:
            if(self.__actual.getDato().getCuil().lower() == cuil.lower()) and (isinstance(self.__actual.getDato(),docenteInvestigador) or (isinstance(self.__actual.getDato(),personalApoyo))):
                bandera = False
                self.__actual.getDato().setCategoria(nuevoPorcentaje)
            self.__actual = self.__actual.getSiguiente()
            i -=1
        if bandera:
            print("El cuil ingresado no existe")

    def modificarImporteExtra(self,cuil,nuevoImporteExtra):
        i = self.__tope
        bandera = True
        self.__actual = self.__comienzo
        
        while i!= 0 and bandera:
            if(self.__actual.getDato().getCuil().lower() == cuil.lower()):
                bandera = False
                self.__actual.getDato().setImporteExtra(nuevoImporteExtra)
            self.__actual = self.__actual.getSiguiente()
            i -=1
        if bandera:
            print("El cuil ingresado no existe")