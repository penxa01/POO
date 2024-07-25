from tkinter import *
from tkinter import ttk, messagebox
import requests

class aplicacion():
    __ventana = None
    __pesos = None
    __dolares =None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('270x125')
        self.__ventana.resizable(0,0)
        self.__ventana.title('Conversor $USD a $AR')
        
        self.mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5", relief = 'sunken',borderwidth= 2)
        self.mainframe.place(x = 0, y =0)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.__dolares = StringVar()
        self.__pesos = StringVar()

        self.__dolares.trace('w', self.calcular)
        self.dolaresEntry = ttk.Entry(self.mainframe, width=7, textvariable=self.__dolares)
        self.dolaresEntry.grid(column=2, row=1, sticky=(W, E),padx=5, pady=5)

        self.et1 =ttk.Label(self.mainframe, textvariable=self.__pesos).grid(column=2, row=2, sticky=(W, E),padx=5, pady=5)
        self.bt1 =ttk.Button(self.mainframe, text='Salir', command=quit).grid(column=3, row=3, sticky=W,padx=5, pady=5)
        self.et2 =ttk.Label(self.mainframe, text="dólares").grid(column=3, row=1, sticky=W,padx=5, pady=5)
        self.et3 =ttk.Label(self.mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E,padx=5, pady=5)
        self.et4 =ttk.Label(self.mainframe, text="pesos").grid(column=3, row=2, sticky=W,padx=5, pady=5)

        self.dolaresEntry.focus()
        self.__ventana.mainloop()
    


    def calcular(self, *args):
        datos = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
        datos = datos.json()
        valorVenta = float(datos[0]["casa"]["venta"].replace(",", "."))
        if self.dolaresEntry.get()!='':
            try:
                valor=float(self.dolaresEntry.get())
                self.__pesos.set("{}".format(round(valorVenta*valor,2)))
            except ValueError:
                messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico')
                self.__dolares.set('')
                self.__pesos.set('')
                self.dolaresEntry.focus()
        else:
            self.__pesos.set('')
    
    def ejecutar(self):
        self.__ventana.mainloop()
    
if __name__ == '__main__':
    conversor = aplicacion()
    conversor.ejecutar()
