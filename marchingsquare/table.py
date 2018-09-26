from typing import Tuple, List
# format(15, '08b')
class Table:
    def __init__(self):
        self.table =((0b0000, []), (0b1000, ['left', 'bottom']), (0b0100, ['left', 'top']), (0b0010, ['top', 'right']),
         (0b0001, ['right', 'bottom']), (0b1100, ['top', 'bottom']), (0b1001, ['left', 'right']),
         (0b1010, ['left', 'top', 'right', 'bottom']), (0b1111, []), (0b0111, ['left', 'bottom']),
         (0b1011, ['left', 'top']), (0b1101, ['top', 'right']), (0b1110, ['right', 'bottom']),
         (0b0011, ['top', 'bottom']), (0b0110, ['left', 'right']), (0b0101, ['left', 'top', 'right', 'bottom']))

    def ltable(self):
        return self.table




