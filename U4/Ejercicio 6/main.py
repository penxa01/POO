
from VistaProvincia import ProvinciasView
from Controlador import Controlador
from Mprovincias import ManejaProvincia
from ObjectEncoder import ObjectEncoder
#Inicializa el object encoder, lo decodifica y luego se inicializa la vista y el controlador
if __name__ == "__main__":
    encoder = ObjectEncoder()
    try: 
        aux=encoder.Leer("datos.json")
        aux=encoder.Decoder(aux)

    except FileNotFoundError:
        aux=ManejaProvincia()
    #Se realiza la vinculacion entre el controlador y se setea en la vista
    vista=ProvinciasView()
    control=Controlador(vista, aux)
    vista.setControlador(control)
    control.start()
    encoder.Guardar(control.salir(), "datos.json") 
    