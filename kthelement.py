class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        arr.sort()
        set(arr)
        for i in range(len(arr)):
            if i==k-1:
                return arr[i]
                break
def main():
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    obj = Solution()
    result = obj.kthSmallest(arr, k)
    print("The", k, "th smallest element is:", result)
if __name__ == "__main__":
    main()