class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        pre = strs[0]
        for i in range(1, len(strs)):
            while pre and not strs[i].startswith(pre):
                pre = pre[:-1]
            if not pre:
                return ""
        return pre