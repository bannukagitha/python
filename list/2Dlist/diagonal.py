row,col=map(int,input().split())
matrix=[]
for i in range(row):
  matrix.append(list(map(int,input().split())))
total=total1=0
#for i in range(row):
#  for j in range(col):
#    if i==j:
#      total+=matrix[i][j]

for i in range(row):
    total += matrix[i][i]
    total1+=matrix[i][col-i-1]
print(total)
print(total1)
difference=abs(total-total1)
print(difference)