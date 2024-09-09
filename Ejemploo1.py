def multiplicacion(factor1, factor2):
    producto = factor1 * factor2
    return producto

if __name__ == "__main__":
    # Corrige 'imput' a 'input' y la indentación
    multiplicando = float(input("Ingrese el primer número: "))
    multiplicador = float(input("Ingrese el segundo número: "))

    # Llama a la función de multiplicación y almacena el resultado
    resultado = multiplicacion(multiplicando, multiplicador)

    # Imprime el resultado de manera formateada
    print(f"{multiplicando} * {multiplicador} = {resultado}")