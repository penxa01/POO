from Repositorio import RespositorioPacientes
from Vista import PatientView
from Controlador import ControladorPacientes
from ObjectEncoder import ObjectEncoder
def main():
    #Se carga el archivo JSon y se inicializa el repositorio, la vista y el controlador
    conn=ObjectEncoder('pacientes.json')
    repo=RespositorioPacientes(conn)
    vista=PatientView()
    #Se realiza una referencia circular entre el controlador y la vista
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
if __name__ == "__main__":
    main()