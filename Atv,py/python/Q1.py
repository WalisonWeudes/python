op = int(input("1-circulo\n2-Quadrado\n3-Trialgulo\n4-sair\n:"))

while op != 4:
    if op == 1:
        n1 =float(input("Informe o raio do circulo: "))
        a = 3.14 * (n1 * n1)
        print(f"A area desse circulo é {a}")
    elif op == 2:
        n1 = float(input("Informe o valor de um dos lados do quadrado: "))
        a = (n1 * n1)
        print(f"A area desse Quadrado é {a}")
    elif op == 3:
        b = float(input("Informe o valor da base:"))
        h = float(input("Informe o valor da altura:"))
        a = (b * h) / 2

        print(f"A area do triangulo é  {a}")


    op = int(input("1-circulo\n2-Quadrado\n3-Trialgulo\n4-sair\n:"))
    continue