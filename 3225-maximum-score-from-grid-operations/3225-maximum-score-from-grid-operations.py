class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # prefix[col][row] allows us to get the sum of any vertical segment in O(1) time.
        # prefix[col][b] - prefix[col][a] = sum of grid[a...b-1][col]
        prefix = [[0] * (n + 1) for _ in range(n)]
        for col in range(n):
            for row in range(n):
                prefix[col][row + 1] = prefix[col][row] + grid[row][col]
                
        # DP states for the previous column (column 0 initialization)
        # Base case: Column 0 has no left neighbor, so its initial score is 0.
        pick = [0] * (n + 1)
        skip = [0] * (n + 1)
        
        # Process from column 1 to n - 1
        for col in range(1, n):
            next_pick = [0] * (n + 1)
            next_skip = [0] * (n + 1)
            
            for curr in range(n + 1):
                for prev in range(n + 1):
                    
                    if curr > prev:
                        # Col `col` is taller. It scores the white cells in col `col-1`.
                        score = prefix[col - 1][curr] - prefix[col - 1][prev]
                        
                        # Use skip[prev] to ensure we don't double count cells col-2 might have scored
                        val = skip[prev] + score
                        if val > next_pick[curr]: next_pick[curr] = val
                        if val > next_skip[curr]: next_skip[curr] = val
                        
                    else:
                        # Col `col-1` is taller. It scores the white cells in col `col`.
                        score = prefix[col][prev] - prefix[col][curr]
                        
                        # Safe to use pick[prev] because col-1's left dependencies are isolated
                        val_pick = pick[prev] + score
                        if val_pick > next_pick[curr]: next_pick[curr] = val_pick
                        
                        # For skip, we intentionally do NOT add the score (deferring it)
                        val_skip = pick[prev]
                        if val_skip > next_skip[curr]: next_skip[curr] = val_skip
            
            # Move to the next column
            pick = next_pick
            skip = next_skip
            
        return max(pick)