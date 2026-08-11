row,col=map(int,input().split())
matrix=[]
for i in range(row):
  matrix.append(list(map(int,input().split())))
print("Row Sum")
for row1 in matrix:
  total=0
  for j in row1:
    total+=j
  print(total)
print("Column Sum:")
for j in range(col):
  total=0
  for i in range(row):
    total+=matrix[i][j]
  print(total)