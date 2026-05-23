"""
Módulo interactivo para la gestión de una matriz de películas (CRUD).

Este script implementa las buenas prácticas de programación en Python:
- Separación estricta de funciones y lógica de ejecución.
- Modularización de validaciones para evitar la duplicación de código.
- Manejo seguro de errores de tipo de datos (ValueError).
"""

# =====================================================================
# 1. SECCIÓN DE FUNCIONES AUXILIARES (VALIDACIONES DE ENTRADA)
# =====================================================================

def solicitar_titulo():
    """Solicita el título y asegura que no sea una cadena vacía."""
    while True:
        titulo = input("Por favor, ingrese el título de la película: ").strip()
        if titulo != "":
            return titulo
        print("Error: el título no puede estar vacío.")


def solicitar_anio():
    """Solicita el año y valida que sea un entero entre 1888 y 2026."""
    while True:
        try:
            anio = int(input("Por favor, ingrese el año de lanzamiento (1888 - 2026): "))
            if 1888 <= anio <= 2026:
                return anio
            print("Error: el año debe estar entre 1888 y 2026.")
        except ValueError:
            print("Error: debe ingresar un número entero para el año.")


def solicitar_calificacion():
    """Solicita la calificación y valida que sea un número entre 0.0 y 10.0."""
    while True:
        try:
            calificacion = float(input("Por favor, ingrese la calificación (0.0 - 10.0): "))
            if 0.0 <= calificacion <= 10.0:
                return calificacion
            print("Error: la calificación debe estar entre 0.0 y 10.0.")
        except ValueError:
            print("Error: debe ingresar un número válido para la calificación.")


def solicitar_genero():
    """Solicita el género y asegura que no sea una cadena vacía."""
    while True:
        genero = input("Por favor, ingrese el género de la película: ").strip()
        if genero != "":
            return genero
        print("Error: el género no puede estar vacío.")


# =====================================================================
# 2. SECCIÓN DE FUNCIONES PRINCIPALES (OPERACIONES DEL MENÚ / CRUD)
# =====================================================================

def registrar_peliculas(matriz):
    """Permite el ingreso ordenado y obligatorio de nuevas películas."""
    try:
        cantidad = int(input("\n¿Cuántas películas desea registrar?: "))
        for i in range(cantidad):
            print(f"\n========== REGISTRANDO PELÍCULA {i + 1} ==========")
            titulo = solicitar_titulo()
            anio = solicitar_anio()
            calificacion = solicitar_calificacion()
            genero = solicitar_genero()
            
            matriz.append([titulo, anio, calificacion, genero])
        print(f"\n¡Se han registrado {cantidad} película(s) con éxito!")
    except ValueError:
        print("Error: Ingrese una cantidad válida de películas.")


def mostrar_peliculas(matriz):
    """Muestra los elementos de la matriz en forma de lista numerada."""
    if not matriz:
        print("\nNo hay películas registradas en el sistema.")
        return False
    
    print("\n========== PELÍCULAS REGISTRADAS ==========")
    for indice, p in enumerate(matriz):
        print(f"[{indice + 1}] Título: {p[0]} | Año: {p[1]} | Calificación: {p[2]} | Género: {p[3]}")
    return True


def editar_pelicula(matriz):
    """Permite modificar todos los atributos de una película mediante su índice."""
    if not mostrar_peliculas(matriz):
        return

    try:
        opcion = int(input("\nIngrese el número de la película que desea EDITAR: "))
        indice = opcion - 1
        
        if 0 <= indice < len(matriz):
            print(f"\n--- Modificando: {matriz[indice][0]} ---")
            print("Ingrese los nuevos datos obligatorios:")
            
            matriz[indice][0] = solicitar_titulo()
            matriz[indice][1] = solicitar_anio()
            matriz[indice][2] = solicitar_calificacion()
            matriz[indice][3] = solicitar_genero()
            
            print("\n¡Película actualizada con éxito!")
        else:
            print("Error: El número seleccionado no existe en la lista.")
    except ValueError:
        print("Error: Debe ingresar un número entero.")


def eliminar_pelicula(matriz):
    """Elimina de forma permanente una película seleccionada de la matriz."""
    if not mostrar_peliculas(matriz):
        return

    try:
        opcion = int(input("\nIngrese el número de la película que desea BORRAR: "))
        indice = opcion - 1
        
        if 0 <= indice < len(matriz):
            eliminada = matriz.pop(indice)
            print(f"\n¡La película '{eliminada[0]}' fue eliminada correctamente!")
        else:
            print("Error: El número seleccionado no existe en la lista.")
    except ValueError:
        print("Error: Debe ingresar un número entero.")


def buscar_peliculas(matriz):
    """Filtra y muestra películas que cumplan con criterios específicos."""
    if not matriz:
        print("\nNo hay películas disponibles para buscar.")
        return

    print("\n--- CRITERIOS DE BÚSQUEDA ---")
    print("1. Buscar por Género")
    print("2. Buscar por Calificación Mínima")
    print("3. Contar por Umbral de Calificación Y Año Límite") # <-- Nueva opción
    print("4. Volver al menú principal")
    
    opcion_busqueda = input("Seleccione un criterio (1-4): ").strip()
    contador_resultados = 0
    
    if opcion_busqueda == "1":
        genero_buscar = input("Ingrese el género que desea buscar: ").strip().lower()
        print("\n========== RESULTADOS DE BÚSQUEDA ==========")
        for p in matriz:
            if p[3].lower() == genero_buscar:
                print(f"Título: {p[0]} | Año: {p[1]} | Calificación: {p[2]} | Género: {p[3]}")
                contador_resultados += 1
                
    elif opcion_busqueda == "2":
        try:
            nota_minima = float(input("Ingrese la calificación mínima (0.0 - 10.0): "))
            print("\n========== RESULTADOS DE BÚSQUEDA ==========")
            for p in matriz:
                if p[2] >= nota_minima:
                    print(f"Título: {p[0]} | Año: {p[1]} | Calificación: {p[2]} | Género: {p[3]}")
                    contador_resultados += 1
        except ValueError:
            print("Error: Ingrese un número válido.")
            return

    elif opcion_busqueda == "3": # <-- Lógica de la nueva opción
        try:
            umbral = float(input("Ingrese el umbral de calificación (0.0 - 10.0): "))
            anio_limite = int(input("Ingrese el año límite de lanzamiento (1888 - 2026): "))
            
            # Llamamos al nuevo módulo especializado
            total_coincidencias = contar_por_calificacion_y_anio(matriz, umbral, anio_limite)
            
            print("\n========== SALIDA DEL CONTEO ==========")
            print(f"Total de títulos con calificación >= {umbral} y año >= {anio_limite}: {total_coincidencias}")
            return # Salimos de la función ya que esta opción solo pide el conteo total
            
        except ValueError:
            print("Error: Asegúrese de ingresar números válidos para la calificación y el año.")
            return
            
    elif opcion_busqueda == "4":
        return
    else:
        print("Opción inválida.")
        return

    if contador_resultados == 0:
        print("No se encontraron películas que coincidan con tu búsqueda.")


def contar_por_calificacion_y_anio(matriz, umbral_calificacion, anio_limite):
    """
    Cuenta cuántas películas tienen una calificación mayor o igual al umbral
    Y además fueron lanzadas en un año posterior o igual al límite.
    """
    contador = 0
    for p in matriz:
        # p[2] es la Calificación, p[1] es el Año
        if p[2] >= umbral_calificacion and p[1] >= anio_limite:
            contador += 1
            
    return contador




# =====================================================================
# 3. SECCIÓN PRINCIPAL (CONTROL DE EJECUCIÓN DEL PROGRAMA)
# =====================================================================
if __name__ == "__main__":
    # Inicialización de la base de datos local (Matriz vacía)
    matrizpeliculas = []

    # Ciclo infinito controlado para mantener la interfaz activa
    while True:
        print("\n==========================================")
        print("       SISTEMA DE GESTIÓN DE CINE        ")
        print("==========================================")
        print("1. Registrar Películas")
        print("2. Mostrar Todas las Películas")
        print("3. Editar una Película")
        print("4. Eliminar una Película")
        print("5. Buscar Películas (Criterios)")
        print("6. Salir")
        print("==========================================")
        
        opcion = input("Por favor, elija una opción (1-6): ").strip()
        
        if opcion == "1":
            registrar_peliculas(matrizpeliculas)
        elif opcion == "2":
            mostrar_peliculas(matrizpeliculas)
        elif opcion == "3":
            editar_pelicula(matrizpeliculas)
        elif opcion == "4":
            eliminar_pelicula(matrizpeliculas)
        elif opcion == "5":
            buscar_peliculas(matrizpeliculas)
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema de gestión! Saliendo...")
            break
        else:
            print("\nOpción inválida. Por favor, ingrese un número del 1 al 6.")