# _____________________
# Programa Videoteca digital
# Descripción: Programa que permite gestionar una videoteca digital...
# Este programa permite registrar películas ingresadas por el usuario...
# Año de lanzamiento
# Estudiante: Mario Quitiaquez Rosero
# Fecha: 2026-05-21

#Crear matriz para almacenar la información de las películas

matriz_peliculas = []
#ingresar cantidad de películas a registrar 
cantidad_peliculas = int(input("Ingrese la cantidad de películas a registrar: "))                       
# Ciclo para ingresar la información de cada película
for i in range(cantidad_peliculas): 
    print(f"\nRegistro de película {i+1}:")
    titulo = input("Ingrese el título de la película: ")
    calificacion = float(input("Ingrese la calificación: "))
    año_lanzamiento = int(input("Ingrese el año de lanzamiento de la película: "))
    
    
    
    # Agregar la información de la película a la matriz
    pelicula = [titulo, año_lanzamiento]
    matriz_peliculas.append(pelicula)     
    # Mostrar matriz completa
print("\nMatriz de películas:")
print(matriz_peliculas)  





