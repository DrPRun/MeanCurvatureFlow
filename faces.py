import numpy as np
class Faces(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.storage = {}

    def __setitem__(self, key, value):
        self.storage[key] = value

    def __getitem__(self, key):
        if key == 0:
            return self.a
        elif key == 1:
            return self.b
        elif key == 2:
            return self.c
        else:
            return None

class crdvtx(object):

    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
        self.storage = {}

    def __setitem__(self, key, value):
        self.storage[key] = value

    def __getitem__(self, key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        if key == 2:
            return self.z
        else:
            return None
