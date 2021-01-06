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
