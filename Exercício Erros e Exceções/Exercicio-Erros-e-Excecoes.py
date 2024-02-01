def calcular_media(valores):
    tamanho = 0
    soma = 0
    for i, valor in enumerate(valores):
        soma += valor
        tamanho += 1
    media = soma / tamanho
    print('A média calculada para os valores {} foi de {}'.format(valores, media))

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.isdigit(): #confere se são apenas digitos
        numero = int(valor)
        valores.append(numero)
    elif valor.lower() == "ok":
        continuar = False
    else:
        print("Digite apenas números ou 'ok' para calcular")

media = calcular_media(valores)