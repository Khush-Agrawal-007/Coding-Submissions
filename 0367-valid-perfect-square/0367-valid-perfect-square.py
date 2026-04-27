class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # l,r = 1,num
        # while l<=r:
        #     mid = (l+r)//2
        #     sqr = mid*mid
        #     if sqr ==num:
        #         return True
        #     elif sqr<num:
        #         l = mid+1
        #     else:
        #         r = mid-1
        # return False

        root = int(num ** 0.5)
        return root * root == num