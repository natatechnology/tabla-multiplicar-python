# Maestro, aqui iniciamos importando la libreria para crear una base de datos desde un archivo con SQLite
import sqlite3

# Creamos el archivo y conectamos a la base de datos
conn = sqlite3.connect('base_de_datos.db')
c = conn.cursor()

# Crear la tabla si no existe
c.execute('''CREATE TABLE IF NOT EXISTS historial (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             valor INTEGER NOT NULL,
             resultado TEXT NOT NULL)''')
conn.commit()

# funcion del menu principal
def menu():
    print("Menú:")
    print("1. Mantenimiento")
    print("2. Clientes")
    print("3. Inventario")
    print("4. Tabla de multiplicar")
    print("5. Salir")

# funcion para la multiplicacion
def tabla_multiplicar():
    try:
        valor = int(input("Ingrese un valor para mostrar su tabla de multiplicar: "))
        resultados = []
        for i in range(1, 13):
            resultado = valor * i
            resultados.append(f"{valor} x {i} = {resultado}")
            print(f"{valor} x {i} = {resultado}")

        # Guardar en la base de datos
        c.execute("INSERT INTO historial (valor, resultado) VALUES (?, ?)", (valor, "\n".join(resultados)))
        conn.commit()
        print("Tabla de multiplicar guardada en la base de datos.")
    except ValueError:
        print("Por favor, ingrese un número válido.")


# Aquí es donde en realidad inicia la ejecucion de las funciones creadas anteriormente con un bucle While infinito
while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("Opción de Mantenimiento seleccionada.")
    elif opcion == '2':
        print("Opción de Clientes seleccionada.")
    elif opcion == '3':
        print("Opción de Inventario seleccionada.")
    elif opcion == '4':
        tabla_multiplicar()
    elif opcion == '5':
        print("Saliendo del programa. Pase bueeenas!")
        # ejecutamos el break para salir del bucle y terminar la ejecucion del programa
        break
    else:
        print("Opción no válida. Por favor, seleccione nuevamente.")

# Cerrar la conexión a la base de datos
conn.close()
