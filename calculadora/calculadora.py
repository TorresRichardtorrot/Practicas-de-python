def calculadora(n1,n2,operacion):
    r = f"{n1} {operacion} {n2}"
    return eval(r)

n1 = input("Igrese el numero 1: ")
n2 = input("Igrese el numero 2: ")
operacion = input("igrese que tipo de operacion a realizar:")

print("El resultado es:", calculadora(n1,n2,operacion))