class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return [max(nums)]

        result = []
        
        left = 0

        for right in range(k, len(nums)+1):

            result.append(max(nums[left:right]))
            left+=1

        return result

        

        