import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

        hq.heapify(self.nums)
        while len(self.nums) > k:
            hq.heappop(self.nums)
        
    def add(self, val: int) -> int:
        hq.heappush(self.nums, val)

        while len(self.nums) > self.k:
            hq.heappop(self.nums)

        return self.nums[0]
        
