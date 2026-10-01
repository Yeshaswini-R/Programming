class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h ={}
        for word in strs:
            lword = list(word)
            lword.sort()
            sword = ''.join(lword)
            if sword in h:
                h[sword].append(word)
            else:
                h[sword] = [word]
        result = []
        for key in h:
            result.append(h[key])
        return result
