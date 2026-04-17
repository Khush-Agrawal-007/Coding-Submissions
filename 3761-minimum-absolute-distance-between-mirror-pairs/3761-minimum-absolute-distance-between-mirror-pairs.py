class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        lookup = {}
        min_dist = float('inf')
        
        for i, num in enumerate(nums):
            # If the current number resolves a previously stored reversed value
            if num in lookup:
                min_dist = min(min_dist, i - lookup[num])
            
            # Calculate the reverse of the current number (handles trailing zeros naturally)
            rev_num = 0
            temp = num
            while temp > 0:
                rev_num = rev_num * 10 + (temp % 10)
                temp //= 10
            
            # Store the current index waiting for its reversed counterpart
            lookup[rev_num] = i
            
        return min_dist if min_dist != float('inf') else -1