import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            hq.heappush(heap, n)

            if len(heap) > k:
                hq.heappop(heap)

        return heap[0]
        