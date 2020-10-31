# Length units

class Length:
    """
    units used
    meter, yard, mile, foot, inch, light_year
    """
    def __init__(self, value, *args):
        self.__value = float(value)
        self.__value_convert_to_meter = args[0]
        self.__value_convert_to_yard = args[1]
        self.__value_convert_to_mile = args[2]
        self.__value_convert_to_foot = args[3]
        self.__value_convert_to_inch = args[4]
        self.__value_convert_to_light_year = args[5]

    @classmethod
    def from_meter(cls, value):
        return cls(value, 1.0, 1.0936132983, 0.0006213712, 3.280839895, 39.37007874, 1.057008707E-16)

    @classmethod
    def from_yard(cls, value):
        return cls(value, 0.9144, 1.0, 0.0005681797, 3.0, 36.0, 9.665287622E-17)

    @classmethod
    def from_mile(cls, value):
        return cls(value, 1609.35, 1760.0065617, 1.0, 5280.019685, 63360.23622, 1.701096963E-13)

    @classmethod
    def from_foot(cls, value):
        return cls(value, 0.3048, 0.3333333333, 0.0001893932, 1.0, 12.0, 3.22176254E-17)

    @classmethod
    def from_inch(cls, value):
        return cls(value, 0.0254, 0.0277777778, 0.0000157828, 0.0833333333, 1.0, 2.684802117E-18)

    @classmethod
    def from_lightyear(cls, value):
        return cls(value, 9460660000000000.0, 10346303587051618.0, 5878559666946.0,
                   31038910761154856.0, 372466929133858300.0, 1.0)

    @property
    def value(self):
        return self.__value

    # Properties

    @property
    def to_meter(self):
        """
        This method converts the value to Meter unit
        """
        return self.__value*self.__value_convert_to_meter

    @property
    def to_yard(self):
        """
        This method converts the value to Yard unit
        """
        return self.__value*self.__value_convert_to_yard

    @property
    def to_mile(self):
        """
        This method converts the value to Mile unit
        """
        return self.__value*self.__value_convert_to_mile

    @property
    def to_foot(self):
        """
        This method converts the value to Foot unit
        """
        return self.__value*self.__value_convert_to_foot

    @property
    def to_inch(self):
        """
        This method converts the value to Inch unit
        """
        return self.__value*self.__value_convert_to_inch

    @property
    def to_light_year(self):
        """
        This method converts the value to Light Year unit
        """
        return self.__value*self.__value_convert_to_light_year