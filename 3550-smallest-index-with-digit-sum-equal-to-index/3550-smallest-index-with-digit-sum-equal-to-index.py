class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,val in enumerate(nums):
            sum=0
            while val>0:
                digit=val%10
                val=val//10
                sum= sum + digit
            if sum==i:
                return i
        return -1