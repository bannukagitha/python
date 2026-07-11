class missing:
  def Missing(self,arr):
    n = len(arr)
    total = (n + 1) * (n + 2) // 2
    sum_arr = sum(arr)
    return total - sum_arr

def main():
  n=int(input("Enter the number of elements in the array: "))
  arr = []
  print("Enter the elements of the array:")
  for _ in range(n):
    arr.append(int(input()))
  obj = missing()
  print("The missing number is:", obj.Missing(arr))
  
if __name__ == "__main__":
  main()
  