from ClaseCarrera import Carrera

class Facultad:
    __codigo =0
    __Nombre = " "
    __direccion = " "
    __localidad = " "
    __Telefono = 0
    __CantCarr= []

    def __init__(self,cod ,nombre ,direc ,local,tel):
        self.__codigo = cod
        self.__Nombre = nombre 
        self.__direccion = direc
        self.__localidad = local
        self.__Telefono = tel
        self.__CantCarr= []

    def __str__(self):
        return ("Codigo:{}\nNombre:{}       Direccion:{}\nTelefono:{}".format(self.__codigo,self.__Nombre,self.__direccion,self.__Telefono))
    
    def __del__(self):
        print("Borrando facultad y carreras que pertenecen a la misma")
        del self.__CantCarr
        
    def getNombre(self):
        return self.__Nombre
    
    def getCodigo(self):
        return self.__codigo

    def agregarCarrera(self,fila):
        self.__CantCarr.append(Carrera(int(fila[0]),int(fila[1]),fila[2],fila[3],fila[4]))
        

    def buscarCarrera(self,carrera):
        i = 0
        band = False
        while(i<len(self.__CantCarr)) and (band == False):
            if(self.__CantCarr[i].getNombre().lower() == carrera.lower()):
                band = True
            else:
                i +=1
        if band:
            print("Carrera Encontrada")
            indice = i
            i = self.__CantCarr[indice]    
        else:
            i = -1
        
        return i
                
                
    def mostrarInfoCarreras(self):
        for carrera in self.__CantCarr:
            print("Nombre:{}".format(carrera.getNombre()))
            print("Duracion:{}".format(carrera.getDuracion()))
            print("".center(20,"-"))