from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k] = max money reaching (i, j) using exactly k neutralizations
        # Initialize with negative infinity as profits can go negative
        dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Base cases for the starting point
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0
            
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    # Find the best path coming from the Top or Left
                    best_prev = float('-inf')
                    if i > 0: best_prev = max(best_prev, dp[i-1][j][k])
                    if j > 0: best_prev = max(best_prev, dp[i][j-1][k])
                        
                    # Transition 1: Accept the cell's value (Don't neutralize)
                    if best_prev != float('-inf'):
                        dp[i][j][k] = max(dp[i][j][k], best_prev + coins[i][j])
                        
                    # Transition 2: Neutralize the current cell 
                    # (Only valid if it's a robber and we used > 0 neutralizations overall)
                    if k > 0 and coins[i][j] < 0:
                        best_prev_k1 = float('-inf')
                        if i > 0: best_prev_k1 = max(best_prev_k1, dp[i-1][j][k-1])
                        if j > 0: best_prev_k1 = max(best_prev_k1, dp[i][j-1][k-1])
                            
                        if best_prev_k1 != float('-inf'):
                            # Add 0 because the penalty is bypassed
                            dp[i][j][k] = max(dp[i][j][k], best_prev_k1) 
                            
        # The answer is the best score at the bottom-right corner across all possible 'k'
        return int(max(dp[m-1][n-1]))