import json
import keyword


class ColorizeMixin:
    repr_color_code = 33  # green

    def __repr__(self):
        return '\033' + f"[1;{self.repr_color_code};48m"


class Advert(ColorizeMixin):

    def __new__(cls, obj):
        if isinstance(obj, dict):
            return super().__new__(cls)
        elif isinstance(obj, list):
            return [cls(item) for item in obj]
        else:
            return obj

    def __init__(self, mapping: dict):
        self.__data = dict(mapping)
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                self.__data[k + '_'] = v
            if k == 'price':
                self.__dict__['__price'] = v

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        else:
            return Advert(self.__data[item])

    @property
    def price(self):
        if not self.__dict__.get('__price', None):
            return 0
        return self.__dict__['__price']

    @price.setter
    def price(self, value):
        if value > 0:
            self.__dict__['__price'] = value
        else:
            raise ValueError

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == "__main__":
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
    print(ad)
