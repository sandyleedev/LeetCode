class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start = 0
        cur_sum = 0
        min_len = float('inf')

        for end in range(len(nums)):
            cur_sum += nums[end]
            while cur_sum >= target:
                min_len = min(min_len, end - start + 1)
                cur_sum -= nums[start]
                start += 1
        
        return min_len if min_len != float('inf') else 0