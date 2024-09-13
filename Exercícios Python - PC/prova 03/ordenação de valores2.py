lista = []

for c in range(3):
    entrada = int(input())
    lista.append(entrada)
nova_lista = lista.copy()
nova_lista.sort()


for i in nova_lista:
    print(i)

print()

for j in lista:
    print(j)


