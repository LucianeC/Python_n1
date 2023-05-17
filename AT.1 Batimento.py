# Verificar se os batimentos cardíacos por minuto se encontram na faixa adequada.

# Para isso, você deve solicitar ao usuário que informe o seu número de BATIMENTOS POR MINUTO (BPM) e a IDADE.
# O script deve verificar e exibir uma mensagem informando se os batimentos do usuário encontram-se DENTRO da faixa adequada

# Até 2 anos 120 a 140
# De 8 anos até 17 anos 80 a 100
# Adulto sedentário 70 a 80
# Idosos 50 a 60

idade = int(input("digite sua idade: "))
btm = int(input("digite o seu batimento por minuto: "))


if idade <= 2 :
    if btm >=120 and btm <= 140:
        print("faixa adequada. Os batimentos ({} por minuto) estão de acordo com a idade ({} anos)".format(btm, idade))
    else:
        print("faixa inadequada. Os batimentos ({} por minuto) não estão de acordo com a idade ({} anos). Por favor, consulte um especialista".format(btm, idade))
elif idade >= 8 and idade <= 17:
    if btm >=80 and  idade <=100:
        print("faixa adequada. Os batimentos ({} por minuto) estão de acordo com a idade ({} anos)".format(btm, idade))
    else:
        print("faixa inadequada. Os batimentos ({} por minuto) não estão de acordo com a idade ({} anos). Por favor, consulte um especialista".format(btm, idade))
elif idade >=18  and idade <=59:
    if btm >=70 and btm <= 80:
        print("faixa adequada. Os batimentos ({} por minuto) estão de acordo com a idade ({} anos)".format(btm, idade))
    else:
        print("faixa inadequada. Os batimentos ({} por minuto) não estão de acordo com a idade ({} anos). Por favor, consulte um especialista".format(btm, idade))
elif idade >= 60 :
    if  btm <=50 and btm <= 70 :
        print("faixa adequada. Os batimentos ({} por minuto) estão de acordo com a idade ({} anos)".format(btm, idade))
    else:
        print("faixa inadequada. Os batimentos ({} por minuto) não estão de acordo com a idade ({} anos). Por favor, consulte um especialista".format(btm, idade))
else:
    print("Dados não existentes")


