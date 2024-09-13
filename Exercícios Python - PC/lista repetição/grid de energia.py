matriz_3x3 = []
num = int(input())
# Criando as linhas da matriz
for i in range(num):
  linha = []

  # Criando os elementos de cada linha
  for j in range(num):
    elemento = 1
    elemento += abs(j - i) # Exemplo de lógica para gerar valores
    linha.append(elemento)

  # Adicionando a linha à matriz
  matriz_3x3.append(linha)
# Imprimindo a matriz 3x3
for linha in matriz_3x3:
  print(linha)