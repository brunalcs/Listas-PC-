N = int(input())

lista = []

for i in range(N + 1):
    lista.extend([i] * i)

total = len(lista) + 1

print(f"{total} números")

print("0", end=" ")
print(" ".join(map(str, lista)))