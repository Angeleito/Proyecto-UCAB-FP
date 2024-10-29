import os

clientes = []

def cargar_datos_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
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
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {nombre_archivo}.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

def cargar_datos_manual():
    iniciales = input("Ingrese las iniciales del cliente (4 letras): ").strip()
    clave = input("Ingrese la clave de la tarjeta (4 dígitos distintos): ").strip()
    deuda = input("Ingrese la deuda del cliente (4 o 5 dígitos): ").strip()
    if validar_datos_cliente(iniciales, clave, deuda):
        clientes.append((iniciales, clave, deuda))
    else:
        print("Datos inválidos. Por favor, intente de nuevo.")

def validar_datos_cliente(iniciales, clave, deuda):
    if len(iniciales) != 4 or not iniciales.isalpha():
        return False
    if len(clave) != 4 or not clave.isdigit() or len(set(clave)) != 4:
        return False
    if not (4 <= len(deuda) <= 5) or not deuda.isdigit():
        return False
    return True

def mostrar_datos():
    if not clientes:
        print("No hay datos disponibles.")
        return
    for cliente in clientes:
        print(f"Iniciales: {cliente[0]}, Clave: {cliente[1]}, Deuda: {cliente[2]}")

def calcular_pago_minimo():
    if not clientes:
        print("No hay datos disponibles.")
        return
    for cliente in clientes:
        pago_minimo = calcular_pago_minimo_cliente(int(cliente[2]))
        print(f"Iniciales: {cliente[0]}, Deuda: {cliente[2]}, Pago Mínimo: {pago_minimo}")

def calcular_pago_minimo_cliente(deuda):
    return round(deuda * 0.05, 2)

def crear_archivo_salida(nombre_archivo):
    try:
        with open(nombre_archivo, 'w') as archivo:
            for cliente in clientes:
                pago_minimo = calcular_pago_minimo_cliente(int(cliente[2]))
                archivo.write(f"{cliente[0][0]}{cliente[0][1]}\n")
                archivo.write(f"{pago_minimo}\n")
        print(f"Archivo de salida {nombre_archivo} creado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al crear el archivo de salida: {str(e)}")

def menu():
    while True:
        print("\nMenú:")
        print("1. Cargar datos del archivo o de forma manual")
        print("2. Mostrar los datos almacenados")
        print("3. Calcular y mostrar el pago mínimo de cada cliente")
        print("4. Crear el archivo de salida (Clitarsal.txt)")
        print("5. Salir del programa")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            fuente = input("¿Desea cargar los datos desde el archivo (a) o manualmente (m)? ").strip().lower()
            if fuente == 'a':
                cargar_datos_desde_archivo('Clitarent.txt')
            elif fuente == 'm':
                cargar_datos_manual()
            else:
                print("Opción no válida.")
        elif opcion == '2':
            mostrar_datos()
        elif opcion == '3':
            calcular_pago_minimo()
        elif opcion == '4':
            crear_archivo_salida('Clitarsal.txt')
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

# Ejecutar el menú
menu()