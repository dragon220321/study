class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

test = Solution()
a = 1323
print(test.isPalindrome(a))