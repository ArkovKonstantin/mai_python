import pytest
from func.functions import *


@pytest.mark.parametrize("test_input,expected", [
    ([1, 2, 3], 3),
    ([], 0),
    ({1: 1, 2: 2}, 2)
])
def test_ilen(test_input, expected):
    assert ilen(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ([0, [1, [2, 3]]], [0, 1, 2, 3]),
    ([1, 2, [3, [4, []]]], [1, 2, 3, 4]),
    ((1, 2, 3), [1, 2, 3])
])
def test_flatten(test_input, expected):
    assert list(flatten(test_input)) == expected


@pytest.mark.parametrize('test_input, expected', [
    (['abc', 'ab', 'abc'], ['abc', 'ab']),
    ([1, 2, 3, 1, 2], [1, 2, 3]),
    ([], [])
])
def test_distinct(test_input, expected):
    assert list(distinct(test_input)) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([
         {'color': 'red', 'clothing': 'jeans'},
         {'color': 'blue', 'clothing': 'jeans'},
         {'color': 'red', 'clothing': 'shirt'},
     ],
     {
         'red': [{'color': 'red', 'clothing': 'jeans'}, {'color': 'red', 'clothing': 'shirt'}, ],
         'blue': [{'color': 'blue', 'clothing': 'jeans'}, ]
     }),
])
def test_groupby(test_input, expected):
    assert groupby('color', test_input) == expected


@pytest.mark.parametrize('length, test_input, expected', [
    (5, [1, 2, 3, ], [(1, 2, 3), ]),
    (2, [1, 2, 3, ], [(1, 2), (3,)]),
    (0, [1, 2, 3, ], [(1, 2, 3), ]),
    (1, [1, 2, 3], [(1,), (2,), (3,)]),
])
def test_chunks(length, test_input, expected):
    assert list(chunks(length, test_input)) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([], None),
    ([1, 2, 3], 1)
])
def test_first(test_input, expected):
    assert first(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([], None),
    ([1, 2, 3], 3)
])
def test_last(test_input, expected):
    assert last(test_input) == expected
