import os
import time

# transicion : [ elemento a leer ] x [ numero de estado ] -> [ elemento a escribir] x [ movimiento del selector ] x [ numero del nuevo estado ]
# la transicion necesita recibir el alfabeto, en ella se encuentra la tabla con todas las combinaciones posibles

def transicion(read, state, sigma):
    '''out = [                                                             # tabla de transición
        [("#", "n", 0), ("#", "d", 3), ("*", "i", 4), ("#", "i", 5), ("*", "d", 1)],
        [("#", "d", 2), ("*", "d", 2), ("*", "d", 3), ("*", "i", 4), ("*", "i", 5)]
    ]'''

    return out[sigma.index(read)][state - 1]

# agregarMargenes: X -> #^n X #^m
# al emplear listas para emular la cinta, es necesario agregarle posibilidades adelante y atrás para la posible escritura de nuevos elementos

def agregarMargenes(entry):
    margenIzq = 0
    margenDer = len(entry) + 1

    index = margenIzq

    for _ in range(margenIzq):
        entry = ["#"] + entry
    for _ in range(margenDer):
        entry = entry + ["#"]

    return entry, index

def main():
    chain = input("Ingrese la cadena: ")
    entry = list(chain)

    if set(sigma) | set(entry) != set(sigma):                           # se valida si la entrada no posee elementos por fuera del alfabeto
        print("la cinta ingresada posee elementos que no se encuentran en el alfabeto")
        return

    entry, index = agregarMargenes(entry)

    cont = 0
    state = 1

    while state != 0:                                                   # funcionamiento principal, se corta al llegar al estado final, es decir, cuando state = 0
        cont += 1

        os.system("cls")

        print(f"[{cont}]", end = "\n\t")

        for i in range(len(entry)):                                     # print del selector
            if i == index:
                print("|", end="")
            else:
                print("-", end="")
        print("", end = "\n\t")

        for i in entry:                                                 # print de la cinta actual
            print(i, end="")
        print("")

        write, move, state = transicion(entry[index], state, sigma)     # llamado a la funcion transicion, se actualiza además el nuevo estado

        entry[index] = write                                            # [1] escritura sobre la posicion actual

        if move == "d":                                                 # [2] movimiento del selector
            index += 1
        elif move == "i":
            index -= 1

        time.sleep(0.25)

    print(chain, end = " -> ")                                          # impresion de la entrada y de la salida
    for i in entry: print(i, end ="")

if __name__ == "__main__":
    sigma = ["#", "*"]                                                  # se emplea "#" para indicar una casilla vacía, obligatoriamente debe estar dentro del alfabeto

    out = [                                                             # tabla de transición
        [("#", "n", 0), ("#", "d", 3), ("*", "i", 4), ("#", "i", 5), ("*", "d", 1)],
        [("#", "d", 2), ("*", "d", 2), ("*", "d", 3), ("*", "i", 4), ("*", "i", 5)]
    ]
    main()