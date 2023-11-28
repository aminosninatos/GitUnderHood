Java
-----
Every java application has to have at least one class and at one main method per application.

Execusion procedure
-------------------
Step 1:
javac + Filename.java
Step 2:
java + Filename // execute without add .java

Access Modificators
--------------------
For class only two : public : the class is visible everywhere, defaut : class visible only in the same package.
For variables four : public : visible everywhere, private: visible only in the same class, proctected : visible
in the same package and visibile for the child classes, defaut : visible only in the same package.

Encapsulation
-------------
Encapsulation in Java is a mechanism of wrapping the data (variables) and code acting on the data (methods)
together as a single unit. In encapsulation, the variables of a class will be hidden from other classes, and
can be accessed only through the methods of their current class.

Polymorphism
------------
Polymorphism means "many forms", and it occurs when we have many classes that are related to each other by inheritance.
Inheritance lets us inherit attributes and methods from another class. Polymorphism uses those methods to perform
different tasks. This allows us to perform a single action in different ways.

Abstarct class
--------------
A class that is declared using “abstract” keyword is known as abstract class. It can have abstract methods(methods without
body) as well as concrete methods (regular methods with body).
An abstract class can not be instantiated, which means you are not allowed to create an object of it.

Interface
----------
An interface is a completely "abstract class" that is used to group related methods with empty bodies.
To access the interface methods, the interface must be "implemented" (kinda like inherited) by another
class with the implements keyword (instead of extends).
Like abstract classes, interfaces cannot be used to create objects (in the example above, it is not possible
to create an "Animal" object in the MyMainClass)

Collections
-----------
The Collection in Java is a framework that provides an architecture to store and manipulate the group of objects.
Java Collections can achieve all the operations that you perform on a data such as searching, sorting, insertion,
manipulation, and deletion.
Java Collection means a single unit of objects. Java Collection framework provides many interfaces (Set, List,
Queue, Deque) and classes (ArrayList, Vector, LinkedList, PriorityQueue, HashSet, LinkedHashSet, TreeSet).

HashMap
--------
HashMap is a Map based collection class that is used for storing Key & value pairs, it is denoted as HashMap<Key, Value>
It is not an ordered collection which means it does not return the keys and values in
the same order in which they have been inserted.It does not sort the stored keys and Values.

HashMap, LinkedHashMap and TreeMap
----------------------------------
HashMap makes absolutely no guarantees about the iteration order.
TreeMap will iterate according to the "natural ordering" of the keys.
LinkedHashMap will iterate in the order in which the entries were put into the map. 
