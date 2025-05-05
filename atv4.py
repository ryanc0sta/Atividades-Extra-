"""

 Exercícios com funções

 Crie uma função que multiplica todos os argumentos
 não nomeados recebidos
 Retorne o total para uma variável e mostre o valor
 da variável.

"""

def soma(*args):
    resultado = 1
    for numeros in args:
        resultado *= numeros
    
    return resultado


total = soma(3, 3, 5, 10)
print(total)

"""
 Crie uma função fala se um número é par ou ímpar.
 Retorne se o número é par ou ímpar.
 """

def numero(x):
    if x % 2 == 0:

        return f'Número {x} é par'
    
    return f'Número {x} é ímpar'

resposta = numero(15)
print(resposta)


