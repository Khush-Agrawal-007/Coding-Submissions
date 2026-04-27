class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        freq = {0:1}
        curr_sum = 0
        for i in nums:
            curr_sum +=i
            rem = curr_sum % k
            
            count +=freq.get(rem,0)
            freq[rem] = freq.get(rem,0)+1
        
        return count 