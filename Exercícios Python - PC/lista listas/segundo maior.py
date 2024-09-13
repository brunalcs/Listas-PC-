entrada = input()
valores = list(map(float, entrada.split(',')))

maior = float('-inf')
segundo_maior = float('-inf')


if len(valores) < 2:
  print("Não é possível determinar o segundo maior valor com menos de dois elementos.")
elif valores[0] == valores[-1]:
  print("Não é possível determinar o segundo maior valor com menos de dois valores distintos.")
else:
  for numero in valores:
    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero > segundo_maior and numero != maior:
        segundo_maior = numero
  print(segundo_maior)