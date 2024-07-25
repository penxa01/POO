from functools import partial
from tkinter import ttk as tk
from tkinter import *
from ClaseFraccion import Fraccion
import re
class App:
    __num=0
    __ventana=None
    __entrada=None
    #Se trabajo con un indice para poder crear las funciones que borran la entrada
    __index=0
    __operacion=0
    __segundonumero=0
    __operador=''
    __lista=[]
    __f1=None
    __f2=None

    def __init__(self):
        #Se inicializa la ventana con sus propiedades
        self.__ventana=Tk()
        self.__ventana.geometry("316x260")
        self.__ventana.title("Calculadora")
        self.__ventana.resizable(0,0)
        self.__ventana.config(bg='Light blue')
        self.__entrada=Entry(self.__ventana,width=48,font=('Arial',8,'bold'),bg='white',justify='left')
        self.__entrada.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
        self.botones()
        self.__ventana.mainloop()

    #Recibe como parametro un numero lo inserta en la entrada e incrementa el indice
    def ponernumeros(self,num):
        self.__entrada.insert(self.__index,num)
        self.__index+=1
    #borran uno o todos los caracteres de la entrada
    def borrarentrada(self):
        self.__index=0
        self.__entrada.delete(0,END)

    def borrarindividual(self):
        num=int(self.__index)-1
        self.__entrada.delete(num)
        self.__index-=1
    #Obtiene el numero en caso de ser entero
    def getprimer(self):
        self.__primernumero=int(self.__entrada.get())
        self.__entrada.delete(0,END)
        self.__index=0
   #Convierte el numero en una fraccion     
    def conviertefraccion(self):
        listanumeros=str(self.__entrada.get())
        #Re.findall trabaja la entrada como expresion regular para separar los numeros de la fraccion como una tupla y poder realizar las operaciones
        match=re.findall('[-0-9]+',listanumeros)
        self.__lista.append(match)
        self.__entrada.delete(0,END)
        self.__index=0
        

    #Asigna la variable self.__operador para realizar la operacion correspondiente
    def dividir(self):
        try:
            self.__operador='dividir'
            self.getprimer()
        except:
            self.__operador='dividir'
            self.conviertefraccion()
            pass

    def sumar(self):
        try:
            self.__operador='sumar'
            self.getprimer()
        except:
            self.__operador='sumar'
            self.conviertefraccion()
            pass

    def multiplicar(self):
        try:
            self.__operador='multiplicacion'
            self.getprimer()
        except:
            self.__operador='multiplicacion'
            self.conviertefraccion()
            pass
    
    def restar(self):
        try:
            self.__operador='resta'
            self.getprimer()
        except:
            self.__operador='resta'
            self.conviertefraccion()
            pass
    #Recibe las entradas y las trabaja para convertirlas en fracciones usando la ClaseFraccion
    def operacion(self):
        num1=0
        num2=0
        num3=0
        num4=0
        listanumeros=str(self.__entrada.get())
        #Re.findall trabaja la entrada como expresion regular para separar los numeros de la fraccion como una tupla y poder realizar las operaciones
        match=re.findall('[-0-9]+',listanumeros)
        self.__lista.append(match)
        #Asigna numeradores y denominadores para posteriormente instanciar las fracciones
        num1=self.__lista[0][0]
        num2=self.__lista[0][1]
        num3=self.__lista[1][0]
        num4=self.__lista[1][1]
        self.__f1=Fraccion(num1,num2)
        self.__f2=Fraccion(num3,num4)
        self.__lista.clear()
    #Teniendo en cuenta la variable self.__operador realiza la operacion correspondiente
    def igual(self):
        try:
            if self.__operador=='dividir':
                try:
                    #Primero se contempla si es un numero entero
                    self.__segundonumero=int(self.__entrada.get())
                    if self.__segundonumero!=0:     
                        if self.__primernumero%self.__segundonumero==0:
                            result=self.__primernumero//self.__segundonumero
                            self.__entrada.delete(0,END)
                            self.__entrada.insert(0,result)
                        else:
                            result=self.__primernumero/self.__segundonumero
                            self.__entrada.delete(0,END)
                            self.__entrada.insert(0,result)
                    else:
                        result="ERROR division por 0"
                        self.__entrada.delete(0,END)
                        self.__entrada.insert(0,result)
                except:
                    #Si entra por except es porque es una fraccion
                    self.operacion()
                    r=self.__f1//self.__f2
                    print(r)
                    self.__entrada.delete(0,END)
                    result=self.__f1.simplificar(r)
                    self.__entrada.insert(0,result)

                
            elif self.__operador=='sumar':
                try:
                    #Primero se contempla si es un numero entero
                    self.__segundonumero=int(self.__entrada.get())
                    result=self.__primernumero+self.__segundonumero
                    self.__entrada.delete(0,END)
                    self.__entrada.insert(0,result)
                except:
                    #Si entra por except es porque es una fraccion
                    self.operacion()
                    r=self.__f1+self.__f2
                    self.__entrada.delete(0,END)
                    result=self.__f1.simplificar(r)
                    self.__entrada.insert(0,result)


            elif self.__operador=='multiplicacion':
                try:
                    #Primero se contempla si es un numero entero
                    self.__segundonumero=int(self.__entrada.get())
                    result=self.__primernumero*self.__segundonumero
                    self.__entrada.delete(0,END)
                    self.__entrada.insert(0,result)
                   
                except:
                    #Si entra por except es porque es una fraccion
                    self.operacion()
                    r=self.__f1*self.__f2
                    self.__entrada.delete(0,END)
                    result=self.__f1.simplificar(r)
                    self.__entrada.insert(0,result)
                    
                    
            elif self.__operador=="resta":
                try:
                    #Primero se contempla si es un numero entero
                    self.__segundonumero=int(self.__entrada.get())
                    result=self.__primernumero-self.__segundonumero
                    self.__entrada.delete(0,END)
                    self.__entrada.insert(0,result)

                except:
                    #Si entra por except es porque es una fraccion
                    self.operacion()
                    r=self.__f1-self.__f2
                    self.__entrada.delete(0,END)
                    result=self.__f1.simplificar(r)
                    self.__entrada.insert(0,result)

            #Castea el resultado y lo muestra en la entrada
            r=str(result)
            self.__index=len(r)
            self.__primernumero=0
            self.__segundonumero=0
        except:
            pass



    def botones(self):
        #Se definen los botones que ingresan numeros,operadores, borrar un caracter y limpiar entrada
        borrar=tk.Button(self.__ventana,text="C",command=partial(self.borrarentrada)).grid(row=2,column=0,pady=3,ipady=4)
        dividir=tk.Button(self.__ventana,text="%",command=partial(self.dividir)).grid(row=2,column=3,pady=3,ipady=4)
        #Se considera a '/' como la linea fraccionaria
        separador=tk.Button(self.__ventana,text="/",command=partial(self.ponernumeros,'/')).grid(row=2,column=2,pady=3,ipady=4)
        borrar1=tk.Button(self.__ventana,text="<-",command=partial(self.borrarindividual)).grid(row=2,column=1,pady=3,ipady=4)

        b7=tk.Button(self.__ventana,text="7",command=partial(self.ponernumeros,'7'))
        b7.grid(row=3,column=0,pady=3,ipady=4)
        b8=tk.Button(self.__ventana,text="8",command=partial(self.ponernumeros,'8')).grid(row=3,column=1,pady=3,ipady=4)
        b9=tk.Button(self.__ventana,text="9",command=partial(self.ponernumeros,'9')).grid(row=3,column=2,pady=3,ipady=4)
        bx=tk.Button(self.__ventana,text="x",command=partial(self.multiplicar)).grid(row=3,column=3,pady=3,ipady=4)

        b4=tk.Button(self.__ventana,text="4",command=partial(self.ponernumeros,'4')).grid(row=4,column=0,pady=3,ipady=4)
        b5=tk.Button(self.__ventana,text="5",command=partial(self.ponernumeros,'5')).grid(row=4,column=1,pady=3,ipady=4)
        b6=tk.Button(self.__ventana,text="6",command=partial(self.ponernumeros,'6')).grid(row=4,column=2,pady=3,ipady=4)
        bmenos=tk.Button(self.__ventana,text="-",command=partial(self.restar)).grid(row=4,column=3,pady=3,ipady=4)

        b1=tk.Button(self.__ventana,text="1",command=partial(self.ponernumeros,'1')).grid(row=5,column=0,pady=3,ipady=4)
        b2=tk.Button(self.__ventana,text="2",command=partial(self.ponernumeros,'2')).grid(row=5,column=1,pady=3,ipady=4)
        b3=tk.Button(self.__ventana,text="3",command=partial(self.ponernumeros,'3')).grid(row=5,column=2,pady=3,ipady=4)
        bmas=tk.Button(self.__ventana,text="+",command=partial(self.sumar)).grid(row=5,column=3,pady=3,ipady=4)
        #Permite ingresar numeros o fracciones negativas
        bnegativo=tk.Button(self.__ventana,text="neg",command=partial(self.ponernumeros,'-')).grid(row=6,column=0,pady=3,ipady=4)
        b0=tk.Button(self.__ventana,text="0",command=partial(self.ponernumeros,'0')).grid(row=6,column=1,pady=3,ipady=4,ipadx=40,columnspan=2)

        bigual=tk.Button(self.__ventana,text="=",command=partial(self.igual)).grid(row=6,column=3,pady=3,ipady=4)




if __name__=='__main__':
    app=App()