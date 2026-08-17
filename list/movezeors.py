def movezeroa(nums):
          n=len(nums)
          left=0
          right=0
          while right<n:
              if nums[left]==0 and nums[right]!=0:
                  nums[left],nums[right]=nums[right],nums[left]
              if nums[left]!=0:
                  left+=1
              right+=1
              
          return nums
