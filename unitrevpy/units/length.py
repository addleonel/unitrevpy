# Length units
import numpy as np
from .unit import Unit


class Length(Unit):
    """
    units used
    meter, yard, mile, foot, inch, light_year
    """
    def __init__(self, value, prefix, *args, **kwargs):
        super(Length, self).__init__(value, prefix)
        if kwargs:
            self.__to_meter = kwargs['meter']
            self.__to_yard = kwargs['yard']
            self.__to_mile = kwargs['mile']
            self.__to_foot = kwargs['foot']
            self.__to_inch = kwargs['inch']
            self.__to_light_year = kwargs['light_year']

        if self.prefix:
            self.__to_meter = kwargs['meter'] * self.PREFIX[self.prefix][1]
            self.__to_yard = kwargs['yard'] * self.PREFIX[self.prefix][1]
            self.__to_mile = kwargs['mile'] * self.PREFIX[self.prefix][1]
            self.__to_foot = kwargs['foot'] * self.PREFIX[self.prefix][1]
            self.__to_inch = kwargs['inch'] * self.PREFIX[self.prefix][1]
            self.__to_light_year = kwargs['light_year'] * self.PREFIX[self.prefix][1]

        if args:
            self.sym = args[0]

    def __operator(self, convert_value, circling):
        if isinstance(self.value, (list,)):
            return list(np.round(np.array(self.value)*convert_value, circling))
        return round(self.value*convert_value, circling)

    def meter(self, circling=4):
        """
        This method converts the value to Meter unit
        """
        return self.__operator(self.__to_meter, circling)

    def yard(self, circling=4):
        """
        This method converts the value to Yard unit
        """
        return self.__operator(self.__to_yard, circling)

    def mile(self, circling=4):
        """
        This method converts the value to Mile unit
        """
        return self.__operator(self.__to_mile, circling)

    def foot(self, circling=4):
        """
        This method converts the value to Foot unit
        """
        return self.__operator(self.__to_foot, circling)

    def inch(self, circling=4):
        """
        This method converts the value to Inch unit
        """
        return self.__operator(self.__to_inch, circling)

    def light_year(self, circling=4):
        """
        This method converts the value to Light Year unit
        """
        return self.__operator(self.__to_light_year, circling)


class Meter(Length):
    def __init__(self, value, prefix=None):
        super(Meter, self).__init__(
            value,
            prefix,
            'm',
            meter=1.0,
            yard=1.0936132983,
            mile=0.0006213712,
            foot=3.280839895,
            inch=39.37007874,
            light_year=1.057008707E-16,
        )


class Yard(Length):
    def __init__(self, value, prefix=None):
        super(Yard, self).__init__(
            value,
            prefix,
            'yd',
            meter=0.9144,
            yard=1.0,
            mile=0.0005681797,
            foot=3.0,
            inch=36.0,
            light_year=9.665287622E-17
        )


class Mile(Length):
    def __init__(self, value, prefix=None):
        super(Mile, self).__init__(
            value,
            prefix,
            'mi',
            meter=1609.35,
            yard=1760.0065617,
            mile=1.0,
            foot=5280.019685,
            inch=63360.23622,
            light_year=1.701096963E-13
        )


class Foot(Length):
    def __init__(self, value, prefix=None):
        super(Foot, self).__init__(
            value,
            prefix,
            'ft',
            meter=0.3048,
            yard=0.3333333333,
            mile=0.0001893932,
            foot=1.0,
            inch=12.0,
            light_year=3.22176254E-17
        )


class Inch(Length):
    def __init__(self, value, prefix=None):
        super(Inch, self).__init__(
            value,
            prefix,
            'in',
            meter=0.0254,
            yard=0.0277777778,
            mile=0.0000157828,
            foot=0.0833333333,
            inch=1.0,
            light_year=2.684802117E-18
        )


class LightYear(Length):
    def __init__(self, value, prefix=None):
        super(LightYear, self).__init__(
            value,
            prefix,
            'ly',
            meter=9460660000000000.0,
            yard=10346303587051618.0,
            mile=5878559666946.0,
            foot=31038910761154856.0,
            inch=372466929133858300.0,
            light_year=1.0
        )
