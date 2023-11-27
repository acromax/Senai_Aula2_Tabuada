# programa para retornar uma tabuada de um número fornecido pelo usuário
# aula3 Python Turma 21 - 27/11/2023

# Apresentação
print('\n\t\t\t -- Tabuada Personalizada --\n')

# Entrada
numero = int(input('Informe um número entre 0 e 10: '))

# Processamento e Saída
if 0 <= numero <= 10:
    print(f'\nA tabuada do {numero} é:\n')
    for i in range(1, 11):  # loop da tabuada
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
else:
    print('Por favor, digite um número entre 0 e 10.\n')