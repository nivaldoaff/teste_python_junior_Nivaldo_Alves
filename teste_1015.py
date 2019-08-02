p1 = list()
p2 = list()

#Entrada de valores
p1.append(float(input('Digite um valores para x1')))
p1.append(float(input('Digite um valores para y1')))

p2.append(float(input('Digite um valores para x2')))
p2.append(float(input('Digite um valores para y2')))

#Formula
d = (((p2[0])-(p1[0]))**2)+(((p2[1])-(p1[1]))**2)
t = d **(1/2)

#Resultado
print(f'{t:.4f}')

