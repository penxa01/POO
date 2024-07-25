
class Palindromo:
    __palabra = None
    
    def __init__(self, palabra = ""):
        self.__palabra = palabra

    def esPalindromo(self):
        i=0
        j=len(self.__palabra)
        bandera = True
        while i<abs(j) and bandera:
           if self.__palabra[i] != self.__palabra[j-1]:
               bandera=False
           else:
               i += 1
               j -= 1
        return bandera
    
    def getLongitud(self):
        return len(self.__palabra)
    
    def parImpar(self):
        paridad = False

        if((len(self.__palabra)%2) == 0):
            paridad = True
        
        return paridad
        
    def setPalabra(self, nuevaPalabra):
        self.__palabra = nuevaPalabra
    
    def getPalabra(self):
        return self.__palabra
    
    def __ne__(self,otro):
        return self.__palabra != otro.getPalabra()