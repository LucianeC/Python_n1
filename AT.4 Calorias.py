# Algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu naquele dia
# Depois possa informar o número de calorias de cada um dos alimentos.
# Armazenar todas as calorias digitadas
# Deve exibir o total de calorias no final.

#O usuário informara a quantidade de alimentos que consumiu no dia
qntd_alimentos = int(input('Quantos alimetos você consumiu hoje: '))

total_caloria = 0

# Função que armazena a quantidade de alimento e pedindo a caloria de cada alimento
for alimetos in range(1, qntd_alimentos +1, 1):
    calorias = int(input('Quantas calorias cada {} tem: '.format(alimetos)))

# Soma as quantidades de caloria
    total_caloria = total_caloria + calorias

#Exibe a quantidade total de caloria durante o dia
print('Hoje você consumiu no total {} calorias ao longo do dia'.format(total_caloria))