import json


def print_matrix(a):
    for row in a:
        for col in row:
            print(col, end=" ")
        print("")


def flatten(range_r):
    res = []
    for i in range_r:
        for j in i:
            res.append(j)
    return res


def find_ind(range_r, x):
    for i, subrange in enumerate(range_r):
        if x in subrange:
            return i


def check_any_in(p1, p2):
    f = False
    for x in p1:
        f = f or (x in p2)
    return f


def f(x):
    if isinstance(x, int):
        return [x]
    return x


def parse_range(r):
    return [f(x) for x in json.loads(r)]


def _in_conflicts(value, conflicts):
    for cluster in conflicts:
        if value in cluster:
            return True, cluster
    return False, []
