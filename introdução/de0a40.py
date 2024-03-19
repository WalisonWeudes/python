i = 0
while i != 40:
    if i < 40:
        if (i % 4 == 0) or (i % 10 == 0 ) or (i == 0) :
            print("PIN")
        else:
            print(i)
        i+=1
print("FIM!!")