def primo(a,b):
    list = []
    while a <= b:
        if a == 2 or a == 3 or a == 5:
            list.append(a)
            a+=1
        else:
            if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
                a+=1
            else:
                list.append(a)
                a+=1
    return list

n1= int(input("numero inicial: "))
n2= int(input("numero final: "))

c = primo(n1,n2)
if c != []:
    print(f"Os numeros {c} são primos no intervalo de {n1} a {n2} ")
else:
    print("não a numeros primos")