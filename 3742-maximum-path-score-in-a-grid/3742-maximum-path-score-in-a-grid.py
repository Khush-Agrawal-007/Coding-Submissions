from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        NEG = -10**9

        # prev[j][cost] = max score to reach column j in previous row using cost
        prev = [[NEG] * (k + 1) for _ in range(n)]

        for i in range(m):
            curr = [[NEG] * (k + 1) for _ in range(n)]

            for j in range(n):
                for cost in range(k + 1):

                    # Starting cell
                    if i == 0 and j == 0:
                        curr[j][0] = 0
                        continue

                    cell_score = grid[i][j]
                    cell_cost = 0 if grid[i][j] == 0 else 1

                    if cost < cell_cost:
                        continue

                    prev_cost = cost - cell_cost
                    best = NEG

                    # Coming from top
                    if i > 0:
                        best = max(best, prev[j][prev_cost])

                    # Coming from left
                    if j > 0:
                        best = max(best, curr[j - 1][prev_cost])

                    if best != NEG:
                        curr[j][cost] = best + cell_score

            prev = curr

        ans = max(prev[n - 1])
        return ans if ans != NEG else -1