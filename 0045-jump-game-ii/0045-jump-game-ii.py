class Solution:
    def jump(self, nums: list[int]) -> int:
        current_end = 0
        res = 0
        farthest = 0

        for i in range(len(nums)):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                if i == len(nums) - 1:
                    break

                res += 1
                current_end = farthest
        
        return res