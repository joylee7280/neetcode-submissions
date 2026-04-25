class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target-nums[i]) in nums[i+1:]:
                if nums[i] == target-nums[i]:
                    pos = nums.index(target-nums[i],nums.index(target-nums[i])+1)
                    return([i,pos])
                else:
                    pos = nums.index(target-nums[i])
                return([i,pos])
