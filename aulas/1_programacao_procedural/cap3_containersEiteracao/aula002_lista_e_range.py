# PyDev console: starting.
# Python 3.7.3 (default, Apr 22 2020, 13:29:22)
# [GCC 8.3.0] on linux
# [1,2,3]
# [1, 2, 3]
# type([])
# <class 'list'>
# lista = list(range(10))
# lista
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista = list(range(1,10))
# lista
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista = list(range(1,10,2))
# lista
# [1, 3, 5, 7, 9]
# lista = list(range(10,0,-2))
# lista = list(range(10,0,-2))
# lista
# [10, 8, 6, 4, 2]
# dir(lista)
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# lista.sort()
# lista
# [2, 4, 6, 8, 10]
# lista.append(12)
# lista
# [2, 4, 6, 8, 10, 12]
# lista.pop()
# 12
# lista
# [2, 4, 6, 8, 10]
# lista.extend(12,14)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: extend() takes exactly one argument (2 given)
# lista.extend([12,14])
# lista
# [2, 4, 6, 8, 10, 12, 14]
# lista+[16,18]
# [2, 4, 6, 8, 10, 12, 14, 16, 18]
# lista
# [2, 4, 6, 8, 10, 12, 14]
# [1,3]*3
# [1, 3, 1, 3, 1, 3]
# 'Python Pro'.split()
# ['Python', 'Pro']
# 'Python-Pro'.split('-')
# ['Python', 'Pro']
# lista = _
# lista
# ['Python', 'Pro']
# '#'.join(lista)
# 'Python#Pro'
# [1,1.0,'Adriano', []]
# [1, 1.0, 'Adriano', []]