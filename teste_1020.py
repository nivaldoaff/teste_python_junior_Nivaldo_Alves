from math import floor

#Entrada de valores
i = int(input('Digite valor da idade me dias'))

#Formulas
a = i / 365
a_b = floor(a)
a_c = i % 365
m = a_c / 30
m_b = floor(m)
d = a_c % 30

#Resultado
print(f'{a_b:.0f} Anos(s)')
print(f'{m_b:.0f} Mes(s)')
print(f'{d} Dia(s)')
