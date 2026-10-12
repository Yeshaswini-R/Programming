class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        k = len(part)
        while part in s:
            i=0
            while i <= len(s) - len(part):
                if s[i:i+k] == part:
                    s = s[:i] + s[i+k:]
                    break
                i=i+1
        return s