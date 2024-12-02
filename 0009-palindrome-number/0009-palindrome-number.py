class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        string_x = str(x)

        for char in string_x:
            if string_x[0] == "-":
                return False
            elif len(string_x) != 1 and string_x[len(string_x) - 1] == "0":
                return False

        reversed_x = string_x[::-1]
        return string_x == reversed_x