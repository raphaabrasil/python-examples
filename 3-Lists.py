''' 3-Lists.py '''

my_list = []
my_other_list = [0, 1, 2]

''' Pegadinha '''
my_list = my_other_list
print(my_list)

my_list.append(135)

print(my_list)  # !!!
print(my_other_list)  # ???

'''
Quando copiamos uma list usando list = list 2,
estamos criando duas variaveis apontando pro mesmo
endereço em memória. Por isso, quando damos append
(ou seja lá o que for) em uma das listas, consequentemente
essa mudança também ocorre na outra :)

Como fazer para isso nao acontecer?
'''

my_list = []
my_other_list = [0, 1, 2]

my_list = list(my_other_list)  # !!!
print(my_list)

my_list.append(135)

print(my_list)  # !!!
print(my_other_list)  # !!!!!!
