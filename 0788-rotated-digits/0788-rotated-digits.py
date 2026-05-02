class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        
        # Define digit sets for clarity
        # Invalid: 3, 4, 7
        # Neutral (stay the same): 0, 1, 8
        # Rotating (change the value): 2, 5, 6, 9
        
        for i in range(1, n + 1):
            s = str(i)
            
            # 1. Check for invalid digits
            if '3' in s or '4' in s or '7' in s:
                continue
            
            # 2. Check if the number actually changes
            # It must contain at least one of 2, 5, 6, or 9
            if any(d in s for d in '2569'):
                count += 1
                
        return count