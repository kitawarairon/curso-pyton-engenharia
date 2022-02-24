""""
O que é type hint
O python é uma linguagem de tipagem dinâmica!
"""

from typing import NewType

densidade = NewType('kg/m³', float)
gravidade = NewType('m/s²', float)
altura = NewType('m', float)
pascal = NewType('Pa', float)


def pressao(rho: densidade, g: gravidade, h: altura) -> pascal:
    return rho * g * h
