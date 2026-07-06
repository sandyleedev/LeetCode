class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)
        
        def helper(start, end):
            prev2, prev1 = 0, 0

            for i in range(start, end + 1):
                temp = max(prev2 + nums[i], prev1)
                prev2 = prev1
                prev1 = temp
            
            return prev1
        
        return max(helper(0, len(nums) - 2), helper(1, len(nums) - 1))