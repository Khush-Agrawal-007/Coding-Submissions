class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # 1. Simulate the queries
        for li, ri, ki, vi in queries:
            # range(start, stop, step) is perfect for this task
            for idx in range(li, ri + 1, ki):
                nums[idx] = (nums[idx] * vi) % MOD
                
        # 2. Compute the bitwise XOR of the final array
        final_xor = 0
        for num in nums:
            final_xor ^= num
            
        return final_xor