''' 2 - Strings '''

my_string = "Ola Python"
my_unicode_string = u"Olá Python!"

print ('my_string == %s e eh do tipo %s' % (
    my_string, type(my_string).__name__)
)


''' Strings podem ser acessadas como um array (via indice) '''

print my_string[0]  # output = O
print my_string[-1]  # output = n
print my_string[0:3]  # output = Ola
print my_string[:3]  # output = Ola
''' my_string[0:3] == my_string[:3] '''
print my_string[3:]  # output =  Python
print my_string[3:-1]  # output = Pytho


''' Porem strings sao imutaveis via indice '''

my_string[1] = 'a'  # TypeError: 'str' object does not support item assignment
