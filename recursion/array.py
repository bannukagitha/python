def reversearray(l,r,arr):
  if l==r:
    return
  arr[l],arr[r]=arr[r],arr[l]
  return reversearray(l+1,r-1,arr)

def reverse(i,arr):
  if i==len(arr)-i-1:
    return
  arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
  return reverse(i+1,arr)
def palindrome(i,arr):
  if i>=len(arr)-i-1:
    return True
  if arr[i]!=arr[len(arr)-i-1]:
    return False
  return palindrome(i+1,arr)
  
  
arr=[1,2,3,2,1]
print(palindrome(0,arr))
reverse(0,arr)
print(arr)