## OPTIMAL SOLUTION using Prefix Sum 
'''do preprocessing where we define num
minus preprocessing till i then we get i till j '''
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = [0]*len(nums)
        self.arr[0]=nums[0]
        for i in range(1,len(self.arr)):
            self.arr[i] = self.arr[i-1] + nums[i]        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.arr[right]
        else:
            return self.arr[right]-self.arr[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

#  Brute FORCE 

# class NumArray(object):

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums
#     def sumRange(self, left, right):
#         """
#         :type left: int
#         :type right: int
#         :rtype: int
#         """
#         sum = 0
#         for i in range(left,right+1):
#             sum = sum + self.nums[i]
            
#         return sum
        