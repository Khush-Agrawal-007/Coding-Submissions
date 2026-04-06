class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## BASIC IMPLEMENTATION OF XOR GATE  ' ^ '
        result = 0
        for i in nums:
            result = i ^ result
        return result