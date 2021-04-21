Mutable & inmmutable
-----------------------
strings are immutable:
s = 'hello'
s.upper() will print 'HELLO'
after that s will print 'hello'

- lists are Mutables
- Sets are lists that has no duplicates & are Mutables.
- tuples are immutables.
- dictionnaries are Mutables & unordered.

Parametres & Arguments
---------------------------
Parametres are used when defining a function.
Arguments are used when calling that function.

Modules
---------
- when importing a Module all its code is executed
  to avoid the part we dont want to excute we put it inside:
  if __name__ == "__main__"

- when you import using the form :"from module import something", you dont have
  to proceed the variable or function from that module with the module name.
