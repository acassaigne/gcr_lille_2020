import unittest
from cell import Cell


class Grid(object):

    def __init__(self):
        self.cells = []

    def is_empty(self):
        return len(self.cells) == 0

    def set_cells(self, cells):
        self.cells = cells

    def tick(self):
        pass


class TestMain(unittest.TestCase):

    def test_one_cell_dead_become_alive_when_she_has_3_neighbors(self):
        cell = Cell(a_live=False)
        cell.tick(live_neighbors=3)
        self.assertTrue(cell.is_alive())

    def test_a_cell_alive_died_when_she_has_zero_neighbors(self):
        cell = Cell()
        cell.tick(live_neighbors=0)
        self.assertFalse(cell.is_alive())

    def test_a_cell_alive_died_when_she_has_one_neighbors(self):
        cell = Cell()
        cell.tick(live_neighbors=1)
        self.assertFalse(cell.is_alive())

    def test_a_cell_alive_died_when_she_has_four_or_more_neighbors(self):
        cell = Cell()
        cell.tick(live_neighbors=4)
        self.assertFalse(cell.is_alive())

    def test_an_empty_grid_stay_empty(self):
        grid = Grid()
        self.assertTrue(grid.is_empty())

    def test_a_grid_with_one_cell_is_not_empty(self):
        grid = Grid()
        cell = Cell()
        grid.set_cells([ cell ])
        self.assertFalse(grid.is_empty())

    def test_a_tick_on_a_empty_grid_should_stay_empty(self):
        grid = Grid()
        grid.tick()
        self.assertTrue(grid.is_empty())
