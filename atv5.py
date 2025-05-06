# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplos(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador 
    
    return multiplicar

duplicar = criar_multiplos(2)
triplicar = criar_multiplos(3)
quadruplicar = criar_multiplos(4)
