r1, c1 = map(int, input().split())

A = []

for i in range(r1):
    A.append(list(map(int, input().split())))

r2, c2 = map(int, input().split())

B = []

for i in range(r2):
    B.append(list(map(int, input().split())))

result = []

for i in range(r1):
    row = []

    for j in range(c2):
        total = 0

        for k in range(c1):
            total += A[i][k] * B[k][j]

        row.append(total)

    result.append(row)

for row in result:
    print(*row)