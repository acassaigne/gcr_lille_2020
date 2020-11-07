import unittest

class Grid():
    def is_dead(self, x, y):
        return True

class TestMain(unittest.TestCase):

    def test_cell_is_dead(self):
        grid = Grid()
        self.assertTrue(grid.is_dead(0,0))
        
    def test_cell_is_alive(self):
        grid = Grid()
        grid.set_alive(0,0)
        self.assertTrue(grid.is_alive(0,0))

if __name__ == '__main__':
    unittest.main()