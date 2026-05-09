from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        
        for layer in range(layers):
            # Define the bounding box for the current layer
            top, bottom = layer, m - 1 - layer
            left, right = layer, n - 1 - layer
            
            # Extract elements in a clockwise perimeter walk
            elements = []
            
            # Top row (left to right)
            for j in range(left, right): 
                elements.append(grid[top][j])
            # Right column (top to bottom)
            for i in range(top, bottom): 
                elements.append(grid[i][right])
            # Bottom row (right to left)
            for j in range(right, left, -1): 
                elements.append(grid[bottom][j])
            # Left column (bottom to top)
            for i in range(bottom, top, -1): 
                elements.append(grid[i][left])
                
            # Calculate effective rotation steps to avoid redundant cycles
            L = len(elements)
            steps = k % L  
            idx = 0
            
            # Write the elements back in the same clockwise path, 
            # but shifted by 'steps' to achieve the counter-clockwise rotation
            for j in range(left, right):
                grid[top][j] = elements[(idx + steps) % L]
                idx += 1
            for i in range(top, bottom):
                grid[i][right] = elements[(idx + steps) % L]
                idx += 1
            for j in range(right, left, -1):
                grid[bottom][j] = elements[(idx + steps) % L]
                idx += 1
            for i in range(bottom, top, -1):
                grid[i][left] = elements[(idx + steps) % L]
                idx += 1
                
        return grid