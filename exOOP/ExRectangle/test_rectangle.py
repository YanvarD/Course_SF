from rectangle import Rectangle, Square,Circle

rectangle_1 = Rectangle(3,6)


sq1 = Square(4)
circ1 = Circle(8)


figures = [rectangle_1, sq1, circ1]

for figur in figures:
    if isinstance(figur, Square):
        print("площадь квадрата", figur.get_area_square())
    elif isinstance(figur, Circle):
        print("площадь круга - ", circ1.get_area_circle())
    else:
        print("Площадь прямоугольника - ", rectangle_1.get_area())



