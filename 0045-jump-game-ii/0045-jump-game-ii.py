class Solution:
    def jump(self, nums: list[int]) -> int:
        current_end = 0
        jumps = 0
        farthest = 0

        for i in range(len(nums)):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                if i == len(nums) - 1:
                    break
                
                jumps += 1
                current_end = farthest
        
        return jumps