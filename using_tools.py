
from converter.length import Meter, Yard, LightYear
from converter.temperature import Celsius, Fahrenheit, Kelvin
from converter.area import SquareInch, SquareFoot
from converter.volume import Liter, CubicMeter, Milliliter
from converter.weight import Kilogram, MetricTon
from converter.time import Second, Minute

if __name__ == '__main__':
    # length
    print(Meter(40).to_inch())
    print(Yard(20).to_meter())
    print(LightYear(1).to_meter())
    print("-"*30)
    # temperature
    print(Celsius(20).to_kelvin())
    print(Celsius(20).to_fahrenheit())
    print(Kelvin(20).to_celsius())
    print(Kelvin(20).to_fahrenheit())
    print(Fahrenheit(20).to_celsius())
    print(Fahrenheit(20).to_kelvin())
    print(Fahrenheit(20).value)
    # area
    print("-"*30)
    print(SquareInch(30).to_hectare())
    print(SquareFoot(40).to_square_meter())
    # volume
    print("-"*40)
    print(Liter(80).to_cubic_centimeter())
    print(Milliliter(100))
    print(CubicMeter(0.40))
    # weight
    print("-"*30)
    print(Kilogram(300).to_gram())
    print(MetricTon(4).to_kilogram())
    # time
    print("-"*30)
    print(Second(800).to_minute())
    print(Minute(700).to_hour())

