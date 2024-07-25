from ClasePersonal import personal

class personalApoyo(personal):
    __categoria = None

    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,categoria):
        super().__init__(cuil,apellido,nombre,sueldo,antiguedad)
        self.__categoria = categoria
    
    def __str__(self):
        cadena = ""
        cadena += super().__str__() + ("Categoria:{}".format(self.__categoria))
    
    def getCategoria(self):
        return self.__categoria
    
    def getImporteCategoria(self):
        monto = None

        if ((1<=self.getCategoria())and (self.getCategoria()<=10)):
            monto = self.getSueldoBasico() * 0.10
        elif((11<=self.getCategoria())and (self.getCategoria()<=20)):
            monto = self.getSueldoBasico() * 0.20
        elif((21<=self.getCategoria())and (self.getCategoria()<=22)):
            monto = self.getSueldoBasico() * 0.30
        return monto
            
    def toJson(self):
        diccionario = super().toJson()
        diccionario["__atributos__"]["categoria"] = self.getCategoria()
        return diccionario

    def getSueldo(self):
        return self.getSueldoBasico() + self.getImporteCategoria()