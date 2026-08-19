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

def main():
  n=int(input())
  i=1
  j=1
  print_name(i,n)
  linear(j,n)
if __name__=="__main__":
  main()