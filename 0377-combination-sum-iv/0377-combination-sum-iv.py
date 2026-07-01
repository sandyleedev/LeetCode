from functools import lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        dp[0] = 1

        for i in range(1, target + 1):
            dp[i] = 0
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        return dp[target]