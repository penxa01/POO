from tkinter import *
from tkinter import ttk

class appIVA():
    __ventana = None

    def __init__(self):
        #Titulo
        self.__ventana = Tk()
        self.__ventana.title('Calculadora IVA')
        self.__ventana.geometry('350x307')
        self.__ventana.resizable(0,0)
        self.titulo = ttk.Label(self.__ventana, text = 'Calculo de IVA', background= 'Light Blue')
        self.titulo.pack(side = TOP, fill= BOTH,ipadx= 10, ipady= 10)
        self.separador = ttk.Separator(self.__ventana, orient = HORIZONTAL)
        self.separador.pack(side = TOP, fill =X )
        #Variables de datos
        self.__valor = IntVar()
        self.__precioSinIVA =StringVar()
        self.__IVA = StringVar()
        self.__precioConIVA = StringVar()
        self.__precioSinIVA.set('')
        self.__IVA.set('')
        self.__precioConIVA.set('')
        self.__valor.set('')
        self.__mensaje = StringVar()
        self.__mensaje.set('Ingrese precio')
        
        self.et1 = ttk.Label(self.__ventana, text = 'Precio sin IVA')
        self.et1.place(x = 30, y= 60)
        self.et2 = ttk.Label(self.__ventana, text = 'IVA')
        self.et2.place(x = 30, y= 170)
        self.et3 = ttk.Label(self.__ventana, text = 'Precio Con IVA')
        self.et3.place(x = 30, y= 200)
        self.et4 = ttk.Label(self.__ventana, textvariable = self.__mensaje)
        self.et4.place (x= 150, y= 80)
        self.et4.configure(foreground='black')

        self.en1 = ttk.Entry(self.__ventana, textvariable = self.__precioSinIVA, width = 20)
        self.en1.place(x = 150, y =60)
        self.en2 = ttk.Entry(self.__ventana, textvariable = self.__IVA, width = 20,)
        self.en2.place(x = 150, y =170)
        self.en3 = ttk.Entry(self.__ventana, textvariable = self.__precioConIVA, width = 20)
        self.en3.place(x = 150, y =200)

        self.bt1 = ttk.Button(self.__ventana, text = 'Salir',padding = (5,5),command = quit)
        self.bt1.place(x = 230, y = 250)
        self.bt1 = ttk.Button(self.__ventana, text = 'Calcular',padding = (5,5),command = self.calcular,)
        self.bt1.place(x = 30, y = 250)

        ttk.Radiobutton(self.__ventana,text = 'IVA 21 %', value =0, variable = self.__valor).place(x = 30, y = 100)
        ttk.Radiobutton(self.__ventana,text = 'IVA 10.5 %', value =1, variable = self.__valor).place(x = 30, y = 130)

    def definirIVA(self):
        iva = 0.0
        if self.__valor.get() == 0:
            iva = 0.21
        elif self.__valor.get() == 1:
            iva = 0.105
    
        return iva

    def calcular(self):
        try:
            iva = self.definirIVA()
            resultado =round(float(self.__precioSinIVA.get()) * float(iva),2)
            self.__IVA.set('{}'.format(resultado))
            self.__precioConIVA.set('{}'.format(float(self.__precioSinIVA.get()) + resultado))
        except:
            self.__mensaje.set('El valor ingresado es erroneo')
            self.et4.configure(foreground='red')

    def ejecutar(self):
        self.__ventana.mainloop()
    
if __name__ == '__main__':
    app = appIVA()
    app.ejecutar()