#Os colaboradores da sua equipe foram sorteados para ganhar um console de última geração,
# cada um, em razão do bom desempenho que tiveram nos últimos projetos.
# A empresa pede que todos os cinco membros da equipe recebam o mesmo aparelho.

# Crie um algoritmo onde o usuário possa digitar o voto de cada um dos 5 membros da equipe
# e, ao final, exiba qual foi o console escolhido e
# com quantos votos.


voto1 = input("Qual console deseja ganhar: xbox, playstation ou nintendo:  ")
voto2 = input("Qual console deseja ganhar: xbox, playstation ou nintendo: ")
voto3 = input("Qual console deseja ganhar: xbox, playstation ou nintendo: ")
voto4 = input("Qual console deseja ganhar: xbox, playstation ou nintendo: ")
voto5 = input("Qual console deseja ganhar: xbox, playstation ou nintendo: ")


xbox = 0
playstation = 0
nintendo = 0

if voto1.upper() == "XBOX":
    xbox += 1
elif voto1.upper() == "PLAYSTATION":
  playstation += 1
elif voto1.upper() == "Nitendo":
    nintendo += 1

if voto2.upper() == "XBOX":
    xbox += 1
elif voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "NINTENDO":
    nintendo += 1

if voto3.upper() == "XBOX":
    xbox += 1
elif voto3.upper() == "PLAYSTATION":
    playstation += 1
elif voto3.upper() == "NINTENDO":
    nintendo += 1

if voto4.upper() == "XBOX":
    xbox += 1
elif voto4.upper() == "PLAYSTATION":
     playstation += 1
elif voto4.upper() == "NINTENDO":
     nintendo += 1

if voto5.upper() == "XBOX":
     xbox += 1
elif voto5.upper() == "PLAYSTATION":
     playstation += 1
elif voto5.upper() == "NINTENDO":
    nintendo += 1

nome_votado = ""
mais_votado: 0

if xbox > playstation and xbox > nintendo:
    nome_votado = "XBOX"
    mais_votado = xbox
elif playstation  > xbox and playstation  > nintendo:
    nome_votado = "PLAYSTATION"
    mais_votado = playstation
elif nintendo  > xbox and nintendo  > playstation:
    nome_votado = "NINTENDO"
    mais_votado = nintendo

print ("O console mais votado foi: {} com {} votos ".format(nome_votado, mais_votado))