class Solution(object):
    def removeDuplicates(self, nums):
        unique = sorted(set(nums))   # your logic
        
        for i in range(len(unique)):
            nums[i] = unique[i]     # write back into original array
        
        return len(unique)
        # if not nums:
        #     return 0
        # l = 0
        # for r in range(1, len(nums)):
        #     if nums[r] != nums[l]:
        #         l += 1
        #         nums[l] = nums[r]
        
        # return l + 1









