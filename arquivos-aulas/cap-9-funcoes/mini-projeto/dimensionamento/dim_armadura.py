import numpy as np

'''
Dados de entrada da seção
bw -> largura da viga
h -> altura da viga
c -> classe de agressividade -> 2 cm = 0.002 m
d -> altura útil = h - c
'''

'''
Dados de entrada dos materiais
# concreto
fck -> resistência à compressao do concreto
gammac -> resistencia de calculo = fck / gamac

# aco
fky -> resistencia do aço
gammas -> coef. pond. do aco
fyd -> resist. do aco de cal
'''

'''
Dados de entrada da carga
mk -> momento atuante
gammad -> coef. de carga
md -> mk * gammad
'''

# dados de entrada da seção
bw = 0.12  # m
h = 0.31  # m
c = 0.02  # m
d = h - c  # m


# dados doconcreto e do aço
# dados do concreto
fck = 20  # MPa
gammac = 1.4
fcd = (fck / gammac) * 1000

# dados do aço
fyk = 50  # kN/cm²
gammas = 1.15
fyd = fyk / gammas

# momento atuante
mk = 12.2  # kNm
gammad = 1.4
md = mk * gammad

# começando de fato o dimensionamento

# cálculo da linha neutra

# criando variáveis auxiliares para ajudar no calculo da linha neutra
A = 0.68 * d
B = 1.088 * (md / (bw * fcd))
x_pos = (A + np.sqrt(A ** 2 - B))/0.544
x_neg = (A - np.sqrt(A ** 2 - B))/0.544

print(x_pos, x_neg)

# vericação da linha neutra
if x_pos < 0.259 * d or 0.259 <= x_pos <= 0.45 * d:
    print('Xpos foi escolhido!')
    x_esc = x_pos
    fs = fyd

if x_neg < 0.259 * d or 0.259 <= x_neg <= 0.45 * d:
    print('Xneg foi escolhido!')
    x_esc = x_neg
    fs = fyd

# calculo da armadura
z = d - 0.4 * x_esc

armadura_longitudinal = md / (z * fs)
print(armadura_longitudinal)

