class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ### Sort_2
        n = len(nums)
        xor = n
        for i in range(n):
            xor = xor^i^nums[i]
        return xor
        ### Sort_1
        # nums.sort()
        # for i in range(len(nums)):
        #     if(i!=nums[i]):
        #         return(i)
        # return(len(nums))