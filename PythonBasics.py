Divison in python
------------------
whenever there is a divison python will throw a floating number x.y
to get an integer divison we use the // operator.
to get the reminder we use the module operator %.

Formating string
-----------------
in python 3.6 we concatenate string Using f string:
str1 = 'x'
mystr = f'hello, {str1}'
in python 3.5 and below we can use:
mystr0 = 'hello, {}'
mystr = 'hello, '.format(str1)

Lists, tuples, sets and dictionaries
-------------------------------------
my_list = [x,y,z]
my_tuple = (x,y,z)
my_set = {x,y,z}
my_dictionary = {x:y,z:t,v:w}
for lists, tupels and dictionaries, you can get the first element: my_list[0]

Iterables & range
------------------
primes = [x,y,z]
for prime in primes:
    print(prime)

if x in primes:
    print(f'{x} does exist in primes')

for i in range(10):
    print(i) # will print from 0 to 9
