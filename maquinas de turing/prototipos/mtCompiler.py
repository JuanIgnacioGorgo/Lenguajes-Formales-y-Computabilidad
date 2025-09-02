import os
import time

# leerMaquina lee el archivo con la mt y retorna su funcion de transicion y su alfabeto

def leerMaquina(filename):
    with open(filename, "r") as f:
        simbolos = f.readline().strip().split()

        matriz = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            fila = eval("[" + line + "]")
            matriz.append(fila)

    return simbolos, matriz

# transicion : [ elemento a leer ] x [ numero de estado ] -> [ elemento a escribir] x [ movimiento del selector ] x [ numero del nuevo estado ]
# la transicion necesita recibir el alfabeto, en ella se encuentra la tabla con todas las combinaciones posibles

def transicion(read, state, sigma):
    return out[sigma.index(read)][state - 1]

# eliminarExtremos : la funcion elimina los bordes vacios de la lista

def eliminarExtremos(input):
    while input[0] == "#":
        input = input[1:]

    while input[len(input) - 1] == "#":
        input = input[:len(input) - 1]

    return input

def main():
    chain = input("Ingrese la cadena: ")
    entry = list(chain)

    if set(sigma) | set(entry) != set(sigma):                           # se valida si la entrada no posee elementos por fuera del alfabeto
        print("la cinta ingresada posee elementos que no se encuentran en el alfabeto")
        return

    index = 0

    cont = 0
    state = 1

    while state != 0:                                                   # funcionamiento principal, se corta al llegar al estado final, es decir, cuando state = 0
        cont += 1

        os.system("cls")

        print(f"[{cont}] s{state}", end = "\n\t")

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
            if index == len(entry):
                entry = entry + ["#"]
        elif move == "i":
            index -= 1
            if index == -1:
                entry = ["#"] + entry
                index = 0

        time.sleep(0.25)

    print(chain, end = " -> ")                                          # impresion de la entrada y de la salida
    
    entry = eliminarExtremos(entry)

    for i in entry: print(i, end ="")

if __name__ == "__main__":
    filename = input("Ingrese el nombre del archivo: ") + ".txt"
    sigma, out = leerMaquina(filename)
    main()