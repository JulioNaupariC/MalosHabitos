def calcular_area_rectangulo(base, altura):
    return base * altura


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura


def main():
    # Solicita al usuario los valores para el área del rectángulo
    base_rectangulo = float(input("Ingrese la base del rectángulo: "))
    altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))

    # Solicita al usuario los valores para el área del triángulo
    base_triangulo = float(input("Ingrese la base del triángulo: "))
    altura_triangulo = float(input("Ingrese la altura del triángulo: "))

    # Calcula las áreas usando las funciones
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)

    # Imprime los resultados
    print("Área del rectángulo:", area_rectangulo)
    print("Área del triángulo:", area_triangulo)


if __name__ == "__main__":
    main()