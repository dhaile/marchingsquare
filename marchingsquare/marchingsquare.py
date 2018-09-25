# from collections import namedtuple
from typing import Tuple, List
from . import table

class MarchingSquare:
    """
        Input : F is a 2D array of scalar values.
        Coord is a 2D array of (x, y) coordinates.
        sigma is an isovalue.
        Result : A set Y of isocontour line segments.









        TODO   import 'interpo'

        """

    def __init__ (self, table: table.Table() ):
        self.grid = [[0 for x in range(r)] for y in range(2)]
        print(self)


    def __str__(self):
        return self.sigma

    def grid(self, l):
        d = {}
        for x, m in enumerate(l):
            for y, n in enumerate(m):
                d.update({(x, y): [n, math.nan]})
        return d

    def sign(self, sigma, grid):
        for k, v in grid.items():
                if sigma > v[0]
                   v[1] = 0
                else:
                   v[1] = 1


    def assign(self, sigma, grid):
        """
        Assign '+' or '-' signs to each vertex
        :param vertx:
        :param sigma:
        :return:
        """

        sign(sigma, grid)

    def table(self):
        """

        :return: contains sixteen entries, one for each configuration
        """
        # count clockwise
        super

    def march(self, sigma: int, g):
        # Grid = Tuple(List(int, int, int))
        self.sigma = sigma
        self.grid = grid(g)
        grid = self.grid
        assign(sigma, grid)

