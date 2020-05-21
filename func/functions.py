# Домашка 

"""
- делать все на функциях
- должно работать со всеми Iterable: списки, генераторы, проч.
- по возможности возвращать генератор (ленивый объект)
- тесты на pytest + pytest-doctest, покрыть как можно больше кейсов
- в помощь: itertools, collections, funcy, google
"""

from typing import Iterable
from collections import defaultdict


## 1. Написать функцию получения размера генератора

def ilen(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    tmp = iterable
    return len(list(tmp))


## 2. Написать функцию flatten, которая из многоуровневого массива сделает одноуровневый
def flatten(iterable: Iterable):
    """
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """
    for i in iterable:
        if isinstance(i, Iterable):
            yield from flatten(i)
        else:
            yield i


## 3. Написать функцию, которая удалит дубликаты, сохранив порядок
def distinct(iterable: Iterable):
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    unique = set()
    for i in iterable:
        if i not in unique:
            unique.add(i)
            yield i


## 4. Неупорядоченная последовательность из словарей, сгруппировать по ключу, на выходе словарь
def groupby(key, iterable: Iterable):
    """
    >>> users = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20}, 
        {'gender': 'female', 'age': 21},
    ]
    >>> groupby('gender', users)
    {
        'female': [
            {'gender': 'female', 'age': 23},
            {'gender': 'female', 'age': 21},
        ],
        'male': [{'gender': 'male', 'age': 20}],
    }
    # Или так:
    >>> groupby('age', users)
    """
    group = defaultdict(list)
    for d in iterable:
        group[d[key]].append(d)

    return group


## 5. Написать функцию, которая разобьет последовательность на заданные куски
def chunks(size: int, iterable: Iterable):
    """
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 2), (3, 4, )]
    """
    buf = []
    idx = 0
    for v in iterable:
        if idx >= size:
            idx = 0
            yield tuple(buf)
            buf = []
        buf.append(v)
        idx += 1
    yield tuple(buf)


# list(chunks(3, [0, 1, 2, 3, 4]))


## 6. Написать функцию получения первого элемента или None
def first(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> first(range(0))
    None
    """
    try:
        return next(iter(iterable))
    except StopIteration:
        return None


## 7. Написать функцию получения последнего элемента или None
def last(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> last(range(0))
    None
    """
    return list(iterable).pop()


if __name__ == '__main__':
    print(first([]))
