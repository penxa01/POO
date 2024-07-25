
class flor:
    __nroFlor = None
    __nombre = None
    __color = None
    __descripcion = None
    __CantidadPedida = 0

    def __init__(self,numero = 0,name = "",color = "", descripcion = "",cantPedida = 0):
        self.__nroFlor = numero
        self.__nombre = name
        self.__color = color
        self.__descripcion = descripcion
        self.__CantidadPedida = cantPedida
    
    def __str__(self):
        return ("Flor nro {}:\nNombre:{}\nColor:{}\nDescripcion:{}".format(self.__nroFlor,self.__nombre,self.__color,self.__descripcion))

    def getNroFlor(self):
        return self.__nroFlor
    
    def getNombre(self):
        return self.__nombre
    
    def getColor(self):
        return self.__color
    
    def getDescripcion(self):
        return self.__descripcion
    
    def contarFlorPedida(self):
        self.__CantidadPedida += 1
    
    def getCantidadPedida(self):
        return self.__CantidadPedida
    
    def __gt__(self,otro):
        return self.__CantidadPedida< otro.getCantidadPedida()
    