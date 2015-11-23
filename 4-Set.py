# coding:utf-8

'''4-Set'''

''' Listas não ordenadas que não permitem elementos duplicados '''

x = set([10, 2, 1, 4, 10, 1])
print(x)  # [1, 10, 4, 2]

x.add(5)
print(x)   # [1, 10, 4, 2, 5]
print(12 in x)  # False

y = set([3, 4])

print(x | y)     # União [1, 10, 4, 2, 5, 3]
print(x & y)     # Interseção [4]
print(x - y)     # Diferença [1, 10, 2, 5]
print(x ^ y)     # Diferença simétrica [1, 10, 2, 5, 3]
