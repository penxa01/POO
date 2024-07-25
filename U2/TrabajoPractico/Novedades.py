class novedades:
    __legajo = None
    __importe = None
    __concepto = None
    __codigo = None

    def __init__(self,datos):
        self.__legajo = int(datos[0])
        self.__importe = float(datos[1])
        self.__concepto = datos[2]
        self.__codigo = datos[3]

    def getLegajo(self):
        return self.__legajo

    def getImporte(self):
        return self.__importe
    
    def getConcepto(self):
        return self.__concepto

    def getCodigo(self):
        return self.__codigo
