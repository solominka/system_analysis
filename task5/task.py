import numpy as np

from task5.utils import find_ind, flatten, check_any_in, parse_range, _in_conflicts


def calc_matrix(r):
    n = len(flatten(r))

    matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            if find_ind(r, j + 1) >= find_ind(r, i + 1):
                matrix[i][j] = 1

    return matrix


def find_conflicts(m1, m2):
    y1 = np.array(m1)
    y2 = np.array(m2)
    y12 = np.multiply(y1, y2)
    y12t = np.multiply(y1.T, y2.T)
    conflicts = np.logical_or(y12, y12t).astype(np.int32)
    res = []
    for i in range(len(conflicts)):
        for j in range(i):
            if conflicts[i][j] == 0:
                res.append([j + 1, i + 1])

    united_conflicts = unite_conflicts(res)
    return united_conflicts


def find_common_range(a, b, conflicts):
    result = []

    used = []
    for cl in a:
        for value in cl:
            if value in used:
                continue
            flag, cluster = _in_conflicts(value, conflicts)
            if flag:
                result.append(cluster.tolist())
                for x in cluster:
                    used.append(x)
            else:
                result.append(value)

    print(result)
    return result


def unite_conflicts(c):
    n = len(c)
    for cnt in range(n):
        res = []
        to_skip = []
        for i, p1 in enumerate(c):
            if i in to_skip:
                continue
            merged = np.asarray(p1)
            for j, p2 in enumerate(c):
                if j <= i:
                    continue
                if check_any_in(p1, p2):
                    merged = np.append(merged, p2)
                    merged = np.unique(merged)
                    to_skip.append(j)
            merged.sort()
            res.append(merged)
        c = res

    return c


def solve(a, b):
    a_parsed = parse_range(a)
    b_parsed = parse_range(b)
    matrix_a = calc_matrix(a_parsed)
    matrix_b = calc_matrix(b_parsed)
    conflicts_ab = find_conflicts(matrix_a, matrix_b)
    return find_common_range(a_parsed, b_parsed, conflicts_ab)


def task(a, b):
    return solve(a, b)


if __name__ == '__main__':
    task()
