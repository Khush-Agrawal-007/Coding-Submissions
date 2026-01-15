class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Sort citations in descending order (largest to smallest)
        citations.sort(reverse=True)
        
        # Iterate through the sorted list
        for i, c in enumerate(citations):
            # 'i' is the index (0, 1, 2...), so 'i + 1' is the count of papers (1, 2, 3...)
            # We are looking for the cutoff where citations (c) drop below the paper count (i + 1)
            if c < i + 1:
                return i
        
        # If the loop completes, it means every single paper has at least as many 
        # citations as the total count of papers (e.g., [100, 99, 98] -> length 3).
        return len(citations)