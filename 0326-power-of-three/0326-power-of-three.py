class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # i = 0
        # if n ==0 :return False
        # for i in range(n):
        #     if 3**i == n :
        #         return True
        # return False
        return n > 0 and 1162261467 % n == 0