class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # n = len(nums)
        # while i < n:
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        #         n = n-1
        #     else:
        #         i = i+1

        ## TWO POINTER APPROACH 
        left = 0
        for right in range(len(nums)):
            if nums[right]!=0 :
                nums[left],nums[right] = nums[right],nums[left]
                left +=1     