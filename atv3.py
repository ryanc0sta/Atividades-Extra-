"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
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