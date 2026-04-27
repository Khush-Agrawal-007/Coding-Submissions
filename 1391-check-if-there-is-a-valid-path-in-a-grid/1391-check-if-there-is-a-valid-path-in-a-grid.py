class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        # Define the doors for each pipe type
        # Format: Type: { (dr, dc) } where (dr, dc) is a valid exit direction
        exits = {
            1: {(0, -1), (0, 1)},    # Left, Right
            2: {(-1, 0), (1, 0)},    # Top, Bottom
            3: {(0, -1), (1, 0)},    # Left, Bottom
            4: {(0, 1), (1, 0)},     # Right, Bottom
            5: {(0, -1), (-1, 0)},   # Left, Top
            6: {(0, 1), (-1, 0)}     # Right, Top
        }
        
        def dfs(r, c):
            # If we reached the bottom-right corner, we found a path!
            if r == rows - 1 and c == cols - 1:
                return True
            
            visited.add((r, c))
            
            # Look at all valid exits for the current pipe
            for dr, dc in exits[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                # 1. Check if the next cell is on the board and unvisited
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    
                    # 2. Check if the next cell has an entrance matching our exit
                    # If we moved (dr, dc), the next cell must have an exit going exactly the opposite way (-dr, -dc) to connect.
                    if (-dr, -dc) in exits[grid[nr][nc]]:
                        if dfs(nr, nc):
                            return True
                            
            return False
            
        return dfs(0, 0)