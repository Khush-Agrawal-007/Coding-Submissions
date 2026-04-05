class Solution(object):
    def longestCommonPrefix(self, strs):
        # if not strs:
        #     return "null"

        # prefix = strs[0]
        # for word in strs[1:]:
        #     j = 0
        #     while j < len(prefix) and j < len(word) and prefix[j] == word[j]:
        #         j += 1
        #     prefix = prefix[:j]
        #     if not prefix:
        #         return ""
        # return prefix
            


        # sort then see 1st and last string only and find common from both only
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        while i< len(first)and i <len(last) and first[i] == last[i]:
            i+=1
        return first[:i]