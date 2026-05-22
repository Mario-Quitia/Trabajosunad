# ---------------------------------------------------
# Programa: Videoteca Digital
# Descripción:
# El usuario registra películas en una matriz.
# Se valida que la calificación esté entre 0 y 10.
# ---------------------------------------------------

# Crear matriz vacía
matrizpeliculas = []

# Solicitar cantidad de películas
cantidad = int(input("Ingrese la cantidad de películas a registrar: "))

# Ciclo para registrar películas
for i in range(cantidad):

    print(f"\nRegistro de película {i + 1}")

    # Pedir título
    titulo = input("Ingrese el título de la película: ")

    # Validar calificación
    while True:

        try:
            calificacion = float(input("Ingrese la calificación (0.0 - 10.0): "))

            if 0.0 <= calificacion <= 10.0:
                break

            else:
                print("La calificación debe estar entre 0.0 y 10.0.")

        except ValueError:
            print("Error: ingrese un número válido.")

    # Pedir género
    genero = input("Ingrese el género: ")

    # Pedir año
    anio = int(input("Ingrese el año de lanzamiento: "))

    # Guardar datos en la matriz
    matrizpeliculas.append([titulo, calificacion, genero, anio])

# Mostrar películas registradas
print("\nPelículas registradas:")

for pelicula in matrizpeliculas:
    print(pelicula)
