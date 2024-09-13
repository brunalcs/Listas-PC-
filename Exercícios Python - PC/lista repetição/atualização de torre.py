N = int(input())

for count in range(N):
    x, y = map(int, input().split())
    if x % 2 == 0:
        x += 1
    soma = 0
    for i in range(y):
        soma += x + 2 * i
    print(soma)



