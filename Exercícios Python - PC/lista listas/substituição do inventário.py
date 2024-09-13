entrada = input().replace(' ', '')
entrada = entrada.strip('[]')
lista = entrada.split(',')


item_deletar = input()
item_inserir = input()

if item_deletar in lista:
    lista2 = lista.copy()
    quantidade = lista.count(item_deletar)
    while quantidade > 0:
        for i in range(len(lista2)):
            if lista[i] == item_deletar:
                lista2.pop(i)
                lista2.insert(i, item_inserir)
        quantidade = quantidade - 1
    print(lista2)
else:
    print("Item não presente no inventário.")


