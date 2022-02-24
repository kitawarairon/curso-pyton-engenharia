import numpy as np
from typing import NewType

metro = NewType('Metro', float)

'''
Dados de entrada da seção
bw -> largura da viga;
h -> altura da viga;
c -> classe de agressividade ii -> 2 cm;
d = h - c # altura útil
'''

'''
Dados de entrada do concreto e do aço
fck -> resistencia à compressão do concreto
fyk -> resistencia do aço
gammac -> coeficiente do concreto = 1.4
gammas -> coeficiente do aço = 1.15
'''

'''
Dados de entrada do momento 
mk -> momento atuante na viga;
gammad = 1.4
'''
# dados da seção
bw = 0.12  # m
h = 0.31  # m
c = 0.02  # m
d = 0.29

# dados do concreto e do aço
fck = 20  # MPa
gammac = 1.4
fcd = (fck / gammac) * 1000

fyk = 50  # kN/cm²
gammas = 1.15
fyd = fyk / gammas

# dados do  momento atuante
mk = 12.2  # kN/M
gammad = 1.4
md = mk * gammad

# linha neutra

# variáveis auxiliares
a1 = 0.68 * d
a2 = 1.088 * (md / (bw * fcd))

x_pos = (a1 + np.sqrt(a1 ** 2 - a2)) / 0.544
x_neg = (a1 - np.sqrt(a1 ** 2 - a2)) / 0.544
print(x_pos, x_neg)

# verificação da linha neutra

if x_pos < 0.259 * d or 0.259 * d <= x_pos <= 0.45 * d:
    print(f'x positivo')
    x_esc = x_pos

if x_neg < 0.259 * d or 0.259 * d <= x_neg <= 0.45 * d:
    print(f'x negativo')
    x_esc = x_neg

# cálculo da armadura

armadura_longitudinal = md / ((d - 0.4 * x_esc) * fyd)

print(armadura_longitudinal)







