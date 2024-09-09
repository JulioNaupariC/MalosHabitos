# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):

    return base * altura

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):

    return 0.5 * base * altura


base_rectangulo = 5  # Cambia este valor para el área del rectángulo
altura_rectangulo = 6  # Cambia este valor para el área del rectángulo

base_triangulo = 7  # Cambia este valor para el área del triángulo
altura_triangulo = 8  # Cambia este valor para el área del triángulo

area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)

# Mostrar resultados
print(f"Área del rectángulo con base {base_rectangulo} y altura {altura_rectangulo} es: {area_rectangulo}")
print(f"Área del triángulo con base {base_triangulo} y altura {altura_triangulo} es: {area_triangulo}")
