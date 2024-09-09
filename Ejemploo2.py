class Calculadora:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular(self):
        return self.a * self.b + self.c

class Aplicacion:
    def __init__(self):
        # Se inicializan con valores por defecto que pueden ser reemplazados por el usuario
        self.a = 0
        self.b = 0
        self.c = 0
        self.calculadora = None

    def obtener_datos(self):
        # Solicita al usuario los valores para a, b y c
        self.a = float(input("Ingrese el valor de a: "))
        self.b = float(input("Ingrese el valor de b: "))
        self.c = float(input("Ingrese el valor de c: "))

        # Crea una instancia de Calculadora con los valores ingresados
        self.calculadora = Calculadora(self.a, self.b, self.c)

    def ejecutar(self):
        if self.calculadora:
            resultado = self.calculadora.calcular()
            print("El resultado es:", resultado)
        else:
            print("Debe ingresar los datos primero.")

if __name__ == "__main__":
    app = Aplicacion()
    app.obtener_datos()
    app.ejecutar()