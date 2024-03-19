def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Exemplo de uso
n = 10
print("Sequência de Fibonacci até o", n, "º termo:")
for i in range(n):
    print(fibonacci_recursivo(i))
