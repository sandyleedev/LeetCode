class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        s = ""
        count = 1

        for i in range(1, len(chars)):
            if chars[i - 1] != chars[i]:
                s += chars[i - 1]
                if count > 1:
                    s += str(count)
                    count = 1       # reset
            else:
                count += 1

            if i == len(chars) - 1:
                s += chars[i]
                if count > 1:
                    s += str(count)

        for i, c in enumerate(s):
            chars[i] = c

        return len(s)
