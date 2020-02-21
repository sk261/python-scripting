import os

class branch:
    def __init__(self, name):
        self._name = name
        self._size = 0
        self._lastAccessed = 0
        self._files = []
        self._branches = []
    def __iter__(self):
        return branch_iter(self)

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        self._size = value


class branch_iter:
    def __init__(self, branch):
        self._branch = branch
        self._index = 0
    def __next__(self):
        if (self._index < len(self._branch)):
            self._index += 1
            return self._branch[self._index - 1]
        raise StopIteration

class fileTree:
    def __init__(self, path):
        self.trunk


if __name__ == "__main__":
    x = branch("test")
    x.size = 5
    a = x.size
    print(a)
    x.size += 5
    print(x.size)