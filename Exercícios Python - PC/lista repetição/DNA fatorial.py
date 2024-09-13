numero = int(input())
count = 1
resultado = 1

if numero > 0:
    while count <= numero:
        resultado = resultado * count
        count += 1
    print(f"Resultado do fatorial: {resultado}")
else:
    print("O número deve ser maior que 0.")
