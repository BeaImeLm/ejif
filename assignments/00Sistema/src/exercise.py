import os
def main():
    #escribe tu código abajo de esta línea

    os.system('clear')

    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    d = float(input("Ingrese el valor de d: "))
    e = float(input("Ingrese el valor de e: "))
    f = float(input("Ingrese el valor de f: "))

    determinante = a * e - b * d

    if determinante == 0:
        print("El sistema no tiene solución...")
    else:
        x = (c * e - b * f)/determinante
        y = (a * f - c * d)/determinante

        print(f"La solución al sistema de ecuaciones es: x = {x} | y = {y} ")

if __name__=='__main__':
    main()
