# Length units

from converter.unit import Unit

class Length(Unit):

    def __init__(self, value, meter=1.0, yard=1.0, mile=1.0, foot=1.0, inch=1.0, light_year=1.0):
        super(Length, self).__init__(value)
        self.__value_convert_to_meter = meter
        self.__value_convert_to_yard = yard
        self.__value_convert_to_mile = mile
        self.__value_convert_to_foot = foot
        self.__value_convert_to_inch = inch
        self.__value_convert_to_light_year = light_year

    def to_meter(self):
        return self.value*self.__value_convert_to_meter

    def to_yard(self):
        return self.value*self.__value_convert_to_yard

    def to_mile(self):
        return self.value*self.__value_convert_to_mile

    def to_foot(self):
        return self.value*self.__value_convert_to_foot

    def to_inch(self):
        return self.value*self.__value_convert_to_inch

    def to_light_year(self):
        return self.value*self.__value_convert_to_light_year

class Meter(Length):

    def __init__(self, value):
        super(Meter, self).__init__(value, 1.0, 1.0936132983, 0.0006213712, 3.280839895, 39.37007874, 1.057008707E-16)


class Yard(Length):
    
    def __init__(self, value):
        super(Yard, self).__init__(value, 0.9144, 1.0, 0.0005681797, 3.0, 36.0, 9.665287622E-17)


class Mile(Length):

    def __init__(self, value):
        super(Mile, self).__init__(value, 1609.35, 1760.0065617, 1.0, 5280.019685, 63360.23622, 1.701096963E-13)
        
class Foot(Length):
    # meter = 1.0, yard = 1.0, mile = 1.0, foot = 1.0, inch = 1.0, light_year = 1.0
    def __init__(self, value):
        super(Foot, self).__init__(value, 0.3048, 0.3333333333, 0.0001893932, 1.0, 12.0, 3.22176254E-17)

class Inch(Length):
    # meter = 1.0, yard = 1.0, mile = 1.0, foot = 1.0, inch = 1.0, light_year = 1.0
    def __init__(self, value):
        super(Inch, self).__init__(value, 0.0254, 0.0277777778, 0.0000157828, 0.0833333333, 1.0, 2.684802117E-18)

class LightYear(Length):
    # meter = 1.0, yard = 1.0, mile = 1.0, foot = 1.0, inch = 1.0, light_year = 1.0
    def __init__(self, value):
        super(LightYear, self).__init__(value, 9460660000000000.0, 10346303587051618.0, 5878559666946.0,
                                        31038910761154856.0, 372466929133858300.0, 1.0)


if __name__ == '__main__':
    print(Meter(23).to_light_year())
    # print(Meter(23).to_yard())
    # print(Meter(24).value_convert_to_mile)