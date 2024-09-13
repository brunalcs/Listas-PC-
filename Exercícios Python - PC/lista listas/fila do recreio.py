n = int(input())
lista_print = []

for i in range(n):
    qtd_aluno = int(input())
    entrada = input()

    lista = [int(x) for x in entrada.split(' ')]
    lista2 = lista.copy()
    lista.sort()
    lista.reverse()

    count = 0
    for j in range(qtd_aluno):
        if lista[j] == lista2[j]:
            count = count + 1
    lista_print.append(count)

for item in lista_print:
        print(lista_print[i])