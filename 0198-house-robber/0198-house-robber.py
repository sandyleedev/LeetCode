class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n-2 -> dp[n-2]
        # n-1 -> dp[n-1]
        # n까지 훔쳤을때의 최댓값 -> dp[n-2] + n이거나 // dp[n-1] 중 max 찾기
        n = len(nums)
        if n == 0:
            return 0
        
        if n == 1:
            return nums[0]

        dp = [0] * (n + 1)

        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        for i in range(3, n + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

        return dp[n]