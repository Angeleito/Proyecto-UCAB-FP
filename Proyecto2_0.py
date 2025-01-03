def Validar(a, b, f):
  if (a >= b) and (a <= f) or (a == b):
    return True
  else:
    return False

def PagoMinimo(a):
  MI = ((a * 30) / 100)
  DI = (a + MI)
  PM = (DI / 12)
  return PM

def CargarOIngresarDatos(nombre_archivo):
  print("¿Desea cargar los datos desde un archivo? (S/N): ")
  opcion = input().upper()
  if opcion == 'S':
    archivo = open(nombre_archivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    
    if len(lineas) % 3 != 0:
      print("El archivo tiene un número incorrecto de líneas.")
      return

    for i in range(0, len(lineas), 3):
      iniciales = lineas[i].strip()
      clave = lineas[i+1].strip()
      deuda = lineas[i+2].strip()
      if validar_datos_cliente(iniciales, clave, deuda):
        clientes.append((iniciales, clave, deuda))
      else:
        print(f"Datos inválidos para el cliente en las líneas {i+1}-{i+3}.")

  else:
    IngresarDatos()

def IngresarDatos():
  print("Ingrese sus Iniciales en mayúsculas correspondientes a sus dos nombres y sus dos apellidos:")
  Iniciales = input().upper()
  if not Validar(len(Iniciales), 4, 0):
    print("Datos inválidos")
    return
  print("Ingrese número entero positivo de 4 números (entre 1000 y 9999) correspondiente a la clave de su tarjeta:")
  Clave = int(input())
  if not Validar(Clave, 1000, 9999):
    print("Datos inválidos")
    return
  print("Ingrese su deuda de 4 o 5 números enteros positivos (entre 1000 y 99999) correspondiente a su deuda:")
  Deuda = int(input())
  if not Validar(Deuda, 1000, 99999):
    print("Datos inválidos")
    return
  print("Los datos ingresados son:")
  print("Iniciales:", Iniciales, ", clave de la tarjeta:", Clave, ", deuda de la tarjeta:", Deuda)
  GuardarDatos(Iniciales, Clave, Deuda)
  print("Datos ingresados al archivo")

def GuardarDatos(Iniciales, Clave, Deuda):
  arch = open("C:clientes.txt", "at")
  arch.write("Iniciales: " + Iniciales + ", Clave: " + str(Clave) + ", Deuda: " + str(Deuda) + "\n")
  arch.close()
  GuardarArchivoSalida(Iniciales, Deuda)

def GuardarArchivoSalida(Iniciales, Deuda):
  arch = open("C:Clitarsal.txt", "at")
  arch.write("Iniciales: " + Iniciales + "\n")
  arch.write("Pago Mínimo: " + str(PagoMinimo(Deuda)) + "\n")
  arch.close()
  print("Datos guardados en 'Clientes.txt'.")

def MostrarDatos():
  arch = open("clientes.txt", "rt")
  print("Los datos guardados son:")
  for linea in arch.readlines():
    print(linea)
  arch.close()

def MostrarPagoMinimo(Deuda):
  print("Tu pago minimo es:")
  print(PagoMinimo(Deuda))

def menu():
  print("UCAB")
  print("Bienvenido a tu calculador de deuda, para ingresar presione: 1 = SI, 0 = No")
  a = int(input())
  if a == 1:
    print("Ejecutando programa")
    while True:
      print("\nMenu")
      print("1. Cargar o ingresar datos")
      print("2. Mostrar los datos almacenados")
      print("3. Calcular y mostrar el pago mínimo de cada cliente")
      print("4. Guardar datos de salida")
      print("5. Salir del programa")

      print("Seleccione una opción: ")
      opcion = input()
      if opcion == '1':
        CargarOIngresarDatos("clientes.txt")
      elif opcion == '2':
        MostrarDatos()
      elif opcion == '3':
        print("Ingresa nuevamente tu deuda:")
        Deuda = int(input())
        MostrarPagoMinimo(Deuda)
      elif opcion == '4':
        Iniciales = input("Ingrese las iniciales del cliente para guardar los datos de salida: ").upper()
        Deuda = int(input("Ingrese la deuda del cliente para guardar los datos de salida: "))
        GuardarArchivoSalida(Iniciales, Deuda)
      elif opcion == '5':
        print("Saliendo del programa.")
        break
      else:
        print("Opción no válida.")
  elif a == 0:
    print("Cerrando programa")
  else:
    print("Opción inválida... Intente de nuevo")
    menu()
menu()