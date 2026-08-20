def totalsum(i):
  if i==1:
    return 1
  return i+totalsum(i-1)
def fact(i):
  if i==1:
    return 1
  return i*fact(i-1)
def main():
  n=int(input())
  print(totalsum(n))
  print(fact(n))
  
if __name__=="__main__":
  main()