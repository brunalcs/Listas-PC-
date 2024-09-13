T = int(input())

for c in range (T):
    PA, PB, G1, G2 = map(float,input().split())
    PA, PB = int(PA), int(PB)
    anos = 0
    while PA <= PB:
        PA += int(PA * (G1/100))
        PB += int(PB * (G2/100))
        anos += 1
        if anos > 100:
            print("Mais de 1 século.")
            break
    if anos <= 100:
        print(f"{anos} anos.")



