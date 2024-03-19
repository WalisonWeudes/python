op = int(input("======DIGITE======\n1-Alcool\n2-Gasolina\n"))
litros = float(input("informe a quantidade que será abastecida:"))

if op == 1:
    if (litros <= 20.00) and litros != 0.0 :
       
        desconto = litros * 0.03
        valor = (litros * 3.45) - desconto
    else:
        
        desconto = litros * 0.05
        valor = (litros * 3.45) - desconto
elif op == 2:
     if (litros <= 20.00) and litros != 0.0 :
        desconto = litros * 0.03
        valor = (litros * 4.53) - desconto
     else:
        desconto = litros * 0.03
        valor = (litros * 4.53) - desconto
print(f"VALOR = {valor:.2f}")