def eh_primo(n):
    primos = []

    for i in range(1, n+1):
        if n % i == 0:
            primos.append(i)

    if len(primos) == 2:
        return True
    else:
        return False


n = int(input())

if eh_primo(n) == True and eh_primo(n+2) == True:
    print('Número forma par de gêmeos')
else:
    print('Número não forma par de gêmeos')


