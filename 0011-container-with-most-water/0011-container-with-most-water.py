class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        water=0
        while left<right:
            h=min(height[left],height[right])
            w=right-left
            total=h*w
            water=max(water,total)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return water