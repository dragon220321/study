class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic_roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        for i in range(len(s)):
            if i != len(s)-1 and dic_roman[s[i]] < dic_roman[s[i+1]]:
                ans -= dic_roman[s[i]]
            else:
                ans += dic_roman[s[i]]
        return ans

test = Solution()
a = "LVIII"
print(test.romanToInt(a))