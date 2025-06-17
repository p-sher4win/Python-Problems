if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])

    second_lowest = []

    python_students.sort(key=lambda each: each[1])

    second_lowest_1 = python_students[1]
    second_lowest.append(second_lowest_1[0])

    second_lowest_2 = ''

    for each_mark in python_students:
        if each_mark[1] == second_lowest_1[1]:
            second_lowest_2 = each_mark

    second_lowest.append(second_lowest_2[0])

    second_lowest.sort()
    for name in second_lowest:
        print(name)

