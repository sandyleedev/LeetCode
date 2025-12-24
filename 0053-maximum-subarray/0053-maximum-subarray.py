class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for n in nums:
            if currSum + n < 0:
                maxSum = max(maxSum, n)
                currSum = 0
            else:
                currSum += n
                maxSum = max(maxSum, currSum)

        return maxSum