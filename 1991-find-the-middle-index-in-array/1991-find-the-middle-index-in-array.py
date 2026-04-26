class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # prefix = [0]*len(nums)
        # sum = 0
        # prefix[0] = nums[0]
        # for i in range(1,len(nums)-1):
        #     prefix[i] = sum + nums[i]
        #     sum = prefix[i]
        # if prefix[len(nums)-1] == 0:
        #     return -1
        total = sum(nums)
        l_sum = 0

        for i in range(len(nums)):
            r_sum = total -l_sum - nums[i]
        
            if l_sum == r_sum:
                return i
            l_sum = l_sum + nums[i]
        return -1

        