from ClaseMail import Email
import csv
import os

if __name__ == "__main__":
    mailItem1= Email("","","","1234")
    mailItem3 = Email("","","","")
    #Item 1
    persona= input("Ingrese nombre del usuario\n")
    Mail=input ("Ingrese su correo electronico\n")
    mailItem1.CrearCuenta(Mail)
    print("Estimado {} te enviaremos tus mensajes a la direccion de correo {}".format(persona,mailItem1.RetornaMail()))
    print("La contraseña por defecto es 1234\nSe solicita actualizar\n ")
    #Item 2
    Contra= input("Ingrese Contraseña actual\n")
    mailItem1.CambioPass(Contra)
    #Item 3
    NuevoMail= input("Ingrese mail que desea crear\n")
    mailItem3.CrearCuenta(NuevoMail)
    #Item4
    rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
    Archivo = os.path.join(rutaAbsoluta, "ArchivoMails.csv")
    archivo =open(Archivo)
    cont = 0
    reader = csv.reader(archivo,delimiter = ";")
    IDPrueba= input(" Ingrese ID que desea verificar\n")
    mailItem4= Email()
    for comp in reader:
            for i in range(10): 
                mailItem4.CrearCuenta(comp[i])
                ident = mailItem4.Getid()
                if IDPrueba == ident:
                    cont += 1
    print("Hay {} mail con el ID {}\n".format(cont,IDPrueba))
    archivo.close()


    