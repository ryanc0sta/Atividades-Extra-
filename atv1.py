palavra_secreta = 'Paralelepípedo'
tentativas = 0
letras_acertadas = ''

while True:
    letra_escolhida = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_escolhida) > 1:
        print('Digite apenas uma letra.')
        continue 

    if letra_escolhida in palavra_secreta:
        letras_acertadas += letra_escolhida

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
     break

print(f'O número de tentativas foi {tentativas}')