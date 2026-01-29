class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # very bad , brute force approach 
        # for i in range(0,k):
        #     last = nums.pop()
        #     nums.insert(0,last)

        # optimal approach 

        k = k%len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        