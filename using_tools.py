
import convert as c


if __name__ == '__main__':
    # length
    num = c.Mile(23)
    print(num.to_meter())
    print("-"*30)
    # temperature
    tem = c.Fahrenheit(23).value
    print(tem)
    # area
    a = c.SquareMeter(34).to_square_yard()
    print(a)
    # volume
    vol = c.CubicCentimeter(345)
    print(vol)
    # weight
    w = c.Gram(34444).to_kilogram()
    print(w)
    # time
    t = c.Second(23).to_minute()
    print(t)

