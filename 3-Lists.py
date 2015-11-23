# coding:utf-8

''' 3-Lists.py '''

my_list = []
my_other_list = [0, 1, 2]
print(my_list)  # []
print(my_other_list)  # 0, 1, 2

my_other_list.extend([3, 4, 5])
print(my_other_list)  # 0, 1, 2, 3, 4, 5

my_other_list[3:] = []
print(my_other_list)  # 0, 1, 2

my_other_list = my_other_list + [3, 4]
print(my_other_list)  # 0, 1, 2, 3, 4

my_other_list.remove(4)  # 0, 1, 2, 3
my_other_list.pop(3)  # 0, 1, 2
print(my_other_list)

''' Pegadinha '''
my_list = my_other_list
print(my_list)  # 0, 1, 2

my_list.append(135)

print(my_list)  # 0, 1, 2, 135 (!!!)
print(my_other_list)  # 0, 1, 2, 135 (???)

'''
Quando copiamos uma list usando list = list 2,
estamos criando duas variaveis apontando pro mesmo
endereço em memória. Por isso, quando damos append
(ou seja lá o que for) em uma das listas, consequentemente
essa mudança também ocorre na outra :)

Como fazer para isso nao acontecer?
'''

''' Opção 1 '''
my_list = []
my_other_list = [0, 1, 2]

my_list = list(my_other_list)  # !!!
print(my_list)

my_list.append(135)

print(my_list)  # 0, 1, 2, 135 (!!!)
print(my_other_list)  # 0, 1, 2 (!!!!!!)

''' Opção 2 '''
my_list = []
my_other_list = [0, 1, 2]

my_list = my_other_list[:]  # !!!
print(my_list)

my_list.append(135)

print(my_list)  # 0, 1, 2, 135 (!!!)
print(my_other_list)  # 0, 1, 2 (!!!!!!)
