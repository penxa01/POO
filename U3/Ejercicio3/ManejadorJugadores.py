from ClaseJugador import jugador

class manejadorJugadores:
    __ListaJugadores = None

    def __init__(self):
        self.__ListaJugadores = []
    
    def agregarJugador(self,NuevoJugador):
        self.__ListaJugadores.append(NuevoJugador)
    
    def buscarJugador(self,dni):
        i = 0
        bandera = False

        while i < len(self.__ListaJugadores) and  not bandera:
            if(dni == self.__ListaJugadores[i].getDNI()):
                bandera = True
            else:
                i += 1 
        if(bandera == False):
           i =-1

        return i
    
    def getEquipo(self,i):
        return self.__ListaJugadores[i].getContrato().getEquipo()
    
    def getFechaFin(self,i):
        return self.__ListaJugadores[i].getContrato().getFechaFin()