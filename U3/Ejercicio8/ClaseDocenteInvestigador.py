from ClaseDocente import docente
from ClaseInvestigador import investigador

class docenteInvestigador(docente,investigador):
    categoria = None
    importeExtra = None

    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra,area,tipo,categoria,importe):
        super().__init__(cuil=cuil, apellido=apellido, nombre=nombre, sueldo=sueldo, antiguedad=antiguedad, carrera=carrera, cargo=cargo, catedra=catedra,area=area,tipo=tipo)
        self.__categoria = categoria
        self.__importeExtra = importe
    
    def __str__(self):
        return super().__str__() + ("Categoria en el programa de incentivos: {}\nImporte extra por docencia e investigacion: {}".format(self.__categoria,self.__importeExtra))
    
    def getCategoria(self):
        return self.__categoria
    
    def setCategoria(self,newCategoria):
        self.__categoria  = newCategoria    
    
    def getimporteExtra(self):
        return self.__importeExtra
    
    def setImporteExtra(self,nuevoImporteExtra):
        self.__importeExtra = nuevoImporteExtra
    
    def getSueldo(self):
        return self.getSueldoDocente() + self.getimporteExtra()
    
    def toJson(self):
        diccionario = super().toJson()
        diccionario["__atributos__"]["categoria"] = self.getCategoria()
        diccionario["__atributos__"]["importeExtra"] = self.getimporteExtra()