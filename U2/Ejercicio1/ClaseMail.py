
class Email:
    __idmail = ""
    __dominio = ""
    __tipoDominio = ""
    __Pass = "1234"
    def __init__(self,idmail, dominio, tipoDominio, Pass):
        self.__idmail= idmail
        self.__dominio = dominio
        self.__tipoDominio= tipoDominio
        self.__Pass= Pass
    def RetornaMail (self):
        return "{}@{}.{}".format(self.__idmail,self.__dominio,self.__tipoDominio)
    def GetDominio(self):
        DominioSolicitado= self.__dominio
        return DominioSolicitado
    def Getid(self):
        IDSolicitado= self.__idmail
        return IDSolicitado
    def CrearCuenta(self, NuevoMail):
        arroba= NuevoMail.rfind("@")
        punto = NuevoMail.rfind(".")
        if (arroba != -1) and (punto!= -1):
            self.__idmail= NuevoMail[:arroba]
            self.__dominio = NuevoMail[ arroba +1 : punto]
            self.__tipoDominio= NuevoMail [punto+1 :]
    def CambioPass (self,NuevaPass):
        print("nueva pass {}".format(NuevaPass))
        print("Contraseña actual {}".format(self.__Pass))
        if (NuevaPass == self.__Pass):
            NuevaPass= input( "Ingrese nueva contraseña,debe poseer como minimo 8 caracteres\n")
            if(len(NuevaPass) < 8):
                print("La contraseña no es valida\n")
            else:
                aux = input( "Ingrese NUEVAMENTE la contraseña: ")
                if aux == NuevaPass :
                    self.__Pass = NuevaPass
                    print(" La contraseña ha sido cambiada con exito\n")
                else: print("Contraseña incorrecta\n")
        else :print(" Contraseña ingresada es incorrecta\n")
