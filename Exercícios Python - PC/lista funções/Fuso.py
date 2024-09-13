def calculo_fuso(S, T, F):
    calculo = (S+T+F) % 24

    print(f"Horário de saída:{S}")
    print(f"Horário de chegada:{calculo}")


S = int(input())
T = int(input())
F = int(input())

calculo_fuso(S, T, F)