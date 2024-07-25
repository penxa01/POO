from ClasePersonal import personal

class docente(personal):
    __carrera = None
    __cargo = None
    __catedra = None

    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,**kwargs):
        super().__init__(cuil,apellido,nombre,sueldo,antiguedad,**kwargs)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    
    def __str__(self):
        cadena = ""
        cadena += super().__str__() + ("Carrera donde dicta clases:{}\nCargo:{}\nCatedra:{}\n".format(self.__carrera,self.__cargo,self.__catedra))
        return cadena
    
    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo
    
    def getCatedra(self):
        return self.__catedra
    
    def getImporteCargo(self):
        monto = 0
        if (self.__cargo.lower() == "simple"):
            monto =self.getSueldoBasico() * 0.1
        elif(self.__cargo.lower() == "semiexclusivo"):
            monto = self.getSueldoBasico() * 0.2
        elif(self.__cargo.lower() == "exclusivo"):
            monto = self.getSueldoBasico() *0.5
        return monto

    def getImporteAntiguedad(self):
        return self.getSueldoBasico()*(self.getAntiguedad()/100)


    def toJson(self):
        diccionario = super().toJson()
        diccionario["__atributos__"]["carrera"] = self.getCarrera()
        diccionario["__atributos__"]["cargo"] = self.getCargo()
        diccionario["__atributos__"]["catedra"] = self.getCatedra()
        return diccionario
    
    def getSueldo(self):
        return self.getSueldoBasico() + self.getImporteCargo() + self.getImporteAntiguedad()
    
    def getSueldoDocente(self):
        return self.getSueldoBasico() + self.getImporteCargo() + self.getImporteAntiguedad()


