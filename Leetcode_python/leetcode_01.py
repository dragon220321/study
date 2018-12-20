class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums[i+1:]:
                    return [i,i+1+nums[i+1:].index(temp)]

a = [1,2,4,4,9]
b = 8
test = Solution()
print(test.twoSum(a,b))