## Sistema de perguntas e respostas 


questionário = [
    {
        'Pergunta': 'Qual é  raíz quadrada de 16?',
        'Opções': [8, 4, 160, 2],
        'Resposta': 4
    },

    {
        'Pergunta': 'Quanto é 17 vezes 4?',
        'Opções': [68, 54, 32, 81],
        'Resposta': 68
    },
]

for pergunta in questionário:
    print('Pergunta: ', pergunta['Pergunta'])

    opções = pergunta['Opções']
    qnt_opções = len(opções)

    for i, opção in enumerate(pergunta['Opções']):
        print(f'{i}) {opção}')
    print()

    escolha = input('Digite sua resposta: ')

    acertou = False
    escolha_int = None

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None and escolha_int in opções:
        if escolha_int == pergunta['Resposta']:
            acertou = True

    if acertou:
        print('Resposta Correta!')
    else:
        print('Resposta incorreta!')

    print()