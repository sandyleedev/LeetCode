class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = nums[0]
        currMax = 1
        currMin = 1

        for n in nums:
            tmp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(tmp, currMin * n, n)
            maxP = max(maxP, currMax)
        
        return maxP