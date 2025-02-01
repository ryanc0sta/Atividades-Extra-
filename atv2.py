"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []

while True:
    print('Selecione um opção') 
    opcao = input('[a]pagar  [i]nserir  l[istar] [s]air')

    if opcao.startswith('i'):
        item_adc = input('Qual item quer adicionar?')
        lista.append(item_adc)
    
    elif opcao.startswith('a'):
        del_item = input('Qual item quer deletar?')
        try:
            del lista[del_item]
        except ValueError:
            print('Esse item não existe.')
    
    elif opcao.startswith('l'):
        if len(lista) == 0:
            print('Não a nada para listar')

        else:
            for indice, item in enumerate(lista):
                print(indice, item)
    
    elif opcao.startswith('s'):
        print('Encerrando sistema.')
        break

    else:
        print('Por favor, escolha uma das opções apresentadas.')
        continue 

