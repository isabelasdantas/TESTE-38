primeiro = int(input('Escolha o primeiro número inteiro: '))
segundo = int(input('Escolha o segundo número inteiro: '))
if primeiro > segundo:
    print('O primeiro número é maior que o segundo!')
elif segundo == primeiro:
    print('Os número são iguais!')
else:
    print('O segundo número é maior que o primeiro!')