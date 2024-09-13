maior_gasto = -1

while True:
    gastos = float(input())
    if gastos == 0:
        break
    elif gastos > maior_gasto:
        maior_gasto = gastos

if maior_gasto != -1:
    print(f"O seu maior gasto hoje foi R${maior_gasto:.2f}")
else:
    print("Você não teve gastos hoje!")


