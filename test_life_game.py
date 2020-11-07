import unittest

class Grid():

    def __init__(self):
        self.grid = {(0,0): False}

    def is_dead(self, x, y):
        return not self.is_alive(x, y)

    def set_alive(self, x, y):
        self.grid[(x,y)] = True

    def is_alive(self, x, y):
        return self.grid[(x,y)]

class TestMain(unittest.TestCase):

    def test_cell_is_dead(self):
        grid = Grid()
        self.assertTrue(grid.is_dead(0,0))
        
    def test_cell_is_alive(self):
        grid = Grid()
        grid.set_alive(0,0)
        self.assertTrue(grid.is_alive(0,0))
        
    def test_3(self):
        grid = Grid()
        grid.set_alive(0,0)
        self.assertFalse(grid.is_dead(0,0))

if __name__ == '__main__':
    unittest.main()