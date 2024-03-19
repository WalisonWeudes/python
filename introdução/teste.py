def calcular_valor_a_pagar(litros, tipo_combustivel):
    preco_alcool = 3.45
    preco_gasolina = 4.53

    if tipo_combustivel == 'A':
        if litros <= 20:
            desconto = litros * 0.03
        else:
            desconto = litros * 0.05
        valor_a_pagar = (litros * preco_alcool) - desconto
    elif tipo_combustivel == 'G':
        if litros <= 20:
            desconto = litros * 0.04
        else:
            desconto = litros * 0.06
        valor_a_pagar = (litros * preco_gasolina) - desconto
    else:
        print("Tipo de combustível inválido!")
        return

    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")

# Example usage:
litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool e G para gasolina): ")

calcular_valor_a_pagar(litros_vendidos, tipo_combustivel)