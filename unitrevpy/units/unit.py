# This is principal class or mother class
import numpy as np


class Unit:
    PREFIX = {
        'yocto': ('y', 1e-24),
        'zepto': ('z', 1e-21),
        'atto': ('a', 1e-18),
        'femto': ('f', 1e-15),
        'pico': ('p', 1e-12),
        'nano': ('n', 1e-09),
        'micro': ('μ', 1e-06),
        'milli': ('m', 0.001),
        'centi': ('c', 0.01),
        'deci': ('d', 0.1),
        'deca': ('da', 10),
        'hecto': ('h', 100),
        'kilo': ('k', 1000),
        'mega': ('M', 1000000),
        'giga': ('G', 1000000000),
        'tera': ('T', 1000000000000),
        'peta': ('P', 1000000000000000),
        'exa': ('E', 1000000000000000000),
        'zetta': ('Z', 1000000000000000000000),
        'yotta': ('Y', 1000000000000000000000000),
    }

    def __init__(self, value, prefix):
        self.value = value
        if prefix not in self.PREFIX.keys():
            raise KeyError(f'\'{prefix}\' is not in the known prefixes: {[pf for pf in self.PREFIX.keys()]}')
        self.prefix = prefix

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value}, prefix={self.PREFIX[self.prefix][0] if self.prefix else 1})'

    def __str__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if isinstance(value, (int, float)):
            self.__value = float(value)
        elif isinstance(value, (list, tuple, set)):
            self.__value = list(np.array(list(value)) * 1.0)
        else:
            raise TypeError("Incorrect type")
