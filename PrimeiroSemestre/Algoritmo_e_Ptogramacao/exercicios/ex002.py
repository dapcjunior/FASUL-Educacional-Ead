# Exercicio da atividade 03
"""
    Escreva um trecho de código em Python que leia o salário de um
    funcionário que receberá um aumento. Leia também a porcentagem
     de aumento e dê, ao final, qual será o novo salário desse funcionário.
     Use somente números inteiros nas entradas de dados.
    Siga o seguinte algoritmo:
    1. Leia o salário do funcionário na variável “salario”
    2. Leia a porcentagem de aumento na variável “porcentagem”
    3. Calcule, em uma linha de código, o novo salário e guarde na
        variável “novoSalario”
    4. Imprima o novo salário do funcionário
"""
print('Calculo de aumento de salario')

salarioAtual = float(input('Digite seu salario: '))
novoSalario = salarioAtual + (salarioAtual * 0.15)

print(f'Seu salario com almento de 15 % é {novoSalario}')