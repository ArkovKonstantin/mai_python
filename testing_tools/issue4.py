from testing_tools import one_hot_encoder
import pytest


@pytest.mark.parametrize('input_data, expected', [
    (['Moscow', 'New York', 'Moscow', 'London'], [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ])])
def test_args(input_data, expected):
    res_args = one_hot_encoder.fit_transform(*input_data)
    res_list = one_hot_encoder.fit_transform(input_data)
    assert res_args == expected
    assert res_list == expected


def test_empty_arg():
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform()


def test_empty_arglist():
    res = one_hot_encoder.fit_transform([])
    assert res == []


def test_not_string_input():
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform(1)


def test_res_type():
    res = one_hot_encoder.fit_transform('Moscow', 'New York', 'Moscow')
    assert isinstance(res, list)
    assert all(isinstance(x, tuple) for x in res)
