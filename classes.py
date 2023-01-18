from random import uniform


class FigureError(Exception):
    """
    Exception raised for errors in the figures classes.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class Figure2D:
    '''
    Class for working with 2D figures.

    Input:
    Sides must be list with float or int in it,
    but it can be also int or float, parameter to generation.
    If you want see how use this parameter with this types look to staticmethod "generate" in this class.
    '''

    dimensional = 2

    def __init__(self, sides: [list[float, int], int, float]):
        if type(sides) in [float, int]:
            sides = self.generate_sides(sides)
            sides_count = len(sides)
        elif type(sides) == list:
            sides_count = len(sides)
            if sides_count < 3 or sides_count > 100:
                raise FigureError(f"Invalid count of sides - the number of sides must be"
                                  f" in the range from 3 to 100. Size of given list: {sides_count}")
            for side in sides:
                if type(side) not in [float, int]:
                    raise FigureError(f"Invalid type of side \"{side}\"/ It must be float or int type.")
        else:
            raise FigureError("Invalid type of sides. It can be only: "
                              "1) list with float and int in it\n"
                              "2) int - count of sides to generate it")
        self.sides = sides
        self.unique_sides = set(sides)
        self.sides_count = sides_count

    def __repr__(self) -> str:
        sides_list = [str(side) for side in self.sides]
        return f"Figure with {self.sides_count} sides: {', '.join(sides_list)}"


    def perimeter(self) -> float:
        return self.check_perimeter(self.sides)

    @staticmethod
    def generate_sides(count: int) -> list[float]:
        if count < 3 or count > 100:
            raise FigureError(f"Invalid count of sides - the number of sides must be "
                              f"in the range from 3 to 100. Size of given list: {count}")
        sides = []
        for _ in range(int(count)):
            sides.append(uniform(0.5, 100))
        return sides

    @staticmethod
    def check_perimeter(sides: list[float, int]) -> float:
        return float(sum(sides))


class Rectangle(Figure2D):

    class_sides_count = 4
    class_unique_count = 2
    sides_error_text = "A rectangle can only have 4 sides"
    unique_error_text = "A rectangle must have 2 pairs of equal sides"

    def is_necessity_figure(self) -> None:
        """
        The method causes an error when the data in the self
        does not fit the conditions of the class figure.

        This method is used only in necessary cases.
        You can contain data in instances that does not fit the conditions of the class figure,
        but in that way you can not use methods that works only with correct data.
        """
        if self.sides_count != self.class_sides_count:
            raise FigureError(self.sides_error_text)
        if len(self.unique_sides) != self.class_unique_count:
            raise FigureError(self.unique_error_text)

    @classmethod
    def is_fits_conditions(cls, sides: list[float, int]) -> bool:
        """
        This method is same to "is_necessity_figure", but is for checking
        if a given list matches the conditions of the class figure.

        Implemented as a classmethod to access class attributes.
        """
        if len(sides) != cls.class_sides_count or len(set(sides)) != cls.class_unique_count:
            return False
        return True

    @staticmethod
    def generate_sides(count: float) -> list[float]:
        sides = [count, count, count*2, count*2]
        return sides

    def square(self) -> float:
        self.is_necessity_figure()
        side_1, side_2 = self.unique_sides
        return float(side_1 * side_2)


class Square(Rectangle):

    class_unique_count = 1
    sides_error_text = "A square can only have 4 sides"
    unique_error_text = "A square must have equal sides"

    @staticmethod
    def generate_sides(count: float) -> list[float]:
        sides = [count, count, count, count]
        return sides

    def square(self) -> float:
        self.is_necessity_figure()
        return float(self.sides[0] ** 2)


# for 3D figure (cubes)
class Cube(Square):

    dimensional = 3
    class_sides_count = 12
    sides_error_text = "A cube can only have 12 sides"
    unique_error_text = "A cube must have equal sides"

    def volume(self) -> float:
        self.is_necessity_figure()
        return float(self.sides[0] ** 3)

    def square(self) -> float:
        self.is_necessity_figure()
        return super().square() * 6

    @staticmethod
    def generate_sides(side: float) -> list[float]:
        sides = []
        for _ in range(12):
            sides.append(side)
        return sides

    def facet_square(self) -> float:
        self.is_necessity_figure()
        return super().square()
