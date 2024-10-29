def main():
    c = 0
    print("Bienvenido al programa, ingrese(A): Para calcular su deuda, ingrese(S): para salir del programa:")
    ini = input()
    if ini == "A":
        while (c < 3):
            print("Bienvenido, por favor ingrese los siguientes datos:")
            print("Ingresa tus iniciales(Preferiblemente de 4 letras):")
            I = input()
            print("Ingrese la clave correspondiente a un numero entero positivo de 4 digitos:")
            C = int(input())
            print("Ingrese la deuda correspondiente a un numero entero positivo de 4 o 5 digitos:")
            D = int(input())
        
            # Validar iniciales
            if(len(I) != 7):
                print("Las iniciales son: ", I)
            else:
                print("Los datos de las iniciales no son validos")

            # Validar clave
            if(C >= 1000) and (C <= 9999):
                print("La clave es: ", C)
            else:
                print("La clave ingresada no es valida")
        
            # Validar deuda
            if(D >= 1000) and (D <= 99999):
                print("La deuda es: ",D,"BS")
            else:
                print("La deuda ingresada no es valida")
            
            # Calcular pago minimo de deuda
            MI = ((30 * D) / 100)
            DI = (D + MI)
            PM = (DI / 12)

            print("La tasa de interes fija es del 30%")
            print("La deuda con el monto de interes anual es: ", DI,"BS")
            print("El pago minimo es: ", PM,"BS")
    else:
        print("Saliendo del programa")
        
        
        c+=1
main()