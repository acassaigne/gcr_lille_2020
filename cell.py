
class Cell(object):

    def __init__(self, a_live=True):
        self._a_live = a_live

    def tick(self, live_neighbors):
        if live_neighbors == 3:
            self._a_live = True
        if live_neighbors <= 1 or live_neighbors >=4:
            self._a_live = False

    def is_alive(self):
        return self._a_live
