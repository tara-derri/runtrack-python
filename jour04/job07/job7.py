L = [8, 24, 48, 2, 16]

nombre_multiples_de_3 = sum(1 for nombre in L if nombre % 3 == 0)

print(nombre_multiples_de_3)

