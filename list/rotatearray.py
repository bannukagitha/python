def rotateLeft(d, arr):
    d=d%len(arr)
    arr[:d] = reversed(arr[:d])
    arr[d:] = reversed(arr[d:])
    arr.reverse()
    return arr
arr=[1,2,3,4,5]
d=int(input())
print(rotateLeft(d,arr))
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    n=len(nums)
    k=k%n
    def reverse(start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)