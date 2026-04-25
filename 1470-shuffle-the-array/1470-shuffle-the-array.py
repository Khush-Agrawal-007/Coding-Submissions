class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0
        r = n
        no = []
        for i in range(n):
            no.append(nums[l])
            no.append(nums[r])
            l+=1
            r+=1
        return no
            