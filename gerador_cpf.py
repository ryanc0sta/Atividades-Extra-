import random

cpf_gerado = ''

for i in range(9):
    cpf_gerado += str(random.randint(0, 9))

soma_resultados = 0
i = 10

for numero in cpf_gerado[:9]:
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

for numero in cpf_gerado[:9]:
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

cpf_gerado += str(resultado) + str(resultado_2)
print(cpf_gerado)
