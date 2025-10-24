class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # left, right index
        left = 0
        ans = 0
        used = {}           # key - char, value - index

        for right, char in enumerate(s):
            if char in used and used[char] >= left:
                left = used[char] + 1
            used[char] = right
            ans = max(ans, right - left + 1)
        
        return ans

