import csv


# ЗАДАНИЕ
# записать граф в виде строки в csv
# прочитать эту строку
# вывести список всех имен узлов и рядом с каждым имененем узла - его соседей

# описание файла:
# первая строчка - имена вершин
# дальше - имена вершин, с которыми соединена вершина с номером строки
def read_graph(file_name):
    graph = []
    with open(file_name) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        fields_names = next(csvreader)
        for row in csvreader:
            graph.append(row)

    for vertex_index, vertex_name in enumerate(fields_names):
        print(str(vertex_name) + " " + " ".join(str(x) for x in graph[vertex_index]))


if __name__ == '__main__':
    read_graph('graph.csv')
