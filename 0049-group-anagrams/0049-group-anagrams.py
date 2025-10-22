class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        result = []
        word_dict = {}          # key - sorted word, value - list of anagrams

        if len(strs) == 1:
            result.append([strs[0]])
            return result
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in word_dict:
                word_dict[sorted_word].append(word)
            else:
                word_dict[sorted_word] = [word]

        for each in word_dict.values():
            result.append(each)
        
        return result