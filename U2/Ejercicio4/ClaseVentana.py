
class Ventana:
    __titulo = " "
    __xVertiSup = 0
    __yVertiSup = 0
    __xVertiInf = 0
    __yVertiInf = 0

    def __init__(self,tit,XVS = 0,YVS = 0,XVI = 500,YVI = 500):
        self.__titulo = tit
        self.__xVertiSup = XVS
        self.__yVertiSup = YVS
        self.__xVertiInf = XVI
        self.__yVertiInf = YVI
    
    def mostrar(self):
        return print(" {} \n Coordenadas vertice superior:({},{}) \n Coordenadas vertice inferior({},{})".format(self.__titulo,self.__xVertiSup,self.__yVertiSup,self.__xVertiInf,self.__yVertiInf))
    
    def getTitulo(self):
        return self.__titulo

    def ancho(self):
        return (self.__xVertiInf - self.__xVertiSup)

    def alto(self):
        return (self.__yVertiInf - self.__yVertiSup)
    
    def moverDerecha(self,X = 10):
        if (self.__xVertiInf <500) and (self.__xVertiSup > 0):
            self.__xVertiSup += X
            self.__xVertiInf += X
        
    def moverIzquierda(self,X = 10):
        if (self.__xVertiInf <500) and (self.__xVertiSup > 0):
            self.__xVertiSup -= X
            self.__xVertiInf -= X
        
    def bajar(self,Y = 10):
        if (self.__yVertiInf <500) and (self.__yVertiSup > 0):
            self.__yVertiSup += Y
            self.__yVertiInf += Y
    
    def subir (self,Y= 10):
        if (self.__yVertiInf <500) and (self.__yVertiSup > 0):
            self.__yVertiSup -= Y
            self.__yVertiInf -= Y

    



    