class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)
        def get_max_rob(houses):
            rob1, rob2 = 0, 0
            for h in houses:
                temp = max(rob1 + h, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(get_max_rob(nums[1:]), get_max_rob(nums[:-1]))