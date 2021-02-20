import numpy as np
from numpy.linalg import norm


class Solver():
    '''
    solves a set of equations at a single point in time
    '''
    def __init__(self, tolerance=1e-3):
        self.tolerance = tolerance

    def solve(self, simobjs, target_fcn):
        for obj in simobjs:
            err = 0
            for eq in obj.eqs:
                err += eq()

        assert(err < self.tolerance)

        pass


class SimObj():
    def __init__(self, p1, p2, length):
        self.p1 = p1
        self.p2 = p2
        self.length = length
        self.eqs = [
            lambda: norm(self.p1 - self.p2) - length,
        ]


def test():
    objs = []

    p1 = np.array([0, 0])
    p2 = np.array([0, 1])
    length1 = 1
    objs.append(SimObj(p1, p2, length1))

    p3 = np.array([1, 1])
    length2 = 1
    objs.append(SimObj(p2, p3, length2))

    solver = Solver()
    solver.solve(objs, None)


def main():
    tolerance = 1e-3

    p1 = np.array([0, 0])
    p2 = np.array([0, 1])
    length1 = 1
    link1_len = lambda v1, v2: norm(v2 - v1) - length1

    p3 = np.array([1, 1])
    length2 = 1
    link2_len = lambda v1, v2: norm(v2 - v1) - length2

    assert(link1_len(p1, p2) < tolerance)
    assert(link2_len(p2, p3) < tolerance)


if __name__ == '__main__':
    test()
