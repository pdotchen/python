from math import pi
import copy


class Shape:
    def __init__(self, name="no name", color="white"):
        self.name = name
        self.color = color
        self.symmetry = None

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return "Shape with name {} and color {}".format(self.name, self.color)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "Point at ({}, {})".format(self.x, self.y)


class Symmetry(Point):
    def __init__(self, x=0, y=0):
        Point.__init__(self, x, y)

    def __str__(self):
        return "Point of symmetry is ({}, {})".format(self.x, self.y)


class Rectangle(Shape):
    def __init__(self, name="no name", color="white", point=Point(0, 0), w=0, h=0):
        Shape.__init__(self, name, color)
        self.point = point
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def __str__(self):
        return "Rectangle with corner at {} and width = {}, height = {}".format(self.point, self.w, self.h)


class Square(Rectangle):
    def __init__(self, name="no name", color="white", point=Point(0, 0), w=0):
        Rectangle.__init__(self, name, color, point, w, w)
        self.symmetry = Symmetry(point.x + self.w / 2, point.y - self.w / 2)

    def __str__(self):
        return "Square with width = {} and center of symmetry {}".format(self.w, self.symmetry)


class Circle(Shape):
    def __init__(self, name="no name", color="white", center=Point(0, 0), r=0):
        Shape.__init__(self, name, color)
        self.center = center
        self.radius = r
        self.symmetry = Symmetry(center.x, center.y)

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return "Circle with center at {} and radius = {}".format(self.center, self.radius)


class Plane():
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        self.shapes.remove(shape)

    def area_coverage(self):
        return sum([shape.area() for shape in self.shapes])

    def __len__(self):
        return len(self.shapes)

    def __str__(self):
        s = ""
        if len(self.shapes) == 0:
            s += "no shapes"
        for shape in self.shapes:
            s += shape.__str__() + "\n"
        return "A plane with: \n" + s

    def center_of_point_of_symmetry(self):
        x = 0
        y = 0
        count = 0
        for shape in self.shapes:
            if shape.symmetry is not None:
                x += shape.symmetry.x
                y += shape.symmetry.y
                count += 1
        return Symmetry(x / count, y / count)


corner = Point(2, 2)
shape = Shape("shape 1", "purple")
rectangle = Rectangle("shape 2", "orange", Point(1, 1), 10, 20)
square = Square("shape 3", "red", Point(3, 3), 30)
circle = Circle("shape 4", "black", Point(4, 4), 9)
print(corner)
print(shape)
print(rectangle)
print(square)
print(circle)
print(shape.symmetry)
print(rectangle.symmetry)
print(square.symmetry)
print(circle.symmetry)
plane = Plane()
print(plane)
plane.add_shape(square)
plane.add_shape(rectangle)
plane.add_shape(circle)
print(plane)
print(plane.center_of_point_of_symmetry())
plane.remove_shape(square)
print(plane)
print(plane.center_of_point_of_symmetry())

dict1 = {'a': 1, 'b': 1, 'c': 1, 'd': 2, 'e': 3, 'f': 4}
dict2 = dict()

for key in dict1.keys():
    if dict1[key] not in dict2.keys():
        dict2[dict1[key]] = [key]
    else:
        dict2[dict1[key]].append(key)

print(dict1)
print(dict2)
min_key = min(dict2.keys())
print(min_key)
list_of_names = dict2[min_key]
print(list_of_names)
low_priority_name = 'zzz'
for element in list_of_names:
    if element < low_priority_name:
        low_priority_name = element
print(low_priority_name)


def extract_low_priority_name(dictionary):
    dict2 = dict()
    for key in dictionary.keys():
        if dictionary[key] not in dict2.keys():
            dict2[dictionary[key]] = [key]
        else:
            dict2[dictionary[key]].append(key)

    min_key = min(dict2.keys())
    list_of_names = dict2[min_key]
    low_priority_name = 'zzz'
    for element in list_of_names:
        if element < low_priority_name:
            low_priority_name = element
    return low_priority_name


ordered_list = []
copy_dic = copy.deepcopy(dict1)

while len(ordered_list) < len(dict1):
    name = extract_low_priority_name(copy_dic)
    del copy_dic[name]
    ordered_list.append(name)

print(ordered_list)
