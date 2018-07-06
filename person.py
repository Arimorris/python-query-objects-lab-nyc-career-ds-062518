# import your Query class here
from query import Query

class Person:

    _all = []

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Person._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @classmethod
    def count(cls):
        return Query.count(cls)

    @classmethod
    def find_by_name(cls, name):
        return Query.find_by_name(cls, name)

    @classmethod
    def name_starts_with(cls, letter):
        return Query.name_starts_with(cls, letter)

    @classmethod
    def is_older_than(cls, num):
        return Query.is_older_than(cls, num)

    @classmethod
    def mean_age(cls):
        return Query.mean_age(cls)
