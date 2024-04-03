valorEspetaculo = 200.00
ingreco = 5.00
quantvendidos = 120
maiorlucro = 0

while ingreco >1:
    lucro = (ingreco * quantvendidos) - 200
    print(f"preço do ingreço = R${ingreco:.2f},Quatidade = {quantvendidos}, lucro = R${lucro}")
    if lucro > maiorlucro:
        ingrecosave = ingreco
        maiorlucro = lucro 
        quantsave = quantvendidos
    quantvendidos+=26
    ingreco-=0.50

print("\n")
print(f"lucro maximo = R${maiorlucro:.2f}\nPreço do ingreço = R${ingrecosave:.2f}\nQuantidade vendidos = {quantsave}")
