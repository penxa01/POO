from ClaseConjunto import conjunto
import os
class Menu:
    __A = conjunto()
    __B = conjunto()

    __op = 0


    

    def __init__(self, op = 0):
        self.__op = op

    def suma(self):
       print("SUMA DE CONJUNTOS".center(20,"-"))
       suma = self.__A + self.__B
       suma.mostrarConj()
       print("Suma realizada con exito")

    def resta(self):
        print("RESTA DE CONJUNTOS")
        resta = self.__A - self.__B
        resta.mostrarConj()
        print("Resta realizada con exitos")

    def igualar(self):
        print("IGUALAR CONJUNTOS")
        if(self.__A == self.__B):
            print("Los conjuntos son iguales")
        else:
            print("Los conjuntos son distintos")

        
    def opciones(self):
        self.__A.cargar()
        self.__B.cargar()
        os.system("cls")
        continuar = True


        while continuar:
            print("[1] Para hacer la operacion A+B entre conjuntos(SUMA)")
            print("[2] Para hacer la operacion A-B entre conjuntos(RESTA)")
            print("[3] Para comparar conjuntos A == B")
            print("[0] Para salir del menu")
            self.__op = int(input("INGRESE OPCION DESEADA\n"))
            os.system("cls")

            if(self.__op == 1):
                self.suma()
            elif(self.__op ==2):
                self.resta()
            elif(self.__op ==3):
                self.igualar()
            elif(self.__op == 0):
                continuar = not continuar
                print("MUCHAS GRACIAS")
            else: 
                print("Opcion incorrecta, ingrese nuevamente")
            

        