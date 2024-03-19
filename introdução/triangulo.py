A = float(input("informe o valor do lado A:"))
B = float(input("informe o valor do lado B:"))
C = float(input("informe o valor do lado C:"))

if ((A < B+ C) and (B < A + C) and (C <A + B)):
    if (A == B) and (B == C):
        print("Seu triângulo é Equilátero")
    elif (A == B !=  C) or (B == C !=  A) or (C == A !=  B):
        print("Seu triângulo é Isóceles")
    elif(A != B != C):
        print("Seu triângulo é Escaleno")
else:
    print("Infelismente não é possivel forma um triâgulo com esses valores")
  