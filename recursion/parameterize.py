def totalsum(i,total):
  if i<1:
    print(total)
    return
  totalsum(i-1,total+i)
def main():
  n=int(input())
  totalsum(n,0)
  
if __name__=="__main__":
  main()