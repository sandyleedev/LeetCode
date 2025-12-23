class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        cur = nums[0]

        # set prefix
        for i in range(1, len(nums)):
            res[i] = cur
            cur *= nums[i]

        # set postfix
        cur = nums[-1]
        for j in range(len(nums) - 2, -1, -1):
            res[j] *= cur
            cur *= nums[j]
        
        return res