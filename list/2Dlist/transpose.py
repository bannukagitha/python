rows = 2
cols = 3

a = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []

for j in range(cols):
    new_row = []

    for i in range(rows):
        new_row.append(a[i][j])

    transpose.append(new_row)

for i in transpose:
    print(i,sep="\n")