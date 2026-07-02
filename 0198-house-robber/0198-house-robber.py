class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])

        # dp[2] = max(dp[0] + nums[2], dp[1])
        # dp[3] = max(dp[1] + nums[3], dp[2])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[len(nums) - 1]