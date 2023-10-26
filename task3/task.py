import math

from task3.task2 import task2


# Задание
# рассчитать величину энтропии системы
def parse_matrix(var: str):
    rows = var.split("\n")
    matrix = []
    for row in rows:
        matrix.append([int(x) for x in row.split(" ")])
    return matrix


def task(var: str):  # var - матрица r1-r5
    matrix = parse_matrix(var)
    n = len(matrix)
    k = len(matrix[0])
    h = 0
    for i in range(n):
        hi = 0
        for j in range(k):
            Pij = matrix[i][j] / (n - 1)
            if Pij != 0:
                hi -= Pij * math.log2(Pij)
        h += hi
    return round(h, 1)


if __name__ == '__main__':
    print(
        task(
            task2("/Users/introvertess/system_analysis/task2/graph.csv")
        )
    )
