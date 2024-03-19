

a = input('Digite um valor')

try:
    assert isinstance(a, int)
except AssertionError:
    while True:
        try:
            a = int(input('Digite um valor: '))
            break
        except:
            print('Digite um INTEIRO')
            continue

print('Final do codigo')
print(a)

"""""
def soma(a, b = 2):
    print(a + b)
    return a + b, 'Flavio'


if __name__ == '__main__':
    c, d = soma(10, 5)
    print(c, d)
"""""