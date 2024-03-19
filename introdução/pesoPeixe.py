peso = float(input("informe o peso do peixe:"))

if peso > 50.0:
    excesso = peso - 50
    print(f"O peixe tem {excesso}kg a mais de acordo com o regulamento")
    multa = excesso * 4
    print(f"O valor da multa aplicada está estimada em {multa}")
else:
    print("O peixe passou na avaliação de acordo com o regulamento")