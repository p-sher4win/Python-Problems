if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    all_marks = student_marks.get(query_name)
    total = 0
    for mark in all_marks:
        total += mark

    avg_marks = total / len(all_marks)
    print(f"{avg_marks:.2f}")