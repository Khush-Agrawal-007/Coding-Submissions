# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r = 1,n
        while l<r:
            mid = (l+r)//2
            bad = isBadVersion(mid)
            if bad == True:
                r = mid
            elif bad == False:
                l = mid +1
        return l