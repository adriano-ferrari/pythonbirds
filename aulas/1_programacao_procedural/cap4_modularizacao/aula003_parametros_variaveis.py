# PyDev console: starting.
# Python 3.7.7 (default, Mar 19 2020, 23:39:50)
# [GCC 8.3.0] on linux
# def soma(*parcelas):
# ...     print(parcelas)
# ...     print(type(parcelas))
# ...
# soma()
# ()
# <class 'tuple'>
# soma(1)
# (1,)
# <class 'tuple'>
# soma(1,2)
# (1, 2)
# <class 'tuple'>
# def soma(*parcelas):
# ...     aux = 0
# ...     for valor in parcelas:
# ...         aux += valor
# ...     return aux
# ...
# soma()
# 0
# soma(2)
# 2
# soma(2,4)
# 6
# soma(2,4,10)
# 16
# def f(**kwargs):
# ...     print(kwargs)
# ...     print(type(kwargs))
# ...
# f()
# {}
# <class 'dict'>
# f(1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: f() takes 0 positional arguments but 1 was given
# f(nome='Adriano')
# {'nome': 'Adriano'}
# <class 'dict'>
# f(nome='Adriano', sobrenome='Ferrari')
# {'nome': 'Adriano', 'sobrenome': 'Ferrari'}
# <class 'dict'>
# args=(1,2,3)
# kwargs={'nome':'Adriano', 'sobrenome':'Ferrari'}
# def f(*args, **kwargs):
# ...     print(args)
# ...     print(kwargs)
# ...
# f()
# ()
# {}
# f(1,2, nome='Adriano', sobrenome='Ferrari')
# (1, 2)
# {'nome': 'Adriano', 'sobrenome': 'Ferrari'}
# f(args, kwargs)
# ((1, 2, 3), {'nome': 'Adriano', 'sobrenome': 'Ferrari'})
# {}
# f(*args)
# (1, 2, 3)
# {}
# f(**kwargs)
# ()
# {'nome': 'Adriano', 'sobrenome': 'Ferrari'}
# f(*args, **kwargs)
# (1, 2, 3)
# {'nome': 'Adriano', 'sobrenome': 'Ferrari'}
