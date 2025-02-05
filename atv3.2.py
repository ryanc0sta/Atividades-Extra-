"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""


while True:
  cpf = input('Insira um cpf: ').replace('.', '') \
  .replace('-', '')

  if cpf == cpf[0] * len(cpf):
    print('Digite um cpf válido.')
    continue

  else:

    try:
      int(cpf)
    except ValueError:
      print('O cpf deve conter apenas números inteiros.')
      continue

    soma_resultados = 0
    i = 10

    for numero in cpf[:9]:
      soma_resultados += int(numero) * i
      i -= 1
    
    verif = (soma_resultados * 10) 
    resto = verif % 11

    if resto > 9:
      resultado = 0

    else:
      resultado = resto
    
    print(f'O primeiro dígito é {resultado}')

    soma_resultados_2 = 0
    i_2 = 11

    for numero in cpf[:9]:
      soma_resultados_2 += int(numero) * 1
      i_2 -= 1

    soma_resultados_2 += resultado * i

    verif_2 = (soma_resultados_2 * 10)
    resto_2 = verif_2 % 11

    if resto_2 > 9:
      resultado_2 = 0

    else:
      resultado_2 = resto_2

    print(f'O segundo dígio é {resultado_2}')
    break