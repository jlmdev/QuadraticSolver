# QuadraticSolver
# Solves quadratic equations

import math

class QuadraticSolver:
    """
    Accepts arguments to solve quadratic equations. (ax^2 + bx + c, a != 0)
    """
    def quadratic_calculation(self, a, b, c):
        """
        Accepts arguments and performs calculations to solve quadratic equations
        :param a: int - The coefficient of the squared x value
        :param b: int - The coefficient of the x value
        :param c: int - The constant
        :return: root1, root2, single root, or error message
        """
        d = b ** 2 - 4 * a * c
        if d > 0:
            discriminant = math.sqrt(d)
            root1 = (-b + discriminant) / (2 * a)
            root2 = (-b - discriminant) / (2 * a)
        elif d == 0:
            return -b / (2 * a)
        else:
            return 'This equation has no real roots'


if __name__ == '__main__':
    solver = QuadraticSolver()

    while True:
        a = int(input('a: '))
        b = int(input('b: '))
        c = int(input('c: '))
        result = solver.quadratic_calculation(a, b, c)
        print(result)
