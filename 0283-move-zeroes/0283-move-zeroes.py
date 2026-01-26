class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                n = n-1
            else:
                i = i+1



















        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        # return nums


        