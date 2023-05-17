# criar um algoritmo que receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS no voo e a QUANTIDADE DE VIAJANTES
# que moram em uma mesma casa e calcule os descontos
#O programa deverá exibir o
# valor BRUTO DA VIAGEM (o mesmo que foi digitado)
# VALOR DO DESCONTO
# VALOR LÍQUIDO DA VIAGEM (valor bruto menos os descontos)
# VALOR MÉDIO POR VIAJANTE.

# Econômica
# 2 viajantes 3% -- 0.03
# 3 viajantes 4%  -- 0.04
# 4 viajantes ou mais 5% -- 0.05

# Executiva
# 2 viajantes 5% -- 0.05
# 3 viajantes 7% -- 0.07
# 4 viajantes ou mais 0.08%

# Primeira classe
# 2 viajantes 10% -- 0.9
# 3 viajantes 15% -- 0.85
# 4 viajantes ou mais 20% -- 0.8

print( "Digite seus dados para saber o desconto da viagem")

valor = float(input("Digite o valor bruto das passagens: "))
print( "Categorias: Economica, Executiva ou Primeira classe")
categoria = (input("Digite a categoria do seu assento: "))
print( "Quantidade de viajantes em sua residência")
viajantes = int(input("Digite a quantidade de viajantes: "))
valor_novo = float
desconto = float
pp_viajante = float


if categoria.upper() == 'ECONOMICA':
    if viajantes == 2:
        valor_novo = float(valor) * 0.03
        desconto = float((valor_novo) - (valor) )* -1
        pp_viajante = float(desconto) / (viajantes)
    elif viajantes == 3:
        valor_novo = float(valor) * 0.04
        desconto = float((valor_novo) - (valor))* -1
        pp_viajante = float(desconto) / (viajantes)
    elif viajantes >= 4:
        valor_novo = float(valor) * 0.05
        desconto = float((valor_novo) - (valor))* -1
        pp_viajante = float(desconto) / (viajantes)
elif categoria.upper() == 'EXECUTIVA':
    if viajantes == 2:
        valor_novo = float(valor) * 0.05
        desconto = float((valor_novo) - (valor)) * -1
        pp_viajante = float(desconto) / (viajantes)
    elif viajantes == 3:
        valor_novo = float(valor) * 0.07
        desconto = float((valor_novo) - (valor)) * -1
        pp_viajante = float(desconto) / (viajantes)
    elif viajantes >= 4:
        valor_novo = float(valor) * 0.08
        desconto = float((valor_novo) - (valor)) * -1
        pp_viajante = float(desconto) / (viajantes)
elif categoria.upper() == 'PRIMEIRA CLASSE':
    if viajantes == 2:
        valor_novo = float(valor) * 0.09
        desconto = float((valor_novo) - (valor)) * -1
        pp_viajante = float(desconto) / (viajantes)
    elif viajantes == 3:
        valor_novo = float(valor) * 0.085
        desconto = float((valor_novo) - (valor)) * -1
        pp_viajante = float(desconto) / (viajantes)
    elif viajantes >= 4:
        valor_novo = float (valor) * 0.08
        desconto = float((valor_novo) - (valor)) * -1
        pp_viajante = float(desconto) / (viajantes)

print("Valor da viagem: {:.2f}".format(valor))
print("valor do desconto: {:.2f}".format(valor_novo))
print("valor liquido: {:.2f}".format(desconto))
print("Cada pessoa vai pagar:{:.2f}".format(pp_viajante))
