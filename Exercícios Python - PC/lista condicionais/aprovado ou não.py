nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
calculo_media = ((nota1*2)+(nota2*3)+(nota3*4))/9

if calculo_media >= 7:
    print("Francisco está aprovado")
elif calculo_media < 3:
    print("Francisco está reprovado")
else:
    print("Francisco está em prova final")