def print_name(i,n):
  if i>n:
    return 
  print("Bhanu")
  print_name(i+1,n)
def linear(j,n):
  if j>n:
    return
  print(j)
  linear(j+1,n)

def back(k,n):
  if k<1:
    return 
  print(k)
  back(k-1,n)

def main():
  n=int(input())
  i=1
  j=1
  k=n
  print_name(i,n)
  linear(j,n)
  back(k,n)
if __name__=="__main__":
  main()