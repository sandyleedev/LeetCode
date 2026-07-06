class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)

        def helper(houses):
            prev2, prev1 = 0, 0
            for h in houses:
                temp = max(prev2 + h, prev1)
                prev2 = prev1
                prev1 = temp
            return prev1
        
        return max(helper(nums[1:]), helper(nums[:-1]))