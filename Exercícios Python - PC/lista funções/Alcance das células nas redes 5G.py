def get_range(n, cells, distance, user):
    indices_no_alcance = []

    for i in range(n):
        if abs(cells[i] - user) <= distance:
            indices_no_alcance.append(cells[i])

    if indices_no_alcance:
        print(' '.join(map(str, indices_no_alcance)))
    else:
        print("USUARIO DESCONECTADO")

# Leitura dos dados de entrada
n, d, u = map(int, input().split())
cells = [int(input()) for _ in range(n)]

# Chamada da função
get_range(n, cells, distance, user)
