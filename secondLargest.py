class secondLargest:
  def SecondLargest(self,arr):
    arr.sort()
    largest = arr[-1]
    for i in range(len(arr)-2,-1,-1):
      if arr[i] != largest:
        return arr[i]
    return -1
def main():
  arr = [1, 2, 3, 4, 5]
  obj = secondLargest()
  result = obj.SecondLargest(arr)
  print("Second largest element is:", result)
if __name__ == "__main__":
  main()