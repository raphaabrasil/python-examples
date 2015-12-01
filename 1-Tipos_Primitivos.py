# coding:utf-8

''' 1 - Tipos Primitivos '''

my_int = 0

print ('my_int == %s e é do tipo %s' % (my_int, type(my_int).__name__))


my_float = 1.543

print ('my_float == %s e é do tipo %s' % (my_float, type(my_float).__name__))


my_long = 54L  # sufixo L indica Long!

my_other_long = (5453254532 * 4323443234)

print ('my_long == %s e é do tipo %s' % (my_long, type(my_long).__name__))
print ('my_other_long == %s e é do tipo %s' % (
    my_other_long, type(my_other_long).__name__)
)


my_bool = True
my_other_bool = my_int == my_float

print ('my_bool == %s e é do tipo %s' % (my_bool, type(my_bool).__name__))
print ('my_other_bool == %s e é do tipo %s' % (my_other_bool,
       type(my_other_bool).__name__))


''' Por ser uma linguagem dinâmica, é permitido que façamos algo do tipo: '''
my_bool = 565L
print ('\n\nmy_bool == %s e é do tipo %s' % (my_bool, type(my_bool).__name__))

my_int = 1.543
print ('my_int == %s e é do tipo %s' % (my_int, type(my_int).__name__))

my_float = True
print ('my_float == %s e é do tipo %s' % (my_float, type(my_float).__name__))

my_long = 10
print ('my_long == %s e é do tipo %s' % (my_long, type(my_long).__name__))
