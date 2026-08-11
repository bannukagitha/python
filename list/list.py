a = [5, 10, 15, 20, 25]
for i in range(len(a)):
  print(i,a[i])#returns the index and the value of the index 
ar = [3, 7, 2, 9, 4]
for x in ar:
  print(x)
n=int(input())
values=list(map(int,input().split()))
arr=[]
for value in values:
  arr.append(value)
print(arr)
arr.insert(0,55)
arr.insert(n,67)
arr.insert(n+1,99)
print(arr)
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.extend(B)
print(A)
print(B)
array=[10,20,30,40,50]
x=array.pop()
print(array)
print(x)
M=int(input())
C=list(map(int,input().split()))
C.sort()
print(C)