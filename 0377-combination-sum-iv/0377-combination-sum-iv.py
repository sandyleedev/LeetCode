from functools import lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # ways of making 10
        # -> dp[9] + dp[8] + dp[5]
        # -> dp[10 - 1] + dp[10 - 2] + dp[10 -5]

        # for num in nums
        # -> dp[10 - num]

        dp = {}
        dp[0] = 1
        # ...
        # dp[target]

        for i in range(1, target + 1):
            dp[i] = 0
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        return dp[target]
