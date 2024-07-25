from ClasePaciente import Paciente
from ObjectEncoder import ObjectEncoder
from ManejadorPacientes import ManejadorPacientes
#Vincula el ObjectEncoder(archivo JSon) con el manejador 
class RespositorioPacientes(object):
    __conn=None
    __manejador=None
    def __init__(self, conn):
        #Conn == ObjectEncoder
        self.__conn = conn
        #Se decodifica el archivo Json
        diccionario=self.__conn.leerJSONArchivo()
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)
    #Funciones del manejador
    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()
    def agregarPaciente(self, paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente
    def modificarPaciente(self, paciente):
        self.__manejador.updatePaciente(paciente)
        return paciente
    def borrarPaciente(self, paciente):
        self.__manejador.deletePaciente(paciente)
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())