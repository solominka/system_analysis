import csv


# file_name - абсолютный путь файла
# i, j - номер строки и столбца, пересечение которых нужно прочитать и вывести
def read_csv(file_name, i, j):
    rows = []
    with open(file_name) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            rows.append(row)
        print(rows[i][j])


# if __name__ == '__main__':
#     read_csv('/Users/introvertess/system_analysis/task1/example.csv', 1, 2)
