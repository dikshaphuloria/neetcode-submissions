import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq.heapify(nums)

        while len(nums) > k:
            hq.heappop(nums)

        return hq.heappop(nums)
        