import tkinter as tk
from tkinter import ttk

from ProvinciaForm import ProvinciaForm
#En caso de modificar algun atributo de provincia, se agregan funciones que se encargan de modificar el atributo en la lista de VistaProvincias
class UpdateProvincia(ProvinciaForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, True, **kwargs)
    def limpiar(self):
        self.clean()