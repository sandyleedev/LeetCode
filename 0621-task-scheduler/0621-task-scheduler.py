from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = list(freq.values()).count(max_freq)

        part_count = max_freq - 1
        part_len = n + 1
        slots = part_count * part_len + max_count

        return max(slots, len(tasks))