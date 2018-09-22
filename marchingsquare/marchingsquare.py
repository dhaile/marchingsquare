from collections import namedtuple


class marchingSquare:
    """
        Input : F is a 2D array of scalar values.
        Coord is a 2D array of (x, y) coordinates.
        σ is an isovalue.
        Result : A set Υ of isocontour line segments.









        TODO   import 'interpo'

     """

    def __ini_marchingSquare__(self, g, table):
        Grid = namedtuple('Grid', ['x', 'y'], verbose=True)
        self.g = Grid
        self.table = {00000: {}, 1000: {'left', 'bottom'}, 0100: {'left', 'top'}, 0010: {'top', 'right'},
                      0001: {'right', 'bottom'},
                      1100: {'top', 'bottom'}, 1001: {'left', 'right'}, 1010: {'left', 'top', 'right', 'bottom'},
                      1111: {},
                      0111: {'left', 'bottom'}, 1011: {'left', 'top'}, 1101: {'top', 'right'},
                      1110: {'right', 'bottom'},
                      0011: {'top'cc, 'bottom'}, 0110:{'left', 'right'}, 0101:{'left', 'top', 'right', 'bottom'}}








    def assign(self, sigma):
        """
        Assign “+” or “−” signs to each vertex

        :param sigma:
        :return:
        """
        g = self.g
        for each v in g:
           if sigma >

    def table(self):
        """

        :return: contains sixteen entries, one for each configuration
        """
        # count clockwise
