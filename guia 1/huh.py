encendido=True
saldo=500_000
while encendido:
    try:
        print("Menu Banco")
        print("(1) Para consultar saldo.")
        print("(2) Para retirar dinero.")
        print("(3) Para salir")
        eleccion=int(input("Ingrese la opcion a la que quiera acceder."))
        if eleccion>=1 and eleccion<=3:
            if eleccion==1:
                while True:
                    print(f"tiene un saldo de ${saldo}.")
                    back=input("presione (1) para volver, (2) para salir")
                    try:
                        if back == 2:
                            print("Cierre de sesion exitoso.")
                            encendido=False
                    except:
                        print("Ingrese un valor correcto.")
            elif eleccion == 2:
                while True:
                    print("transferencia realizada.")
                    back=input("presione (1) para volver, (2) para salir")
                    try:
                        if back == 2:
                            print("Cierre de sesion exitoso.")
                            encendido=False
                    except:
                        print("Ingrese un valor correcto.")
            elif eleccion == 3:
                print("Cierre de sesion exitoso.")
                encendido=False
                    
                
    except:
        print("Estimado, 1, 2 o 3.")