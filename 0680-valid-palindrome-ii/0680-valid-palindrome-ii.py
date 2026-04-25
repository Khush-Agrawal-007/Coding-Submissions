def palindrome(s,left,right):
    l,r = left , right
    while l<r:
        if s[l] == s[r]:
            l+=1
            r-=1
        else:
            return False 
    return True
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return(palindrome(s,l+1,r) or palindrome(s,l,r-1))
        return True