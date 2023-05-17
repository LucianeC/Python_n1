#Crianças aprendam a controlar os seus gastos.
#Como forma de validar um protótipo, foi solicitado que você crie um script simples:
# O Usuário deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia
# Na sequência, deve informar o VALOR DE CADA UMA das transações que realizou.
# Seu programa deverá exibir, ao final, o valor total gasto pelo usuário, bem como a média do valor de cada transação.

qntd_transacoes = int(input ('Quantas transações financeiras realizou ao longo do dia: '))
total_gasto = 0

for valor in range (1, qntd_transacoes +1, 1):
    transacao = float (input(f'Informe o valor de cada transação {valor} - R$: '))
    total_gasto = total_gasto + transacao

calcular_media = total_gasto / qntd_transacoes
print(f'O valor total gasto foi de R${total_gasto:.2f}, com uma média de R${calcular_media:.2f} por transação!')