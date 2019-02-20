Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cs="a=b;c=d;e=f;g=h"
>>> cs.split(";")
['a=b', 'c=d', 'e=f', 'g=h']
>>> a=[tuple)i.split("="))for i in cs]
SyntaxError: invalid syntax
>>> a=[tuple(i.split("="))for i in cs]
>>> print("a")
a
>>> print(a)
[('a',), ('', ''), ('b',), (';',), ('c',), ('', ''), ('d',), (';',), ('e',), ('', ''), ('f',), (';',), ('g',), ('', ''), ('h',)]
>>> 
