class Solution:
    def reverse(self, x: int) -> int:
        s = 1 # pos

        if x < 0:
            s = 0 # neg
            x = x * -1

        rev = 0
        while x != 0:
            dig = x % 10
            x = x // 10
            rev = rev * 10 + dig 

        if rev > 2 ** 31 - 1:
            return 0
        
        return rev if s==1 else rev * -1