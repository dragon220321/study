class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            min_length = len(strs[0])
            for i in range(len(strs)):
                if min_length > len(strs[i]):
                    min_length = len(strs[i])
            same_str = ""
            flag = 0
            for j in range(min_length):
                if flag == 1:
                    break
                for k in range(1,len(strs)):
                    if strs[0][j] != strs[k][j]:
                        flag = 1
                        break
                    elif k == len(strs) - 1:
                        same_str += strs[0][j]
            return same_str