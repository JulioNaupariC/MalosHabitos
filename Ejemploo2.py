def calcular_multiplicacion_y_suma(factor1, factor2, suma_adicional):

    return factor1 * factor2 + suma_adicional

def obtener_entrada(mensaje):

    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

def principal():

    print("Por favor, ingrese los siguientes valores:")
    factor1 = obtener_entrada("Ingrese el primer número (factor1): ")
    factor2 = obtener_entrada("Ingrese el segundo número (factor2): ")
    suma_adicional = obtener_entrada("Ingrese el valor adicional a sumar: ")

    resultado = calcular_multiplicacion_y_suma(factor1, factor2, suma_adicional)
    print(f"El resultado de ({factor1} * {factor2}) + {suma_adicional} es: {resultado}")

if __name__ == "__main__":
    principal()")