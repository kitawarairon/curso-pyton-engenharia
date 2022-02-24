import numpy as np
from typing import NewType

metro = NewType('m', float)
pressao = NewType('MPa', float)
pressao_em_kn = NewType('kN/cm²', float)
momento = NewType('kNm', float)


def secao(bw, h):
    c = 2
    d = h - c
    return bw/100, d/100


def concreto(fck):
    gammac = 1.4
    return (fck * gammac) * 1000


def aco(fyk):
    gammas = 1.15
    return fyk / gammas


def momento(mk):
    gammad = 1.4
    return mk * gammad


def calculo_da_linha_neutra(bw, d, md, fcd):
    A = 0.68 * d
    B = 1.088 * (md / (bw * fcd))
    x_pos = (A + np.sqrt(A ** 2 - B)) / 0.544
    x_neg = (A - np.sqrt(A ** 2 - B)) / 0.544
    return x_pos, x_neg


def verificao_linha_neutra(d, x_pos, x_neg):
    # vericação da linha neutra
    if x_pos < 0.259 * d or 0.259 <= x_pos <= 0.45 * d:
        print('Xpos foi escolhido!')
        x_esc = x_pos
        return x_esc

    if x_neg < 0.259 * d or 0.259 <= x_neg <= 0.45 * d:
        print('Xneg foi escolhido!')
        x_esc = x_neg
        return x_neg


def calculo_armadura(d, x_esc, md, fyd):
    z = d - 0.4 * x_esc
    armadura_longitudinal = md / (z * fyd)
    return armadura_longitudinal


def calculo_total(bw: metro, h: metro, fck: pressao, fyk: pressao_em_kn, mk: momento) -> float:
    # dados de entrada do problema
    bw, d = secao(bw=bw, h=h)
    fcd = concreto(fck)
    fyd = aco(fyk)
    md = momento(mk)

    # calculo do problema
    x_pos, x_neg = calculo_da_linha_neutra(bw=bw, d=d, md=md, fcd=fcd)
    x = verificao_linha_neutra(d=d, x_pos=x_pos, x_neg=x_neg)
    return calculo_armadura(d=d, x_esc=x, md=md, fyd=fyd)





