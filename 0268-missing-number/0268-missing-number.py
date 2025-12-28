class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            ans += i        # sum 0 ~ n-1
            ans -= nums[i]  # subtract existing numbers

        ans += n            # sum 0 ~ n

        return ans
        