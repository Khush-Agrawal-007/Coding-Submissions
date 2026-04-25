class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        
        # 1. Map 2D coordinates to 1D perimeter distance
        def get_p(x, y):
            if y == 0: 
                return x
            if x == side: 
                return side + y
            if y == side: 
                return 2 * side + (side - x)
            if x == 0: 
                return 3 * side + (side - y)
                
        # Get sorted 1D coordinates
        A = sorted(get_p(x, y) for x, y in points)
        n = len(A)
        
        # Duplicate the array to simulate a circular path
        B = A + [p + 4 * side for p in A]
        
        # 2. Validation function using Binary Lifting
        def check(m):
            # next_idx[i] stores the smallest j such that B[j] - B[i] >= m
            # We use 2*n as an out-of-bounds / infinity fallback
            next_idx = [2 * n] * (2 * n + 1)
            j = 0
            for i in range(2 * n):
                while j < 2 * n and B[j] - B[i] < m:
                    j += 1
                next_idx[i] = j
            
            # Start a tracker from every original point
            curr = list(range(n))
            steps = k - 1
            jump = next_idx
            
            # Binary lift to advance exactly (k - 1) times efficiently
            while steps > 0:
                if steps % 2 == 1:
                    curr = [jump[c] for c in curr]
                steps //= 2
                if steps > 0:
                    jump = [jump[jump[x]] for x in range(2 * n + 1)]
                    
            # Check if any starting point resulted in a valid sequence of k points
            for i, c in enumerate(curr):
                # c must be within the duplicated array, and the distance
                # from the k-th point wrapping back to the start must be >= m
                if c < 2 * n and B[i] + 4 * side - B[c] >= m:
                    return True
                    
            return False

        # 3. Binary search the optimal minimum distance
        # Maximum theoretical distance for k points on a 4*side perimeter
        l, r = 1, (4 * side) // k
        ans = 1
        
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid        # mid is possible, try for a larger distance
                l = mid + 1
            else:
                r = mid - 1      # mid is too large, narrow the range down
                
        return ans