import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value_dict = Counter(nums)
        heap = []

        for key, val in value_dict.items():
            hq.heappush(heap, (-val, key))

        res = []
        while k:
            val, key = hq.heappop(heap)
            res.append(key)
            k-=1

        return res

        

        