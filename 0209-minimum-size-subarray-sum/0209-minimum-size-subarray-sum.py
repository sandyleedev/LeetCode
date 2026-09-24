class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = float('inf')
        cur_sum = 0
        start = 0

        for end in range(len(nums)):
            cur_sum += nums[end]

            while cur_sum >= target:
                min_len = min(min_len, end - start + 1)
                cur_sum -= nums[start]
                start += 1
        
        return min_len if min_len != float('inf') else 0

            