import unittest


class Grid(object):
    def __init__(self):
        self.cell = False
        self.grid = {}

    def is_alive(self, x, y):
        return self.grid[(x,y)]

    def set_alive(self, x, y):
        self.grid[(x,y)] = True


class TestMain(unittest.TestCase):

    def test_cell_is_dead(self):
        grid = Grid()
        result = grid.is_alive(0,0)
        self.assertEqual(False, result)

    def test_cell_is_alive(self):
        grid = Grid()
        grid.set_alive(0,0)
        result = grid.is_alive(0,0)
        self.assertEqual(True, result)

    def test_3(self):
        grid = Grid()
        grid.set_alive(0,1)
        result = grid.is_alive(0,0)
        self.assertEqual(False, result)


