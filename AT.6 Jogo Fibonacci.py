# Uma grande empresa de jogos deseja tornar seus games mais desafiadores.
# Algoritmo que será aplicado futuramente em diversos outros games: o algoritmo da sorte de Fibonacci.
#A O lgoritmo deverá funcionar da seguinte forma:
    # o usuário deve digitar um valor numérico inteiro
    # Algoritmo deverá verificar se esse valor encontra-se na sequência de Fibonacci.
    # Caso o número esteja na sequência, o algoritmo deve exibir a mensagem “Ação bem-sucedida!”
    # Caso não esteja, deve exibir a mensagem “A ação falhou...”.
# A sequência de Fibonacci é muito simples e possui uma lógica de fácil compreensão:
    # Ela se inicia em 1 e cada novo elemento da sequência é a soma dos dois elementos anteriores.
    # Portanto: 1, 1, 2, 3, 5, 8, 13, 21, e assim por diante.
# Se o usuário digitar o número 55 o programa deverá informar que a ação foi bem-sucedida, (afinal 55 está entre os números da sequência).
# Mas, se o usuário digitar o número 6, por exemplo, a ação não será bem-sucedida, pois o número 6 não está na sequência.

print('Usando a Lógica Fibonacci!')

valor_inteiro = int(input('Digite um valor inteiro:  '))

valor_1= 1
valor_2 = 0

for valor in range (1, valor_inteiro + 1, 1):
    atual = valor_1 + valor_2
    valor_1 = valor_2
    valor_2 = atual
    if valor_inteiro == atual:
        print("Ação bem-sucedida! \n Wow, Você é um verdadeiro mestre dos números!")
        break
    elif valor_inteiro < atual:
        print("Ação falhou... Sabe mesmo o que está fazendo? ")
        break
