num_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])


def valid_squares(matrix):
    sum1, sum2, sum3 = 0, 0, 0

    for i in range(0, 7, 3):
        for row in matrix[i:i+3]:
            sum1 += sum(row[0:3])
            sum2 += sum(row[3:6])
            sum3 += sum(row[6:9])

    if sum1 != 135 or sum2 != 135 or sum3 != 135:
        return False

    return True


def valid_row(matrix):
    for row in matrix:
        if set(row) != num_set:
            return False
    return True


def valid_column(matrix):
    column = 0
    while column < 9:
        col = set()
        for row in matrix:
            col.add(row[column])
        if col != num_set:
            return True
        column += 1
    return True


if __name__ == '__main__':
    for case in range(int(input())):
        print("Instacia", case+1)  # Portuguese for instance
        matrix = [list(map(int, input().split())) for _ in range(9)]

        if valid_row(matrix) & valid_column(matrix):
            print("SIM\n")
        else:
            print("NAO\n")

