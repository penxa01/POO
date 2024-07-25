from ClaseContrato import contrato
from datetime import date

class equipo:
    __Nombre = None
    __Ciudad = None
    __Contratos = None
    #Variables de clase
    __CantidadContratos = 0

    def __init__(self,name = "",city = ""):
        self.__Nombre = name
        self.__Ciudad = city
        self.__Contratos = []
    
    def getNombre(self):
        return self.__Nombre
    
    @classmethod
    def getCantidadContratos(cls):
        cls.__CantidadContratos += 1
        return cls.__CantidadContratos
    
    def generarContrato(self,contratoNuevo):
        print("Contrato nro:{}\n".format(self.getCantidadContratos()))
        self.__Contratos.append(contratoNuevo)
    
    def __str__(self):
        return ("Nombre:{} \nCiudad:{}".format(self.__Nombre,self.__Ciudad))
    
    def getContratos(self):
        return self.__Contratos
    
    def getNombre(self):
        return self.__Nombre
    
    def contratosVencimiento(self):
        print("Jugadores que vencen contrato en 6 meses")
        for contrato in self.__Contratos:
            if (((contrato.getFechaFin() - date.today()).days // 30 ) == 6):
                print("".center(20,"-"))
                print("{}".format(contrato.getJugador()))
            
    def getImporteTotal(self):
        importe = 0
        for contrato in self.__Contratos:
            importe += contrato.getImporte()
        
        print("El importe total en jugadores es de: ${}".format(importe))



        