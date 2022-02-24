from dimensionamento.dim_final import calculo_total


# criando um sistema iterativo
while True:
    calculo = input('Deseja calcular ? y / n\n')
    if calculo.lower() == 'n':
        break
    bw = float(input('bw (cm): '))
    h = float(input('h (cm): '))
    fck = float(input('fck (MPa): '))
    fyk = float(input('fyk (kN/cm²): '))
    mk = float(input('mk (kNm): '))
    print(f'A área da armura é {calculo_total(bw, h, fck, fyk, mk):.3f}')


