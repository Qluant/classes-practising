from classes import Figure2D, Rectangle, Square, Cube


print("Docs:")
print(Figure2D.__doc__)

print("Generation (input: 5):")
print(Figure2D.generate_sides(5), Rectangle.generate_sides(5),
      Square.generate_sides(5), Cube.generate_sides(5), sep="\n")
# Output:
# [42.609922960449026, 26.51080729071867, 32.83178228648818, 31.251492711232473, 32.742291622587125]
# [5, 5, 10, 10]
# [5, 5, 5, 5]
# [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]


print("\nErrors:")
try:
    figure = Figure2D([1, 3])
except Exception as error_description:
    print(error_description)
# Output:
# Invalid count of sides - the number of sides must be in the range from 3 to 100. Size of given list: 2

try:
    square = Square([1, 2, 3, 2, 6])
    square.square()
except Exception as error_description:
    print(error_description)
# Output:
# A square can only have 4 sides

try:
    square = Square([1, 2, 3, 2])
    square.square()
except Exception as error_description:
    print(error_description)
# Output:
# A square must have equal sides

# For all errors look into code of "classes.py"


print("\nExample 1:")
figure = Figure2D([14, 9.0, 15.7, 13.4, 25.7])
rectangle = Rectangle([2, 3.7, 3.7, 2])
print(figure.perimeter(), rectangle.perimeter())
# Output:
# 77.8 7.4

print("\nExample 2:")
rectangle = Rectangle(5)
square = Square(6)
print(rectangle.sides, square.sides, "\n", rectangle.square(), square.square())
# Output:
# [5, 5, 10, 10] [6, 6, 6, 6]
# 50.0 36.0

print("\nExample 3:")
cube = Cube(7.5)
print(cube, cube.perimeter(), cube.facet_square(), cube.square(), cube.volume(), sep="\n")
# Output:
# Figure with 12 sides: 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5
# 90.0
# 56.25
# 337.5
# 421.875

print("\nExample 4:")
print(Rectangle.is_fits_conditions([1, 2.3, 2.3, 2]), Rectangle.is_fits_conditions([1, 2.3, 2.3, 1]))
# True False

print("\nExample 5:")
print(Rectangle.dimensional, Square.dimensional, Cube.dimensional)
# 2 2 3
