from converter.length import (Meter, Yard, Mile, Foot, Inch, LightYear)
from converter.temperature import (Celsius, Fahrenheit, Kelvin)
from converter.area import (
    SquareMeter, Hectare, SquareMile, SquareYard, SquareFoot, SquareInch, Acre)
from converter.volume import (
    CubicMeter, CubicKilometer, CubicCentimeter, CubicMillimeter, Liter, Milliliter,
    USGallon, USQuart, USPint, USCup, USFluidOunce, USTableSpoon, USTeaSpoon, ImperialGallon,
    ImperialQuart, ImperialPint, ImperialFluidOunce,ImperialTableSpoon, ImperialTeaSpoon,
    CubicMile, CubicYard, CubicFoot, CubicInch
)
from converter.time import (Second, Minute, Hour, Day, Week, Month, Year)
from converter.weight import (
    Kilogram, Gram, Milligram, MetricTon, LongTon, ShortTon, Pound,
    Ounce, Carat, AtomicMassUnit
)

if __name__ == '__main__':

    # num = Length(23, 'meter')
    # print(num.__to_yard())
    number = Meter(23)
    print(number.to_yard())
    print(number.to_foot())
    print(number.to_mile())