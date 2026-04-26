class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        # Directions: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(r, c, parent_r, parent_c, target_char):
            # If we reach a visited node that isn't the parent, we found a cycle
            if (r, c) in visited:
                return True
            
            # Mark current cell as visited
            visited.add((r, c))
            
            # Explore all 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and character match
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == target_char:
                    # Skip the parent we just came from
                    if nr == parent_r and nc == parent_c:
                        continue
                    
                    # Recursively visit neighbors
                    if dfs(nr, nc, r, c, target_char):
                        return True
                        
            return False

        # Iterate through every cell to handle disconnected graph components
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    # Start DFS with no parent (-1, -1)
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True
                        
        return False