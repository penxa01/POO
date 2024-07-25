from ManejadorMedicamentos import ManejadorMedicamentos
from ManejadorCamas import ManejadorCamas
import os

if __name__ == "__main__":

    Camas = ManejadorCamas()
    Medicamentos = ManejadorMedicamentos()

    print("ITEM 1 Y 2")
    print(" SE CARGA EL ARREGLO DE CAMAS")
    Camas.CargarCamas()
    input("Presione ENTER para continuar")
    os.system("cls")
    print("SE CARGA LA LISTA DE MEDICAMENTOS")
    Medicamentos.cargarMedicamentos()
    input("Presione ENTER para continuar")
    os.system("cls")
    print("ITEM 3")
    print("DAR PACIENTE DE ALTA")
    Camas.DarAlta(Medicamentos.Lista())
    input("Presione ENTER para continuar")
    os.system("cls")
    print("ITEM 4")
    print("LISTAR PACIENTES CON DIAGNOSTICO INGRESADO POR TECLADO")
    Camas.Listar()
    