def binario(a):
    i = 0
    if a == 0:
        return 1
    else:
        while a >= 1:
            c = a % 2 
            print(c)
            a//=2

n1 = 8
binario(n1)
            
