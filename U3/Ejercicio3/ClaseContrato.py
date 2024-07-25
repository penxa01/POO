from datetime import date

class contrato:
    __FechaInicio = ""
    __FechaFin = ""
    __PagoMensual = 0
    __Jugador = None
    __equipo = None

    def __init__(self,fechai:date,fechaf:date,pago,jugador,equipo):
        self.__FechaInicio = fechai
        self.__FechaFin = fechaf
        self.__PagoMensual = pago
        self.__Jugador = jugador
        self.__equipo = equipo
    
    def getEquipo(self):
        return self.__equipo
    
    def getJugador(self):
        return self.__Jugador
    
    def getFechaFin(self):
        return self.__FechaFin
    
    def getFechaInicio(self):
        return self.__FechaInicio
    
    def getPago(self):
        return self.__PagoMensual
    
    def getImporte(self):
        return (self.__PagoMensual*((self.__FechaFin-self.__FechaInicio).days//30))