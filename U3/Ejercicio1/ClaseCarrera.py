class Carrera:
    __codFacu = 0
    __Codigo = 0
    __Nombre = " "
    __Duracion = " "
    __Titulo = " "

    def __init__(self,codFac,cod,nombre,titulo,duracion):
        self.__codFacu = codFac
        self.__Codigo = cod
        self.__Nombre = nombre
        self.__Duracion = duracion
        self.__Titulo = titulo
    
    def __str__(self):
        return ("Codigo de Facultad:{}      Codigo de Carrera:{}\n Nombre:{}      Duracion{}\nTitulo:{}".format(self.__codFacu,self.__Codigo,self.__Nombre,self.__Duracion,self.__Titulo))
    
    def getNombre(self):
        return self.__Nombre

    def getDuracion(self):
        return self.__Duracion