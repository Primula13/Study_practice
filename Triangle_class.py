"""Написать класс треугольник. В конструкторе определить длины сторон. Добавить методы для вычисления площади,
периметра, определения типа треугольника (прямой, равнобедренный, равносторонний, разносторонний)"""


class Triangle(object):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def triangle_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        print("Перимметр треугольника %d" % perimeter)

    def triangle_square(self):
        if (self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and
           self.side2 + self.side3 > self.side1):
            half_perimeter = (self.side1 + self.side2 + self.side3)/2
            square = (half_perimeter * (half_perimeter - self.side1) * (half_perimeter - self.side2) *
                      (half_perimeter - self.side3)) ** 0.5
            print("Площадь треугольника %d" % round(square, 2))
        else:
            print("Площадь не может быть вычислена для вырожденного треугольника")

    def triangle_type(self):
        if (self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and
           self.side2 + self.side3 > self.side1):
            if self.side1 == self.side2 == self.side3:
                print("Треугольник равностронний")
            elif ((self.side1 == self.side2 and self.side2 != self.side3) or (self.side2 == self.side3 and
                  self.side3 != self.side1) or (self.side3 == self.side1 and self.side1 != self.side2)):
                print("Треугольник равнобедренный")
            elif ((self.side1 ** 2 == self.side2 ** 2 + self.side3 ** 2) or
                  (self.side2 ** 2 == self.side1 ** 2 + self.side3 ** 2) or
                  (self.side3 ** 2 == self.side1 ** 2 + self.side2 ** 2)):
                print("Tреугольник прямоугольный")
            else:
                print("Треугольник разносторонний")
        else:
            print("Треугольник вырожденный")
