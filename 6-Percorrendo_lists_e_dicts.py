# coding:utf-8

import timeit

''' 6-Percorrendo_lists_e_dicts '''

''' Lists '''

print '==== LISTS ===='

my_list = [2, 4, 8, 16, 32, 64]

for my_iterator in my_list:
    print my_iterator  # 2 4 8 16 32 64
print '\n'

for my_iterator in reversed(my_list):  # backwards
    print my_iterator  # 64 32 16 8 4 2
print '\n\n'

''' Obs:
    Como dito anteriormente, strings também são acessadas via índice.
    Sendo assim, podemos fazer coisas do tipo:'''

print '==== STRINGS ===='

my_string = 'globo.com'

for my_iterator in my_string:
    print my_iterator  # globo.com
print '\n'

for my_iterator in reversed(my_string):  # backwards
    print my_iterator  # moc.obolg
print '\n\n'


''' Dicts '''

print '==== DICTS ===='

my_dict = dados = {"nome": "Raphael", "sobrenome": "Brasil", "idade": 22}

''' Iterar sobre as chaves do dict '''
for my_iterator in my_dict:
    print my_iterator  # nome, sobrenome, idade
print '\n'

for my_iterator in my_dict.iterkeys():
    print my_iterator  # nome, sobrenome, idade
print '\n'

''' Iterar sobre os valores do dict '''
for my_iterator in my_dict.itervalues():
    print my_iterator  # Raphael, Brasil, 22
print '\n'

for my_iterator in my_dict:
    print my_dict[my_iterator]  # Raphael, Brasil, 22
print '\n'

''' Iterar sobre o par(chave e valor) do dict '''
for key, value in my_dict.iteritems():
    print key, value  # nome Raphael, sobrenome Brasil, idade 22
print '\n'

for key, value in sorted(my_dict.iteritems()):  # ordenado alfabeticamente
    print key, value  # idade 22, nome Raphael, sobrenome Brasil,
print '\n\n'

''' Por que .iterkeys(), .itervalues() e .iteritems()?

    The commands dict.items(), dict.keys() and dict.values() return a copy of
    the dictionary's list of (k, v) pair, keys and values. This could take a
    lot of memory if the copied list is very large.

    The commands dict.iteritems(), dict.iterkeys() and dict.itervalues()
    return an iterator over the dictionary’s (k, v) pair, keys and values. '''

''' range '''

print '==== RANGE ===='

for i in range(0, 5):
    print i  # 0 1 2 3 4
print '\n'

''' xrange '''

print '==== XRANGE ===='

for i in xrange(0, 5):
    print i  # 0 1 2 3 4
print '\n'

''' Qual a diferença então entre range e xrange? '''

print '10 Loops usando RANGE de 1 a 1000000. Media de execução: %s us' % timeit.timeit(
    'for i in range(1000000):' ' pass', number=100
)

print '10 Loops usando XRANGE de 1 a 1000000. Media de execução: %s us' % timeit.timeit(
    'for i in xrange(1000000):' ' pass', number=100
)

''' In python 2.x range() returns a list and xrange() returns an xrange object,
    which is kind of like an iterator and generates the numbers on demand.
    (Lazy Evaluation) '''
