def removeElement( nums, val):
        left,right=0,len(nums)-1
        while left<=right:
            if nums[left]==val and nums[right]!=val:
                nums[left],nums[right]=nums[right],nums[left]
                right-=1
                left+=1
            if nums[left]!=val:
                left+=1
            if nums[right]==val:
                right-=1
        return left