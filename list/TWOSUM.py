length,target=map(int,input().split())
arr=list(map(int,input().split()))
seen=set()
for val in arr:
  x=target-val
  if x in seen:
    print(x,val)
    break
  seen.add(val)
print("using set() rather than the two for loops reduces the complexity N^2 to N becaues we no need to travse arr of length N two types  ")