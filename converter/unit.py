# This is principal class or mother class
# import numpy as np

class Unit:

    def __init__(self, value):
        if isinstance(value, (int, float)):
            self.value = float(value)
        # elif isinstance(value, (list, tuple)):
        #     self.value = np.array(value)
        else:
            raise TypeError("Incorrect type")

    def __str__(self):
        return str(self.value)

    # def operator(self, convert_value):
        # print(type(self.value))
    #    if isinstance(self.value, np.ndarray):
    #        return list(self.value*convert_value)
    #    return self.value*convert_value


if __name__ == '__main__':
    pass
    # num = Unit((3, 4, 4, 4))
    # print(num.operator(34))


