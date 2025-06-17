if __name__ == '__main__':

    python_students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])

    python_students.sort(key=lambda x: x[1])
    student_mark = dict(python_students)
    new_students_list = []

    for key, value in student_mark.items():
        if value > min(student_mark.values()):
            new_students_list.append([key, value])

    dict_new_students = dict(new_students_list)
    second_lowest = min(dict_new_students.values())
    names_sec_lowest = []

    for key, value in dict_new_students.items():
        if value == second_lowest:
            names_sec_lowest.append(key)

    names_sec_lowest.sort()

    for name in names_sec_lowest:
        print(name)