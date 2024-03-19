valorhora = float(input("informe o valor que voce ganha por hora:"))
hora = int(input("Informe a quantidade de horas trabalhadas:"))

salario = valorhora * hora
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario *0.05
salarioliquido = salario - (ir + inss + sindicato)


print(f"+Sálario bruto = {salario}")
print(f"-IR = {ir}")
print(f"-INSS = {inss}")
print(f"-Sindicato = {sindicato}")
print(f"=Sálario liquido = {salarioliquido}")