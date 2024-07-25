from ClaseFlor import flor

class ramo:
    __tamaño = None
    __Flores= None

    def __init__(self,tamaño = ""):
        self.__tamaño = tamaño
        self.__Flores = []
    
    def agregarFlor(self,Nuevaflor):
        if isinstance(Nuevaflor, flor):
            self.__Flores.append(Nuevaflor)
            print("{} agregada al ramo".format(Nuevaflor.getNombre()))
        else:
            print("{} no es una flor".format(Nuevaflor))

    def getTamaño(self):
        return self.__tamaño
    
    def getLista(self):
        return self.__Flores
    
    def mostrar(self):
        print("Tamaño:{}".format(self.__tamaño.capitalize()))
        for flor in self.__Flores:
            print("".center(20,"-"))
            print(flor)

