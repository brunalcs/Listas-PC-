entrada = eval(input())


lista_plana = []


lista = [entrada]

while lista:
    armazenar_item = lista.pop()
    if isinstance(armazenar_item, list):
        lista.extend(armazenar_item)
    else:
        lista_plana.append(armazenar_item)


lista_plana.reverse()
print(lista_plana)
