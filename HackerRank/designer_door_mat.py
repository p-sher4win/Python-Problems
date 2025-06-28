# N = rows, 5 < N < 101
# M = columns, 15 < M 303

N, M = map(int, input().split())
N+=2

for i in range(1, N, 2):
    if i == N-2:
        print('WELCOME'.center(M, '-'))
    elif i < N-2:
        print(('.|.' * i).center(M, '-'))

for i in range(N-4, 0, -2):
    print(('.|.' * i).center(M, '-'))
