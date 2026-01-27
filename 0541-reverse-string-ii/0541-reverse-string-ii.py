class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
        
        ####  OPtimal APPROACH
    #     class Solution(object):
    # def reverseStr(self, s, k):
    #     res = ""
    #     i = 0
    #     while (i<len(s)):
    #         m = s[i:k+i]
    #         res += m[::-1]
    #         res += s[(k+i):((2*k)+i)]
    #         i = 2*k+i
    #     return res