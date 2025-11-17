class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # negative value
        # if curProduct is neg -> cur * n could be maximum
        # if curProduct is pos -> cur * n could be maximum
        # so we need to keep track of our so far maximum and minimum
        res = max(nums)
        cur_max = 1
        cur_min = 1

        for n in nums:
            tmp_max = cur_max
            cur_max = max(cur_max * n, cur_min * n, n)
            cur_min = min(tmp_max * n, cur_min * n, n)
            res = max(res, cur_max)
        return res
            

        