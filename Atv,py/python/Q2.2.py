def fatorial(a):
    if a == 0:
        return 1
    else:
        return a * fatorial(a - 1)

n1 = int(input("informe o numero:"))

c = fatorial(n1)

print(c)