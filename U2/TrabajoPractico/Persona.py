

class persona:
    __legajo = None
    __dni = None
    __apellido = None
    __nombre = None
    __sueldoBasico = None
    #Para el item C agrego un atributo sueldo a cobrar para poder trabajar la sobrecarga de manera adecuada
    __SueldoACobrar= None

    def __init__(self,datos):
        self.__legajo = int(datos[0])
        self.__dni = int(datos[1])  
        self.__apellido = datos[2]
        self.__nombre = datos[3]
        self.__sueldoBasico = float(datos[4])
        self.__SueldoACobrar = self.__sueldoBasico
    
    def getLegajo(self):
        return self.__legajo
    
    def getSueldoBasico(self):
        return self.__sueldoBasico
    
    def getApellido(self):
        return self.__apellido
    
    def getSueldoACobrar(self):
        return self.__SueldoACobrar
    
    def __str__(self):
        return ("Apellido:{}     Nombre:{}\nDNI:{}\nSueldo Basico:${}".format(self.__apellido,self.__nombre,self.__dni,self.__sueldoBasico))
    

    def modificarSueldo(self,codigo,importe):
        if(codigo == "A"):
            self.__SueldoACobrar += importe
        elif(codigo == "D"):
            self.__SueldoACobrar -=importe

    def __gt__(self,otro):
        return (self.__apellido<otro.getApellido())
    
    def __lt__(self,sueldoAComparar):
        return (self.__SueldoACobrar<sueldoAComparar)
        
