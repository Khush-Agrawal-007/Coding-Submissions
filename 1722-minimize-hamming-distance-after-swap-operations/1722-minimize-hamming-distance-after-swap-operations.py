from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        
    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i: int, j: int):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        
        # Step 1: Group indices into connected components
        for u, v in allowedSwaps:
            uf.union(u, v)
            
        # Step 2: Store the frequencies of elements in each connected component
        # components maps -> root_index : { value : frequency }
        components = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            root = uf.find(i)
            components[root][source[i]] += 1
            
        # Step 3: Greedily match source elements to target elements
        hamming_distance = 0
        for i in range(n):
            root = uf.find(i)
            
            # If the target value exists in this component's pool, we can match it
            if components[root][target[i]] > 0:
                components[root][target[i]] -= 1
            # Otherwise, it's a mismatch
            else:
                hamming_distance += 1
                
        return hamming_distance