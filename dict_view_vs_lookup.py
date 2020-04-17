from random import randint
from timeit import timeit

"""
came from Java-like languages to Python? 
watch out the performance hit of dictionary lookup in iterations. 
it could become wild.
"""

d = {k: randint(0, 100) for k in range(10_000)}


def using_dict_view():
    for k, v in d.items():
        result = k, v
        pass


def using_lookup():
    for k in d:
        result = k, d[k]
        pass


print(timeit('using_dict_view()', globals=globals(), number=10_000))
# my result: 4.580507065998972
print(timeit('using_lookup()', globals=globals(), number=10_000))
# my result: 6.276309504999517
