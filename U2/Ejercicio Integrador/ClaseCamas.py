
class Cama():
    __IDcama = 0
    __NroHabitacion = 0
    __Estado = False
    __NyA = None
    __Diagnostico = " "
    __FechaInternacion = " "
    __FechaAlta = " "

    def __init__(self,id= 00,nroH = 0,estado = False,NyA = None,Diagnostico = " ",FechaI = " ",FechaA= None):
        self.__IDcama = id
        self.__NroHabitacion = nroH
        self.__Estado = estado
        self.__NyA = NyA
        self.__Diagnostico = Diagnostico
        self.__FechaInternacion = FechaI
        self.__FechaAlta = FechaA

    def __str__(self):
        return ("Cama:{}  Nro de Habitacion:{}    Estado:{} \nNombre y Apellido:{}    Fecha de internacion:{}\nDiagnostico:{}".format(self.__IDcama,self.__NroHabitacion,self.__Estado,self.__NyA,self.__FechaInternacion,self.__Diagnostico))

    def getEstado(self):
        return self.__Estado
    
    def getDiagnostico(self):
        return self.__Diagnostico
    
    def getNyA(self):
        return self.__NyA
    
    def getID(self):
        return self.__IDcama
    
    def getNroH(self):
        return self.__NroHabitacion
    
    def getInternacion(self):
        return self.__FechaInternacion
    
    def getAlta(self):
        return self.__FechaAlta
    
    def regAlta(self,fecha):
        self.__FechaAlta = fecha
    
        