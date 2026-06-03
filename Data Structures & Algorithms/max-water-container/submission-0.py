class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        a = 0
        while l<r:
            a = max(a,min(heights[l],heights[r])*(r-l))
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
        return a
        