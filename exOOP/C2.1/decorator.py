class Square:

    def __int__(self, a):
        if a > 0:
            self._a = a

    @property
    def sq(self):
        return self._a

    @sq.setter
    def sq(self, value):
        if value > 0:
            self._a = value

