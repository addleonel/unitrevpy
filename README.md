# unitrevpy
## Summary
unitrevpy is a package that contains common unit conversions such as  __length__, __temperature__, __area__, __volume__, __time__, and __weight__.
## What units does it contain?
Specifically contains:

Magnitude | Units
-------------|-------------
|**Lenght**|Meter, Yard, Mile, Foot, Inch, and Light Year.|
|**Temperature**|Celsius, Kelvin, and Fahrenheit.|
|**Area**|Square meter, Hectare, Square Mile, Square Yard, Square Foot, Square Inch, and Acre.|
|**Volume**|Cubic Meter, Cubic Kilometer, Cubic Centimeter, Cubic Millimeter, Liter, Milliliter, US Gallon, US Quart, US Pint, US Cup, US Fluid Ounce, US Table Spoon, US Tea Spoon, Imperial Gallon, Imperial Quart, Imperial Pint, Imperial Fluid Ounce, Imperial Table Spoon, Imperial Tea Spoon, Cubic Mile, Cubic Yard, cubic Foot, and Cubic Inch.|
|**Time**|Second, Minute, Hour, Day, Week, Month, and Year.|
|**Weight**|Kilogram, Gram, Millimeter, Metric Ton, Long Ton, Short Ton, Pound, Ounce, Carat, and Atomic Mass Unit (Dalton).|

## installation
```
pip install unitrevpy
```
or
```
python -m pip install unitrevpy
```
To import it into a script:
```python
from unitrevpy import convert
```
or
```python
from unitrevpy.convert import Celsius
```

## Example
Using an integer or float argument:
```python
from unitrevpy import convert as c
y = c.Meter(23).to_yard()
m = c.Meter(4500).to_mile()
```
Using list, tuple, or set:
```python
from unitrevpy.convert import Kelvin
kelvin = [23, 20, 16]
celsius = Kelvin(kelvin).to_celsius()
```
