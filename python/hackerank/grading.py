def fix_grade(grade):
    if grade < 38:
        return grade
    else:
        for x in range(1, 3):
            if (grade+x)%5 == 0:
                return grade+x
        return grade


if __name__ == '__main__':
    grades = []
    for _ in range(int(input())):
        grades.append(fix_grade(int(input())))
    print(*grades, end="\n", sep="\n")