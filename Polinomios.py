#Primer Parcial Estructura de Datos I
#Miguel Alfonzo Macario Velasquez - 1597421

class Nodo:
    def __init__(self, numero, grado):
        self.numero = numero
        self.grado = grado
        self.siguiente = None


class Polinomio:
    def __init__(self):
        self.cabeza = None

#La funcion agregar permite agregar un numero y su grado, en su caso si la cabeza esta vacia, el numero y el grado
#agregado se vuelve la cabeza, en caso la cabeza ya tiene un valor si pasa al siguiente nodo y se agrega ahi.
    def agregar(self, numero, grado):
        nuevo_nodo = Nodo(numero, grado)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo


#La funcion mostrar permite mostrar los valores almacenados en los nodos teniendo como punto de referencia la cabeza
#permitiendonos mostrar todos los datos almacenados, y mostrados de manera en que se entienda el numero y el grado.
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.numero}x^{actual.grado}", end="")
            if actual.siguiente:
                print(" + ", end="")
            actual = actual.siguiente
        print()


#La funcion "evaluar" devuelve el resultado de la operacion, con el valor que uno desea evaluar (valor) operando
#la ecuacion seleccionada teniendo como referencia la cabeza y multiplicar el grado con el valor a evaluar
#operando todos los datos necesario.
    def evaluar(self, valor):
        resultado = 0
        actual = self.cabeza
        while actual:
            resultado += actual.numero * (valor ** actual.grado)
            actual = actual.siguiente
        print(resultado)


ecuacion1 = Polinomio()
ecuacion2 = Polinomio()

while True:
    print("-----Menú-----")
    print("1. Ingresar componentes a un polinomio")
    print("2. Adicion y sustracción")
    print("3. Evaluar polinomios")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("1. Polinomio A")
        print("2. Polinomio B")
        opcion = int(input("¿Que polinomio desea agragar elementos? "))
        if opcion == 1:
            numero = int(input("Ingrese un numero: "))
            grado = int(input("Ingrese el grado: "))
            ecuacion1.agregar(numero, grado)
            ecuacion1.mostrar()

        elif opcion == 2:
            numero = int(input("Ingrese un numero: "))
            grado = int(input("Ingrese un coeficiente: "))
            ecuacion2.agregar(numero, grado)
            ecuacion2.mostrar()

    elif opcion == 2:
        print("1. Suma")
        print("2. Resta")
        opcion = int(input("Ingrese una opcion: "))
        #No me salio :(
        print("-")

    elif opcion == 3:
        print("1. Polinomio A: "), ecuacion1.mostrar()
        print("2. Polinomio B: "), ecuacion2.mostrar()
        opcion = int(input("¿Que polinomio desea evaluar? "))
        if opcion == 1:
            valor = int(input("Ingrese el valor a Evaluar: "))
            ecuacion1.evaluar(valor)
        elif opcion == 2:
            valor = int(input("Ingrese el valor a Evaluar: "))
            ecuacion2.evaluar(valor)
        else:
            print("Opcion invalida")

    elif opcion == 4:
        break

    else:
        print("Opcion Invalida ")





