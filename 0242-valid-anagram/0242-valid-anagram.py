class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.lower()
        t.lower()
        if len(s)!=len(t):
            return False
        freq = [0]*26
        s = s.replace(' ','')
        t = t.replace(' ','')
        for ch in s:
            freq[ord(ch)-ord('a')] +=1
        for ch in t:
            freq[ord(ch)-ord('a')] -=1
        for i in freq:
            if i!=0:
                return False
        return True
