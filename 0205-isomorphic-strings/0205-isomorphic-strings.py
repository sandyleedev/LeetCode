class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # 없는 문자면 dict 에 추가

        index1 = 0
        index2 = 0

        dict1 = {}
        dict2 = {}

        list1 = []
        list2 = []

        for char in s:
            if char not in dict1:
                dict1[char] = index1
                list1.append(index1)
                index1 += 1
            else:
                list1.append(dict1[char])
        
        for char in t:
            if char not in dict2:
                dict2[char] = index2
                list2.append(index2)
                index2 += 1
            else:
                list2.append(dict2[char])


        return list1 == list2