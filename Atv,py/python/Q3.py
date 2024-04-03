def fatorial(a):
    if a == 0 or a == 1 :
        return 1
    else:
        return a * fatorial(a - 1)


op = int(input("MENU\n1-Arranjo\n2-combinação\n:"))

if op == 1:
    n = float(input("informe o valor de N: "))
    p = float(input("informe o valor de P: "))

    a = fatorial(n)/fatorial(n-p)
    print(a)
elif op == 2:
    n = float(input("informe o valor de N: "))
    r = float(input("informe o valor de R: "))

    c = fatorial(n)/(fatorial(r) * fatorial(n - r))

    print(c)




