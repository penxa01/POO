import os
import csv
from ClaseMedicamentos import medicamento

class ManejadorMedicamentos():
    __Medicamentos = None

    def __init__(self):
        self.__Medicamentos = []

    def cargarMedicamentos(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "medicamentos.csv")
        archivo = open(Archivo)
        reader = csv.reader(archivo,delimiter = ";")
        cabeza = True

        for comp in reader:
            if cabeza:
                cabeza = not cabeza
            else:
                NuevoMed = medicamento(int(comp[0]),int(comp[1]),comp[2],comp[3],comp[4],int(comp[5]),float(comp[6]))
                self.__Medicamentos.append(NuevoMed)

        archivo.close()

    def Lista(self):
        return self.__Medicamentos