class Solution:
    def sort012(self, arr):
        n=len(arr)
        h=n-1
        l=0
        m=0
        while m<=h:
            if arr[m]==0:
                arr[m],arr[l]=arr[l],arr[m]
                m +=1
                l +=1
            elif arr[m]==1:
                m+=1
            else:
                arr[m],arr[h]=arr[h],arr[m]
                h-=1
        return arr
def main():
    arr = [0, 1, 2, 0, 1, 2]
    obj = Solution()
    result = obj.sort012(arr)
    print("Sorted array is:", result)
if __name__ == "__main__":
    main()