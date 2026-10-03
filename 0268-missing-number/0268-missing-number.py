class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        xorAll=0
        xorNums=0
        for i in range(n+1):
            xorAll^=i
        for i in nums:
            xorNums^=i
        return xorAll^xorNums