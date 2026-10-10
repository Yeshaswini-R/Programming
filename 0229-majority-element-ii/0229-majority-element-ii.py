class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        h = {}
        n = len(nums)
        ans = []
        for i in nums:
            h[i] = h.get(i,0) + 1
        for i in h:
            if h[i] > n/3:
                ans.append(i)
        return ans
