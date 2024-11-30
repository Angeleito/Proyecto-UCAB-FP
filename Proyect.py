def main():
  c = 0
  print("Bienvenido al programa para calcular su pago minimo de deuda, ingrese (A): Para calcular su deuda, ingrese (S): para salir del programa:")
  ini = input()
  if (ini == "S"):
    print("Saliendo del programa")
    print("Gracias por usar el programa")
  elif (ini == "A"):
    while c < 3:
      print("Bienvenido, por favor ingrese los siguientes datos:")
      print("Ingresa en letras mayusculas tus iniciales de tus nombres y apellidos:")
      I = input().upper()
      if (len(I) != 2 and len(I) != 6):
        print("Dato valido")
      else:
        print("Las iniciales ingresadas no son validas")
        print("Las iniciales deben ser de 2 o 6 letras")
        print("Las iniciales ingresadas son:", I)

      print("Ingrese la clave correspondiente a un numero entero positivo de 4 digitos diferentes:")
      C = int(input())
      if(C >= 1000) and (C <= 9999):
        C1 = (C // 1000)
        r = (C % 1000)
        C2 = (r // 100)
        r2 = (r % 100)
        C3 = (r2 // 10)
        C4 = (r2 % 10)
        if (C1 != C3) and (C1 != C2) and (C1 != C4) and (C2 != C3) and (C2 != C4) and (C3 != C4):
          print("Dato valido")
        else:
          print("La clave ingresada no es valida")
          print("La clave debe ser un numero entero positivo de 4 digitos diferentes")
          print("La clave ingresada es:",C)
      else:
        print("La clave ingresada no es valida")
        print("La clave debe ser un numero entero positivo de 4 digitos diferentes")
        print("La clave ingresada es:",C)

      print("Ingrese la deuda correspondiente a un numero entero positivo de 4 o 5 digitos:")
      D = int(input())
      if(D >= 1000) and (D <= 99999):
        print("Dato valido")
      else:
        print("La deuda ingresada no es valida")
        print("La deuda debe ser un numero entero positivo de 4 o 5 digitos")
        print("La deuda ingresada es:",D)

      print("Las iniciales son:", I.upper())
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
      if (resp == "N"):
        print("Saliendo del programa")
        c = 4

      c += 1
  else:
    print("Opción no válida, intente de nuevo.")
    main()

main()
