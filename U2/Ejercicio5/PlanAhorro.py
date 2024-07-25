
class PlanAhorro: 
    cantidadCuotasPlan = 60
    cantCuotasLicitar = 10

    def __init__(self,codigo = 0,modelo = " ",version = " ",val = 0.0):
        self.__CodPlan = codigo
        self.__modelo = modelo
        self.__Version = version
        self.__Valor = val
    
    def __str__(self):
        return ("COD. PLAN:{} \n MODELO: {}\n VERSION: {} \n VALOR: ${}".format(self.__CodPlan,self.__modelo,self.__Version,self.__Valor))
    
    def getCodigo(self):
        return self.__CodPlan
    
    def getModelo(self):
        return self.__modelo
    
    def getVersion(self):
        return self.__Version
    
    def getValor(self):
        return self.__Valor
    
    def modificarValor(self,valor):
        self.__Valor = valor
        return 
    
    @classmethod
    def retornaCuotas(cls):
        return cls.cantidadCuotasPlan
    
    @classmethod
    def retornarCuotasLicitar(cls):
        return cls.cantCuotasLicitar

    @classmethod
    def modificarCuotasLicitar(cls,cuotas):
        cls.cantCuotasLicitar =  cuotas
        print("Cambio realizado con exito")
        return
    @classmethod
    def mostrarCuotasLicitar(cls):
        return print("Cuotas necesarias para licitar el vehiculo: {}".format(cls.cantCuotasLicitar))

    