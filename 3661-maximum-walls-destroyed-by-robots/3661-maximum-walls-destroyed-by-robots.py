from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        # Bundle and sort robots by their physical position left-to-right
        arr = sorted(zip(robots, distance))
        P = [p for p, d in arr]
        D = [d for p, d in arr]
        
        # Observation 1: Count and remove walls exactly at robot positions
        robot_positions = set(P)
        base_ans = 0
        filtered_walls = []
        
        for w in walls:
            if w in robot_positions:
                base_ans += 1
            else:
                filtered_walls.append(w)
                
        filtered_walls.sort()
        
        # Helper to fast-count remaining walls within an inclusive range [left, right]
        def count_walls(left: int, right: int) -> int:
            if left > right:
                return 0
            idx_l = bisect_left(filtered_walls, left)
            idx_r = bisect_right(filtered_walls, right)
            return max(0, idx_r - idx_l)
            
        # dp[i][0] -> Max walls up to robot i if it fires Left
        # dp[i][1] -> Max walls up to robot i if it fires Right
        dp = [[0, 0] for _ in range(n)]
        
        # Base case: Zone 0 (space before the very first robot)
        dp[0][0] = count_walls(P[0] - D[0], P[0])
        dp[0][1] = 0 # Firing right doesn't cover anything before P[0]
        
        for i in range(1, n):
            # Evaluate the gap between P[i-1] and P[i]
            
            # --- Calculating dp[i][0] (Robot i fires Left) ---
            reach_L = max(P[i] - D[i], P[i-1])
            walls_LL = count_walls(reach_L, P[i])
            
            reach_R = min(P[i-1] + D[i-1], P[i])
            if reach_R < reach_L:
                # Bullets don't overlap in the middle
                walls_RL = count_walls(P[i-1], reach_R) + count_walls(reach_L, P[i])
            else:
                # Bullets overlap, safely covering the entire space between them
                walls_RL = count_walls(P[i-1], P[i])
                
            dp[i][0] = max(dp[i-1][0] + walls_LL, dp[i-1][1] + walls_RL)
            
            # --- Calculating dp[i][1] (Robot i fires Right) ---
            walls_LR = 0 # Neither bullet shoots into the gap
            walls_RR = count_walls(P[i-1], reach_R)
            
            dp[i][1] = max(dp[i-1][0] + walls_LR, dp[i-1][1] + walls_RR)
            
        # Final check: Calculate the walls destroyed after the very last robot (Zone N)
        ans = base_ans + max(
            dp[n-1][0], 
            dp[n-1][1] + count_walls(P[n-1], P[n-1] + D[n-1])
        )
        
        return ans