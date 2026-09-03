def findIndex (self, arr, key):
  #code here
  first=second=-1
  if key not in arr:
      return [first,second]
  for i in range(len(arr)):
      if arr[i]==key:
          if first!=-1:
              second=i
          else:
              first=second=i
  return [first,second]