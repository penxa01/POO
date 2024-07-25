from tkinter import *
from tkinter import ttk,font

class calculadoraIMC():
    
    def __init__(self):
        #Propiedades de la ventana
        self.__ventana = Tk()
        self.__ventana.title('Calculadora de IMC')
        self.__ventana.geometry('420x200')
        self.__ventana.resizable(0,0)
        #Etiquetas, definicion y ubicacion
        self.etiqueta1 = ttk.Label(self.__ventana, text ='Peso corporal:',font = font.Font(family = 'Arial',weight = 'bold', underline= True))
        self.etiqueta1.place(x = 10,y = 10)
        self.etiqueta2 = ttk.Label(self.__ventana, text ='Estatura:',font = font.Font(family = 'Arial',weight = 'bold', underline= True))
        self.etiqueta2.place(x = 10,y = 50)
        self.etiqueta3 = ttk.Label(self.__ventana, text ='cm',font = font.Font(family = 'Arial',weight = 'bold'))
        self.etiqueta3.place(x = 380,y = 50)
        self.etiqueta4 = ttk.Label(self.__ventana, text ='Kg',font = font.Font(family = 'Arial',weight = 'bold'))
        self.etiqueta4.place(x = 380,y = 10)
        #Variables de datos
        self.__peso = IntVar()
        self.__peso.set('')
        self.__estatura = IntVar()
        self.__estatura.set('')
        self.__mensaje = StringVar()
        self.__mensaje.set('Ingrese los datos requeridos para calcular su IMC')
        self.__Composicion = StringVar()
        self.__Composicion.set('')
        #Entradas de datos,definicion y ubicacion
        self.entrada1 = ttk.Entry(self.__ventana, textvariable= self.__peso, width = 40)
        self.entrada1.place(x = 130, y = 10)
        self.entrada2 = ttk.Entry(self.__ventana, textvariable= self.__estatura, width = 40)
        self.entrada2.place(x = 130, y = 50)
        #Separador y mensaje de resultado
        self.separador =ttk.Separator(self.__ventana,orient = HORIZONTAL)
        self.separador.place(x = 5, y = 90,bordermode = OUTSIDE,height=10,width=410)
        self.etiqComposicion = ttk.Label(self.__ventana,textvariable = self.__Composicion,font = font.Font(family = 'Arial',weight = 'bold'),foreground = 'blue')
        self.etiqComposicion.pack(side = BOTTOM)
        self.etiqMensaje = ttk.Label(self.__ventana,textvariable = self.__mensaje,font = font.Font(family = 'Arial',weight = 'bold'),foreground = 'blue')
        self.etiqMensaje.pack(side = BOTTOM)
        #Botones
        self.botonCalcular = ttk.Button(self.__ventana, text="Calcular",padding=(30,5), command=self.calcularIMC)
        self.botonCalcular.place(x =20, y =100)
        self.botonLimpiar = ttk.Button(self.__ventana,text = 'Limpiar',padding= (30,5), command = self.Limpiar)
        self.botonLimpiar.place(x = 270, y = 100)

    #Funcion del boton calcular
    def calcularIMC(self):
        try:
            resultado = float(self.entrada1.get())/ ((float(self.entrada2.get())/100)**2)
            resultado =round(resultado,1)
            self.etiqMensaje.configure(foreground= 'blue')
            if(resultado < 18.5):
                self.__mensaje.set('Tu Indice de masa Corporal (IMC) es: {}Kg/m2'.format(resultado))
                self.__Composicion.set('Peso Inferior al normal')
            elif(resultado>18.5 and resultado <24.9):
                self.__mensaje.set('Tu Indice de masa Corporal (IMC) es: {}Kg/m2'.format(resultado))
                self.__Composicion.set('Normal')
            elif(resultado>25.0 and resultado <29.9):
                self.__mensaje.set('Tu Indice de masa Corporal (IMC) es: {}Kg/m2'.format(resultado))
                self.__Composicion.set('Peso Superior al normal')
            elif(resultado> 30.0):
                self.__mensaje.set('Tu Indice de masa Corporal (IMC) es: {}Kg/m2'.format(resultado))
                self.__Composicion.set('Obesidad')
        except ValueError:
            self.etiqMensaje.configure(foreground= 'red')
            self.__mensaje.set('Alguno de los datos ingresados no es valido')
            self.__Composicion.set('')

    #Funcionalidad del boton Limpiar
    def Limpiar(self):
        self.__peso.set('')
        self.__estatura.set('')
        self.__mensaje.set('Ingrese los datos requeridos para calcular su IMC')
        self.__Composicion.set('')

    #Permite que la ventana no se cierre instantaneamente
    def ejecutar(self):
        self.__ventana.mainloop()


if __name__ == '__main__':
    app = calculadoraIMC()
    app.ejecutar()