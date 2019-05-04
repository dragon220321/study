class Solution:
    def removeDuplicates(self, nums) -> int:       
        if len(nums) == 0:
            return 0
        flag = 0
        for i in range(len(nums)):
            if nums[flag] != nums[i]:
                flag  += 1
                nums[flag] = nums[i]
        return flag + 1

sln = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
n = sln.removeDuplicates(nums)
print(n)


