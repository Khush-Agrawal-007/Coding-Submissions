class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])
        
        # Step 1: Apply Gravity (Move stones to the right)
        for r in range(rows):
            # Pointer for the rightmost available empty cell
            empty_slot = cols - 1
            
            for c in range(cols - 1, -1, -1):
                if box[r][c] == '#':
                    # Move stone to the empty slot
                    box[r][c], box[r][empty_slot] = box[r][empty_slot], box[r][c]
                    empty_slot -= 1
                elif box[r][c] == '*':
                    # Obstacle resets the empty slot to the left of it
                    empty_slot = c - 1
        
        # Step 2: Rotate 90 Degrees Clockwise
        # New dimensions: cols x rows
        res = [['' for _ in range(rows)] for _ in range(cols)]
        
        for r in range(rows):
            for c in range(cols):
                res[c][rows - 1 - r] = box[r][c]
                
        return res