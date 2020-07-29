"""
This metaclass can be used to create a singleton.
Example usage:
class SomeClass(metaclass=Singleton):
    ..
"""


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            print(type(super()))
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]
