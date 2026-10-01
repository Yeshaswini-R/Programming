class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}
        for word in strs:
            letters = list(word)
            letters.sort()
            key = ''.join(letters)
            if key not in h:
                h[key] = []
            h[key].append(word)
        return list(h.values())