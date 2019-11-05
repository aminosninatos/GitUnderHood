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

List comprehension
-------------------
numbers = list(range(10))
double_numbers = [n * 2 for n in numbers]
you can even construct with condition
even_numbers = [n for n in numbers if n % 2 == 0]

lambda or anonymous functions
------------------------------
functions that do not have names are called lambda
example:  lambda x,y : x + y
to use it : (lambda x,y : x + y)(10,5)
to name it : my_sum = lambda x,y : x + y

Objects in python
------------------
A way to store some date and some actions related to it.

class Student:
    def __init__(self,arg1,arg2):   # self is the empty object
        self.arg1 = x
        self.arg2 = y
    def methode1(self):   # function inside a class is called a Method
        retrun x + y

student_one = Student(x, y)

Dunder methods
---------------
Dunder or magic methods in Python are the methods having two prefix and suffix underscores
in the method name. Dunder here means “Double Under (Underscores)”
in Python all the build in functions like len() or sum() and all the construct like for
are build on objects having this special methods.


Inheritance in Python
----------------------
WorkingStudent object inherites from object Student:
class WorkingStudent(Student):
    def __init(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2)  # super() refers to parent class Student
        self.arg3 = arg3
the methode "methode1" is automatically inherites from Student class.
