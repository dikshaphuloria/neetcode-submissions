class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = float('-inf')
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left

            if heights[left] > heights[right]:
                max_water = max(heights[right]*width, max_water)
                right-=1
            
            else:
                max_water = max(heights[left]*width, max_water)
                left+=1
        
        return max_water


        

        