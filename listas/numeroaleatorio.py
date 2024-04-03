import random
tamanho = int(input("informe o tamanho da lista:"))
n1 = int(input("informe o valor inicial:"))
n2 = int(input("informe o valor final:"))
lista = []
i = 0
while i< tamanho:
    x = random.randint(n1, n2)
    if x not in lista:
        lista.append(x)
        i+=1
print(lista)

            

