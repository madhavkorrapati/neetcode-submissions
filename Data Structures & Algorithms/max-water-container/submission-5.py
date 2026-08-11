class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_num=0
        left=0
        right=len(heights)-1
        while left < right:
            area=min(heights[left],heights[right])*(right-left)
            if area>max_num:
                max_num=area
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_num
        
        
