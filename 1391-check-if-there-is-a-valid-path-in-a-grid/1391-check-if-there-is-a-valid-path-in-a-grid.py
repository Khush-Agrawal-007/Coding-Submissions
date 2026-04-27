from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        
        # Mapping street types to (row_offset, col_offset)
        moves = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        
        while queue:
            r, c = queue.popleft()
            
            if r == rows - 1 and c == cols - 1:
                return True
            
            for dr, dc in moves[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                # 1. Check bounds
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    # 2. Check if the neighbor can connect back to current (r, c)
                    # This means (r, c) must be in moves[grid[nr][nc]] relative to (nr, nc)
                    for back_dr, back_dc in moves[grid[nr][nc]]:
                        if nr + back_dr == r and nc + back_dc == c:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                            break
                            
        return False
        