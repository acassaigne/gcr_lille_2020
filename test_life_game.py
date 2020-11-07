import unittest

class TestMain(unittest.TestCase):

    def test_1(self):
        grid = Grid()
        self.assertTrue(grid.is_dead(0,0))