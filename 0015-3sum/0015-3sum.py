class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        result = []
        for i in range(len(nums)):
            # skip duplicate first elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        
                elif s < target:
                    l += 1
                else:
                    r -= 1
        
        return result