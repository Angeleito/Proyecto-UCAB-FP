def main():
  c = 0
  while True:
    print("Bienvenido al programa para calcular su pago minimo de deuda, ingrese (A): Para calcular su deuda, ingrese (S): para salir del programa:")
    ini = input()
    if (ini == "S"):
      print("Saliendo del programa")
      break
    elif (ini == "A"):
      while c < 3:
        print("Bienvenido, por favor ingrese los siguientes datos:")
        print("Ingresa en mayusculas tus iniciales(Preferiblemente de 4 letras):")
        I = input()
        if not (len(I) != 2 and len(I) != 6):
          print("Los datos de las iniciales no son válidos")
          continue

        print("Ingrese la clave correspondiente a un numero entero positivo de 4 digitos:")
        C = int(input())
        if(C >= 1000) and (C <= 9999):
          print("La clave es:",C)
        else:
          print("La clave ingresada no es valida")

        print("Ingrese la deuda correspondiente a un numero entero positivo de 4 o 5 digitos:")
        D = int(input())
        if(D >= 1000) and (D <= 99999):
          print("La deuda es:",D,"BS")
        else:
          print("La deuda ingresada no es valida")

        print("Las iniciales son:", I)
        print("La clave es:", C)
        print("La deuda es:", D, "BS")

        # Calcular pago mínimo de deuda
        MI = ((30 * D) / 100)
        DI = (D + MI)
        PM = (DI / 12)

        print("La tasa de interés fija es del 30%")
        print("La deuda con el monto de interés es:", DI, "BS")
        print("El pago mínimo es:", PM, "BS")

        print("¿Desea realizar otro cálculo? (S/N)")
        resp = input()
        if (resp != "S"):
          print("Saliendo del programa")
          c = 4
          break

        c += 1
    else:
      print("Opción no válida, intente de nuevo.")
main()
