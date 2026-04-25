class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s=s.strip()
        i=len(s)-1
        while i>=0 and s[i]!=" ":
            count+=1
            i-=1
        return count

