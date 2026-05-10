from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Initialize DP array with -1 (unreachable)
        dp = [-1] * n
        dp[0] = 0  # 0 jumps to reach the starting point
        
        # Iterate through every possible starting index for a jump
        for i in range(n):
            # If we can't reach index i, we can't jump from it
            if dp[i] == -1:
                continue
                
            # Check all possible landing indices after i
            for j in range(i + 1, n):
                # If the jump condition is satisfied
                if abs(nums[j] - nums[i]) <= target:
                    # Update dp[j] with the maximum jumps to get there
                    dp[j] = max(dp[j], dp[i] + 1)
                    
        return dp[-1]