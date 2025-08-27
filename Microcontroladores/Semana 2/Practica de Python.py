# listaNumeros = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
# [print(z, end='-') for z in listaNumeros]
# print()
# for x in listaNumeros:
#     print(x, end='-')
#     for i in range(len(listaNumeros)):
#         print(i)

mitupla = tuple(("tijeras", "papel", "piedra", "regla", "lápiz", "borrador"))
print(mitupla)
print(len(mitupla))
print(type(mitupla))
print(mitupla[1:3])
print(mitupla[-2])

if "tijeras" in mitupla:
    print("tijeras está en la tupla")
else:
    print("tijeras no está en la tupla")