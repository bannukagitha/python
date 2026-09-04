def getMoreAndLess(self, arr, target):
  # code here
  less_equal=0
  greater_equal=len(arr)
  l=0
  r=len(arr)
  while l<r:
      mid=(l+r)//2
      if arr[mid]<=target:
          l=mid+1
      else:
          r=mid
  less_equal=l
  l=0
  r=len(arr)
  while l<r:
      mid=(l+r)//2
      if arr[mid]<target:
          l=mid+1
      else:
          r=mid
  greater_equal=len(arr)-r
  return [less_equal,greater_equal]