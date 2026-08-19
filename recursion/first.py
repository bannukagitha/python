def print_name(i,n):
  if i>n:
    return 
  print("Bhanu")
  print_name(i+1,n)

n=int(input())
i=1
print_name(i,n)