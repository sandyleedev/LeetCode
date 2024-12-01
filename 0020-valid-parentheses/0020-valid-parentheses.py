class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping: # 닫는 괄호일 경우
                if not stack:
                    return False
                else:
                    top_element = stack.pop()
                    if mapping[char] != top_element:
                        return False
            else:
                stack.append(char)

        
        return not stack
            