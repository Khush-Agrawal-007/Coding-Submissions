import collections
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        max_val = max(nums)
        if max_val < 2:
            # If no primes exist, we just walk sequentially to the end
            return n - 1

        # 1. Sieve for Smallest Prime Factor (SPF) up to max_val
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i
                        
        # 2. Precompute Prime Teleportation Buckets
        prime_buckets = collections.defaultdict(list)
        for i, num in enumerate(nums):
            x = num
            while x > 1:
                p = spf[x]
                prime_buckets[p].append(i)
                # Divide out all occurrences of this prime factor
                while x % p == 0:
                    x //= p
                    
        # 3. Breadth-First Search (BFS)
        queue = collections.deque([(0, 0)]) # Stores (current_index, jumps)
        visited = [False] * n
        visited[0] = True
        
        while queue:
            idx, dist = queue.popleft()
            
            # --- Move A: Adjacent Steps ---
            for nxt in (idx - 1, idx + 1):
                if 0 <= nxt < n and not visited[nxt]:
                    if nxt == n - 1:
                        return dist + 1
                    visited[nxt] = True
                    queue.append((nxt, dist + 1))
                    
            # --- Move B: Prime Teleportation ---
            val = nums[idx]
            
            # Check if the current value is strictly a prime number itself
            if val >= 2 and spf[val] == val:
                if val in prime_buckets:
                    # Queue all teleportation targets
                    for nxt in prime_buckets[val]:
                        if not visited[nxt]:
                            if nxt == n - 1:
                                return dist + 1
                            visited[nxt] = True
                            queue.append((nxt, dist + 1))
                            
                    # TLE SAVER: Delete the bucket after using it. 
                    # Once a prime's targets are queued, they have received their shortest path.
                    del prime_buckets[val]
                    
        return -1