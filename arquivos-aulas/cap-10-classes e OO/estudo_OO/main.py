from inic_OO.Polinomios import Pol1, Pol2


eq1 = Pol1(3, 2)
eq2 = Pol2(1, 1, -2)

print(eq2.impressao_polinomio())
print(eq2.delta())
print(eq2.fx(3))
print(eq2.plot(-5, 5))