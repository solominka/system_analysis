import numpy as np

from task5.utils import flatten, parse_range, find_ind


def calc_kendall(experts):
    n = len(flatten(parse_range(experts[0])))
    m = len(experts)
    ranks = [[0 for _ in range(m + 2)] for _ in range(n)]

    for i, e in enumerate(experts):
        r = parse_range(e)
        for j in range(n):
            ranks[j][i] = find_ind(r, j + 1) + 1

    sums = [sum(ranks[i]) for i in range(n)]
    sums.sort()

    mean = sum(sums) / n
    d = sum([(s - mean) ** 2 for s in sums]) / (n - 1)

    sums_max = [i * m for i in range(n)]
    mean = sum(sums_max) / n
    d_max = sum([(s - mean) ** 2 for s in sums_max]) / (n - 1)

    return d / d_max


def task(experts):
    res = calc_kendall(experts)
    return round(res, 2)


if __name__ == "__main__":
    a = "[1,2,3]"
    b = "[1,3,2]"
    c = "[1,3,2]"

    print(task([a, b, c]))
