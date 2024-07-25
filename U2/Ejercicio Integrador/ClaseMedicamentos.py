
class medicamento():
    __idCama = 0
    __idMedicamento = 0
    __nameComercial = " "
    __monodroga = " "
    __presentacion = " "
    __cantidadAplicada = 00
    __precioTotal = 0.0

    def __init__(self,idCama,idMed,nameC,monod,pres,cantApli,precio):
        self.__idCama = idCama
        self.__idMedicamento = idMed
        self.__nameComercial = nameC
        self.__monodroga = monod
        self.__presentacion = pres
        self.__cantidadAplicada = cantApli
        self.__precioTotal = precio

    def getIdCama(self):
        return self.__idCama
    
    
    def getMonodroga(self):
        return self.__monodroga

    def getPresentacion(self):
        return self.__presentacion
    
    def getCantidadAplicada(self):
        return self.__cantidadAplicada

    def getPrecio(self):
        return self.__precioTotal

