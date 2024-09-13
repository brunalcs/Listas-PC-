valor = int(input())
pagamento = input()
calculo_avista = valor - (valor*0.05)
calculo_prazo = valor + (valor*0.08)
parcela = (valor + (valor*0.08))/3



if pagamento == "V":
    print(f"Valor à pagar: {calculo_avista:.0f}")
elif pagamento == "P":
    print(f"Valor à pagar: {calculo_prazo}\nParcela 1: {parcela}\nParcela 2: {parcela}\nParcela 3: {parcela}")