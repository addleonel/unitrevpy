
from converter.length import Meter, Yard, LightYear
from converter.temperature import Celsius, Fahrenheit, Kelvin

if __name__ == '__main__':
    # length
    print(Meter(34).to_inch())
    print(Yard(20).to_meter())
    print(LightYear(0.000000000003434).to_mile())
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


