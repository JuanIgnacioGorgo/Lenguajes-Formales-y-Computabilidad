# pruebas ejemplos de listas

# funciones base

def oI(l):              # cero a izquierda
    return [0] + l

def oD(l):              # cero a derecha
    return l + [0]

def eI(l):              # eliminar a izquierda
    if l == []:
        return []
    
    return l[1 : len(l)]

def eD(l):              # eliminar a derecha
    if l == []:
        return []
    
    return l[0 : len(l) - 1]

def sI(l):              # sucesor izquierda
    if l == []:
        return []

    return [l[0] + 1] + l[1 : len(l)]

def sD(l):              # sucedor derecha
    if l == []:
        return []

    return l[0: len(l) - 1] + [l[len(l) - 1] + 1]

# operadores

def comp(flist):
    def f(l):
        out = l
        for func in flist:
            out = func(out)
        return out
    
    return f

def rep(func):
    def f(l):
        while l[0] != l[len(l) - 1]:
            l = func(l)
        return l

    return f

# funciones propuestas

pI = comp([oI, rep(sI), eD])                                                                # pasar a izquierda         pI: X, b -> b, X

pD = comp([oD, rep(sD), eI])                                                                # pasar a derecha           pD: a, X -> X, a

dI = comp([pD, oI, rep(sI), pI])                                                            # duplicar a izquierda      dI: a, X -> a, a, X

dD = comp([pI, oD, rep(sD), pD])                                                            # duplicar a derecha        dD: X, b -> X, b, b

iE = comp([pD, oI, pI, oI, rep(comp([sI, pD, pD, sI, pI, pI])), eD, eI, pD])                # intercambiar extremos     iE: a, X, b -> b, X, a

iP = comp([pD, iE, pI])                                                                     # intercambiar primeros     iP: a, b, X -> b, a, X

iU = comp([pI, iE, pD])                                                                     # intercambiar últimos      iU: X, a, b -> X, b, a

cI = comp([dI, pD])                                                                         # copiar izquierda          cI: a, X -> a, X, a

def proy(n):                                                                                # n-ésima proyección        proy(n): 
    def f(l):
        if n <= len(l):
            for _ in range(n - 1):
                l = pD(l)

            l = dI(l)

            for _ in range(n - 1):
                l = iE(l)
                l = pI(l)
            
        return l
    
    return f

# funciones algebraicas

suma = comp([oI, rep(comp([sI, iP, sI, iP])), eI])                                          # suma:                     a, X, b -> a + b, X, b

prod = comp([cI, eI, oI, oI, rep(comp([sI, iP, iU, suma, iU, iP])), eI, eD])                # prod:                     a, X, b -> a * b, X, b

exp  = comp([cI, eI, oI, sI, oI, iU, rep(comp([sI, iP, iU, prod, iU, iP])), iU, eI, eD])    # exp:                      a, X, b -> a ^ b, X, b

# ejercicios

e1 = comp([oI,sI,sI,sI,sI,sI,sI,sI])

e2 = comp([sI, sI, sI, sI, sI])

e3 = dI

e4 = comp([dI, dI])

e5 = comp([iE, pI])

e6 = comp([pD, dD, pI, sI, sI, dD, pI, sI, pI])

e7 = comp([pD, iE, pD, iE, pI, iE, pI])

# proyecciones                                                                               

p1 = proy(1)
p2 = proy(2)
p3 = proy(3)
p4 = proy(4)

def main():

    l1 = [2, 3]

    print(l1)
    print(suma(l1))
    print(prod(l1))
    print(exp(l1))
    print(p1(l1))

if __name__ == "__main__":
    main()