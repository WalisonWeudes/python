def organizar(op):
    lista = []
    listaimpares = []
    listazero = []
    while op != -1:
        if op == 0:
            listazero.append(op)
        elif op % 2 == 0:
            lista.insert(0, op)
        else:
            listaimpares.append(op)
        op = int(input("Informe um valor inteiro: "))
    print(listazero)
    for i in listazero:  
        lista.append(i)   
    for a in listaimpares:
        lista.append(a)

    return lista

op = int(input("Informe um valor inteiro: "))
c = organizar(op)
print(c)
