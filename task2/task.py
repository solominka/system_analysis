import csv


# задание
# 1. граф -> csv (список ребер)
# 2. для каждого элемента посчитать, сколько раз он входит в каждый тип отношений (строчка значений r1 r2 r3 r4 r5)
# r1 - я начальник
# r2 - я подчиненный
# r3 - у моего подчиненного есть подчиненный
# r4 - у моего начальника есть начальник
# r5 - соподчинение


def read_graph(file_name):
    graph = []
    with open(file_name) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ')
        for row in csvreader:
            f = int(row[0])
            t = int(row[1])
            graph.append([f, t])
    return graph


def get_parent(graph, x):
    for edge in graph:
        if edge[1] == x:
            return [edge[0]]
    return []


def get_children(graph, x):
    children = []
    for edge in graph:
        if edge[0] == x:
            children.append(edge[1])
    return children


def calc_rs(graph):
    ans = []
    n = max([max(i) for i in graph])
    for i in range(n):
        children = get_children(graph, i + 1)
        parent = get_parent(graph, i + 1)
        r1 = len(children)
        r2 = len(parent)
        r3 = 0
        for child in children:
            r3 += len(get_children(graph, child))
        if len(parent) == 0:
            r4 = 0
            r5 = 0
        else:
            r4 = len(get_parent(graph, parent[0]))
            r5 = max(len(get_children(graph, parent[0])) - 1, 0)
        ans.append([r1, r2, r3, r4, r5])
    return to_csv(ans)


def to_csv(ans):
    string = ""
    for row in ans:
        string += " ".join(str(x) for x in row)
        string += '\n'
    return string


def task(str):
    graph = read_graph(str)
    return calc_rs(graph)


# if __name__ == '__main__':
#     print(task('graph.csv'))
