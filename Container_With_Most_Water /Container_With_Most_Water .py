class Solution:
    def maxArea(self, height):
        Max = 0
        for i in range(len(height)):
            for j in range(i,len(height)):
                Max = max(Max, min(height[i],height[j])*(j-i))
        return Max

        
