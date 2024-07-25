from ClaseAparatos import aparato
import json

class Televisor(aparato):
    __tipoPantalla = None
    __pulgadas = None
    __definicion = None
    __conexion = None

    def __init__(self,marca,modelo,color,pais,precio:float,tipoPantalla:str,pulgadas:int,tipoDefinicion:str,conexionInternet:bool):
        super().__init__(marca,modelo,color,pais,precio)
        self.__tipoPantalla = tipoPantalla
        self.__pulgadas = pulgadas
        self.__definicion = tipoDefinicion
        self.__conexion = conexionInternet
    
    def __str__(self)->str:
        cadena = ""
        cadena += super().__str__() + ("Tipo de pantalla:{}\nPulgadas:{}     Definicion:{}\nConexion:{}".format(self.__tipoPantalla,self.__pulgadas,self.__definicion,self.__conexion))
        return cadena
    
    def getCapacidad(self):
        pass

    def getTipoPantalla(self)->str:
        return self.__tipoPantalla
    
    def getPulgadas(self)->int:
        return self.__pulgadas
    
    def getDefinicion(self) -> str:
        return self.__definicion
    
    def getConexion(self) -> bool:
        return self.__conexion
    
    def getImporte(self)->float:
        importe = self.getPrecio()
        if(self.__definicion.upper() == "SD"):
            importe += importe* 0.01
        elif(self.__definicion.upper() == "HD"):
            importe += importe* 0.02
        elif(self.__definicion.upper() == "FULL HD"):
            importe += importe* 0.03
        
        if self.__conexion:
            importe += self.getPrecio() *0.1
        
        return importe
    
    def toJson(self):
        diccionarioTV = dict(__class__ = self.__class__.__name__, 
        __atributos__ = dict(
            marca = self.getMarca(),
            modelo = self.getModelo(),
            color = self.getColor(),
            pais = self.getPais(),
            precio = self.getPais(),
            tipoPantalla = self.__tipoPantalla,
            pulgadas = self.__pulgadas,
            definicion = self.__definicion,
            conexion = self.__conexion)
        )
        return diccionarioTV



