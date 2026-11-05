class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for i in arr1:
            status = 0
            for j in arr2:
                if abs(i - j) <= d:
                    status = 1
            if status == 0:
                count += 1
        return count