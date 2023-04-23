# С помощью наследования постройте иерархию геометрических фигур, состоящую из следующих классов:
#
# Shape (Фигура)
# Polygon (Многоугольник)
# Triangle (Треугольник)
# IsoscelesTriangle (Равнобедренный треугольник)
# EquilateralTriangle (Равносторонний треугольник)
# Quadrilateral (Четырехугольник)
# Parallelogram (Параллелограмм)
# Rectangle (Прямоугольник)
# Square (Квадрат)
# Иерархия должна быть построена в соответствии со следующим условием: класс B должен наследоваться от класса A, если B является частным случаем A.

# Фигура
class Shape:
    pass


# Многоугольник
class Polygon (Shape):
    pass


# Треугольник
class Triangle(Polygon):
    pass


# Равнобедренный треугольник
class IsoscelesTriangle(Triangle):
    pass


#  (Равносторонний треугольник)
class EquilateralTriangle(IsoscelesTriangle):
    pass


# Четырехугольник
class Quadrilateral(Polygon):
    pass


# Параллелограмм
class Parallelogram(Quadrilateral):
    pass


# Прямоугольник
class Rectangle(Parallelogram):
    pass


# Square
class Square(Rectangle):
    pass

