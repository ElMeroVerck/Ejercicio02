from Egreso import RegistreUnEgreso
from Ingres import RegistreUnIngreso

UnIntento = RegistreUnIngreso()
OtroIntento = RegistreUnEgreso()
cuenta = 0.0

while True:
    print("Bienvenido a tu banco favorito, donde simpre creemos y aportamos en ti. ")
    print("1- iniciar un proyecto de finanzas personales?")
    print("2- Deseas hacer un retiro?")
    print("3- Deseas hacer un Abono?")
    print("4- Reporte de ingresos")
    print("5- Reporte de egresos")
    print("6- Consulta tu saldo disponible")
    print("0- Salir.")
    option = int(input("Que desea hacer?"))
    if option == 0:
        print("Gracias por usar nuestros servicios.\n Que tenga un buen dia")
        break
    # ---------------------------------------------------
    if option == 1:
        print(
            "Gracias por poner tu confianza en nostros. \n ahora ese parte de esta gran familia."
        )
        print("")
        cuenta = 0.0
        print("-" * 75)
    # ---------------------------------------------------
    if option == 2:
        Retiro = float(input("Ingresa el monto que deseas Retirar. "))

        cuenta = cuenta + Retiro

        OtroIntento.AgregarUnEgreso(Retiro)

        print("Realizaste retiro por: $ " + str(Retiro))

        print("-" * 75)
    # -----------------------------------------------------

    if option == 3:
        Abono = float(input("Ingresa el monto que deseas abonar. $ "))

        cuenta = cuenta + Abono

        print("Realizaste un deposito por: $ " + str(Abono))
        UnIntento.AgregarUnIngres(Abono)
        print("-" * 75)
    # -----------------------------------------------------
    if option == 4:
        print("-" * 75)
        print("Sus abonos son: ")
        print(UnIntento.verReporte())
        print("-" * 75)
    # -----------------------------------------------------
    if option == 5:
        print("-" * 75)
        print("Sus retiros son: ")
        print(OtroIntento.verReporte())
        print("-" * 75)
    # -----------------------------------------------------
    if option == 6:
        print("Tu saldo es:" + str(cuenta))
        print("-" * 75)
