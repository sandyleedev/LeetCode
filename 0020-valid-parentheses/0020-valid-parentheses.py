class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        open_p = ["(", "{", "["]
        p_dict = {")": "(", "}": "{", "]": "["}

        for p in s:
            if p in open_p:
                stack.append(p)
            else:
                if not stack or p_dict[p] != stack[-1]:
                    return False
                stack.pop()
        
        return not stack