from unitrevpy import convert as c

if __name__ == '__main__':
    # length
    num = c.Mile((23.34, 23.34, 12.3))
    print(num.to_meter())
    print("-"*30)
    # temperature
    tem = c.Fahrenheit({34, 12, 12, 12, 12, 12, 25, 34}).to_fahrenheit()
    print(tem)
    print("-" * 30)
    # area
    a = c.SquareMeter([345, 234, 123, 43]).to_square_yard()
    print(a)
    print("-" * 30)
    # volume
    vol = c.CubicCentimeter([23, 34, 156, 43])
    print(vol.to_liter())
    print("-" * 30)
    # weight
    w = c.Gram(34444).to_kilogram()
    print(w)
    print("-" * 30)
    # time
    t = c.Day([23, 12, 35, 34])
    print(t.to_hour())


