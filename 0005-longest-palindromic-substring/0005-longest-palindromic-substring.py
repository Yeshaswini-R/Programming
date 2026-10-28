class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 0

        for i in range(len(s)):
            # Odd-length palindrome
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > max_len:
                start = left + 1
                max_len = right - left - 1

            # Even-length palindrome
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > max_len:
                start = left + 1
                max_len = right - left - 1

        return s[start:start + max_len]