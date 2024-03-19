def potencia(a,b):
    temp = 1
    while b != 0:
        temp = temp * a
        b = b - 1

    print(temp)

n1 = int(input("informe o valor da base: "))
n2 = int(input("informe o valor do expoente: "))
potencia(n1,n2)




