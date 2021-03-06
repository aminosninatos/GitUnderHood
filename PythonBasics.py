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

Input function in Python
-------------------------
n = input('Please enter a number')
remember that input() function retuens a str not a number


Use cases for sets in Python
-----------------------------
we use sets in python or convert a list to set using the set() function
mostly to benifit from the intersection or union functions in sets.


Context manager in Python
--------------------------
in opening and closing files:
with open('filename','rw') as file:
    file_content = file.read()


Impoting in python
-------------------
we can use either ways:
import module
module.function()

from module import function
function()

Using sqlite with python
-------------------------
import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.excute('ur sql query')
connection.commit()
connection.close()


Get all rows in sqlite3
-----------------------
import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.excute('select sql query')
rows = cursor.fetchall()
connection.close()


Type hinting
-------------
When you define a function you can specify that it retuens nothing
def function() -> None:
     statmenets
That makes programming easy for editors to detect.


Generators in Python
--------------------
A function that remembers the state its in between executions.
we call the values using yield keyword, and we call the next value using
the next() keyword

Mutability in Python
--------------------
Mutable are object that we can change
immutable are objects that you cannot change
integers, floats, strings, tuples are immutable
list,dictionaries are mutable


Working with date & time
--------------------------
from datetime import datetime
print(datetime.now()) -> not aware of your timezone
from datetime import datetime,timezone
print(datetime.now(timezone.utc))  -> aware of timezone


Regular expressions in Python
------------------------------
"." means anything but not newlines
"+" means one or more of
"*" means zero or more of
"?" means zero or one of


Logging in Python
-----------------
import Logging
logger = logging.getlogger('test_logger')
logger.info('this will not show up')
logger.warning('this will show up')
the level of debugging are DEBUG INFO WARNING ERROR CRITICAL
we can set the level : logging.basicConfig(level=logging.DEBUG)
to go to a file : logging.basicConfig(level=logging.INFO,filename='log.txt')
to format datetime values : logging.basicConfig(level=logging.INFO,datefmt='%d-%m-%y %H:%M:%S')


HTML web scraping in Python
---------------------------
from bs4 import beautifulsoup
my_html = 'html code here'
my_bs = BeautifulSoup(my_html,'html.parser')
print(my_bs.find('html_tag').string)
we can also access our element using parent, child hirachy using CSS locator:
locator = 'parent_tag.class_name child1 child2'
to get the string of the tag :
item = my_bs.select_one(locator).string
if the item has attributes and to get the value of item attribute:
item = my_bs.select_one(locator).attrs['attribute_name']
we can use the request module to get website content:
import requests
page = requests.get('http://www.example.com')
print(page.content)
