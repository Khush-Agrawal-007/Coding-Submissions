from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        
        for q in queries:
            for d in dictionary:
                diff_count = 0
                # Compare characters one by one
                for i in range(len(q)):
                    if q[i] != d[i]:
                        diff_count += 1
                    # Early optimization: if diff exceeds 2, stop checking this dictionary word
                    if diff_count > 2:
                        break
                
                # If we found a valid match, add to result and stop checking dictionary words
                if diff_count <= 2:
                    result.append(q)
                    break
                    
        return result