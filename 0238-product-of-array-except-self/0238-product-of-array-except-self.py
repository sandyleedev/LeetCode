class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # set prefix
        cur = 1
        for i in range(len(nums)):
            res[i] = cur
            cur *= nums[i]

        # set postfix
        cur = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= cur
            cur *= nums[j]
        
        return res