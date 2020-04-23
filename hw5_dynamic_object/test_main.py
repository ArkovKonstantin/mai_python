import json

import pytest

from hw5_dynamic_object.main import Advert


def test_list_attr():
    data = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""
    mapping = json.loads(data)
    ad = Advert(mapping)
    for s in ad.location.metro_stations:
        isinstance(s, str)


def test_class_attr():
    data = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""
    mapping = json.loads(data)
    ad = Advert(mapping)
    assert ad.class_ == "dogs"


def test_negative_price():
    data = """{
            "title": "Вельш-корги",
            "price": 1000,
            "class": "dogs",
            "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
            }
        }"""
    mapping = json.loads(data)
    ad = Advert(mapping)
    with pytest.raises(ValueError):
        ad.price = -1


def test_default_price_value():
    data = """{
        "title": "python",
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    mapping = json.loads(data)
    ad = Advert(mapping)
    assert ad.price == 0


def test_repr():
    data = """{
                "title": "Вельш-корги",
                "price": 1000,
                "class": "dogs",
                "location": {
                "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                }
            }"""
    mapping = json.loads(data)
    ad = Advert(mapping)
    assert repr(ad) == '\033[1;33;48mВельш-корги | 1000 ₽'


def test_repr_color_code():
    data = """{
                    "title": "Вельш-корги",
                    "price": 1000,
                    "class": "dogs",
                    "location": {
                    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                    }
                }"""
    mapping = json.loads(data)
    ad = Advert(mapping)
    idx = repr(ad).find(';')
    assert int(repr(ad)[idx + 1:idx + 3]) == ad.repr_color_code
