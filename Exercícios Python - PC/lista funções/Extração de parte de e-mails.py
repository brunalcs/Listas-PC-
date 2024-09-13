def extrair_parte(emails):
    lista = []
    for e in emails:
        arroba = e.find('@')
        ponto = e.find('.', arroba)
        parte = e[arroba+1:ponto]
        lista.append(parte)
    return lista

def main():
    emails = []
    while True:
        entrada = input()
        if entrada == 'FIM':
            break
        emails.append(entrada)

    lista = extrair_parte(emails)

    for i in lista:
        print(i)

if __name__ == "__main__":
    main()