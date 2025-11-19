class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer
        # (r - l) * min(height[r], height[l])
        # maxArea = 0

        maxArea = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxArea = max(area, maxArea)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea