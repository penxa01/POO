from ClasePersonal import personal

class investigador(personal):
    __area = None
    __tipo = None

    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,area,tipo,**kwargs):
        super().__init__(cuil,apellido,nombre,sueldo,antiguedad,**kwargs)
        self.__area = area
        self.__tipo = tipo
    
    def __str__(self):
        cadena =""
        cadena += super().__str__() + ("Area de investigacion: {}\nTipo de investigacion: {}".format(self.__area,self.__tipo))
        return cadena

    def getArea(self):
        return self.__area 
    
    def getTipo(self):
        return self.__tipo
    
    def getImporteAntiguedad(self):
        return self.getSueldoBasico()*(self.getAntiguedad()/100)
    
    def getSueldo(self):
        return self.getSueldoBasico() + self.getImporteAntiguedad()
    
    def toJson(self):
        diccionario = super().toJson()
        diccionario["__atributos__"]["area"] = self.getArea()
        diccionario["__atributos__"]["tipo"] = self.getTipo()  
        return diccionario