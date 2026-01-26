class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0 
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k 





























        # # 'k' serves as the writer pointer. 
        # # It marks the index where the next valid element should go.
        # k = 0
        
        # # 'i' serves as the reader pointer.
        # for i in range(len(nums)):
        #     # If the current element is NOT the value we want to remove...
        #     if nums[i] != val:
        #         # ...we write it to the 'k' position
        #         nums[k] = nums[i]
        #         # ...and move the writer forward
        #         k += 1
                
        # # Return the number of valid elements
        # return k