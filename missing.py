class missing:
  def Missing(self,arr):
    n = len(arr)
    total = (n + 1) * (n + 2) // 2
    sum_arr = sum(arr)
    return total - sum_arr
def main():
  arr = [1, 2, 3, 5]
  obj = missing()
  result = obj.Missing(arr)
  print("Missing number is:", result)
if __name__ == "__main__":
  main()