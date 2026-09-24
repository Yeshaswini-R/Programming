class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        h = {}
        for ch in s:
            if ch in h:
                h[ch]+=1
            else:
                h[ch]=1
        
        for ch in t:
            if ch not in h or h[ch]==0:
                return ch
            elif ch in h:
                h[ch]-=1