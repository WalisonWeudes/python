n1 = int(input("informe o valor: "))
while n1 > 0:
    i = n1
    temp = 1
    while i != 0:
        temp = temp * i
        i-=1
    print(temp)
    n1 = int(input("informe o valor: "))