class Paciente:
    def __init__(self, nombre,apellido, telefono, altura, peso):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__altura = altura
        self.__peso = peso

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getTelefono(self):
        return self.__telefono

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso

    def setNombre(self, nombre):
        self.nombre = nombre

    def set__apellido(self, apellido):
        self.__apellido = apellido

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def setAltura(self, altura):
        self.__altura = altura

    def setPeso(self, peso):
        self.__peso = peso

    def __str__(self):
        return "Nombre: " + self.nombre + "\n__apellido: " + self.__apellido + "\nTelefono: " + self.__telefono + "\nAltura: " + self.__altura + "\nPeso: " + self.__peso
    
    def toJSON(self):
        d = {
            "__class__": self.__class__.__name__,
            "__atributos__": {
                "nombre": self.__nombre,
                "apellido": self.__apellido,
                "telefono": self.__telefono,
                "altura": self.__altura,
                "peso": self.__peso
            }
        }
        return d