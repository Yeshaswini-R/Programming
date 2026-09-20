class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i,ch in enumerate(s,start=1):
            val = ord(ch)-ord('a')
            ans += (26-val)*i
        return ans
        