from ClasePaciente import Paciente

class ManejadorPacientes:
    indice=0
    __pacientes=None
    def __init__(self):
        indice = 0
        self.__pacientes=[]
    def agregarPaciente(self, paciente):
        paciente.rowid=self.indice
        self.indice+=1
        self.__pacientes.append(paciente)
    def getListaPacientes(self):
        return self.__pacientes
    def deletePaciente(self, paciente):
        indice=self.obtenerIndicePaciente(paciente)
        self.__pacientes.pop(indice)
    def updatePaciente(self, paciente):
        indice=self.obtenerIndicePaciente(paciente)
        self.__pacientes[indice]=paciente
    def obtenerIndicePaciente(self, paciente):
        bandera = False
        i=0
        while not bandera and i < len(self.__pacientes):
            if self.__pacientes[i].rowid == paciente.rowid:
                bandera=True
            else:
                i+=1
        return i
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            pacientes=[paciente.toJSON() for paciente in self.__pacientes]
            )
        return d