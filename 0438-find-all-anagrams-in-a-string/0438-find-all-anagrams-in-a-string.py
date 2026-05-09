from typing import List                 # List type hint use karne ke liye import
from collections import Counter          # Counter frequency/hashmap count banane ke liye import

class Solution:                          # LeetCode ke required class ka start
    def findAnagrams(self, s: str, p: str) -> List[int]:   # Function jo anagram starting indexes return karega
        n = len(s)                      # s string ki total length store karo
        k = len(p)                      # p string ki length store karo, yani window size

        if k > n:                       # Agar p bada hai s se, to anagram possible nahi
            return []                   # Empty list return karo

        ans = []                        # Final answer list, jisme indexes store honge
        p_count = Counter(p)            # p ke characters ka frequency hashmap banao
        window = Counter(s[:k])         # s ke first k characters ka frequency hashmap banao

        if window == p_count:           # Check karo first window p ka anagram hai ya nahi
            ans.append(0)               # Agar haan, starting index 0 answer me add karo

        for i in range(k, n):           # k index se lekar end tak window slide karo
            left_char = s[i - k]        # Ye character current window se bahar ja raha hai
            right_char = s[i]           # Ye character current window me enter kar raha hai

            window[left_char] -= 1      # Bahar jaane wale character ka count 1 kam karo

            if window[left_char] == 0:  # Agar us character ka count 0 ho gaya
                del window[left_char]   # To us character ko hashmap se remove kar do

            window[right_char] += 1     # Naye character ka count window me 1 badhao

            if window == p_count:       # Check karo current window p ka anagram hai ya nahi
                ans.append(i - k + 1)   # Agar haan, current window ka starting index add karo

        return ans                      # Saare valid starting indexes return karo