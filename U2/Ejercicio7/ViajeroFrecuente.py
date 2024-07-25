

class ViajeroFrecuente:
    __num_viajero = 0
    __dni = " "
    __Nombre =  " "
    __Apellido = " "
    __millas_acum = 0

    def __init__(self,num_viajero,dni,nombre,apellido,millas_acum):
        self.__num_viajero= num_viajero
        self.__dni = dni
        self.__Nombre = nombre
        self.__Apellido = apellido
        self.__millas_acum= millas_acum
    
    def __str__(self):
        return ("{} {} \nNumero de viajero:{}\nDNI:{} \nMillas Acumuladas:{}".format(self.__Nombre,self.__Apellido,self.__num_viajero,self.__dni,self.__millas_acum))
    
    def __add__(self,millas):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__Nombre,self.__Apellido,self.__millas_acum+millas)

    def __sub__(self,millas):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__Nombre,self.__Apellido,self.__millas_acum-millas)

    def __gt__(self,other):
        if(type(self) == type(other)):
            return (self.__millas_acum > other.__millas_acum)

    def __eq__(self,millas):
        return (self.cantidadTotalMillas() == millas)
    
    def __radd__ (self, millas):
        print("Millas acumuladas con exito")
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__Nombre,self.__Apellido,self.__millas_acum+millas)
     
    def __rsub__(self, millas):
        if(self.cantidadTotalMillas()> millas):
            print("Millas canjeadas con exito")
            return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__Nombre,self.__Apellido,self.__millas_acum-millas)
        else:
            print("No se puede efectuar la operacion")
        
    def GetNumViaj(self):
        return self.__num_viajero

    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self,MillasRecorridas):
        print("Millas acumuladas:{}".format(self.__millas_acum))
        print("Millas recorridas: {}".format(MillasRecorridas))
        self.__millas_acum =self.__millas_acum + MillasRecorridas
        print("".center(20,"-"))
        print("Millas Totales: {}".format(self.__millas_acum))
        print("".center(20,"-"))

    def canjearMillas(self,Canje):
        print("Millas acumuladas:{}".format(self.__millas_acum))
        print("Millas a canjear: {}".format(Canje))
        if(self.__millas_acum<Canje):
            print("Usted posee millas insuficiente")
        else:
            self.__millas_acum = self.__millas_acum - Canje
            print("".center(20,"-"))
            print("Millas Totales: {}".format(self.__millas_acum))
            print("".center(20,"-"))
