n=int(input())
arr=list(map(int,input().split()))
palindrome=True
left = 0
right = len(arr) - 1
while left < right:
    if arr[left]!=arr[right]:
        palindrome=False
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)
print("True"if palindrome else "False")

