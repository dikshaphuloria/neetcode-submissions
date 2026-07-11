import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            eud_dist = x*x + y*y
            hq.heappush(heap, [-eud_dist, x, y])

            while len(heap) > k:
                hq.heappop(heap)

        return [[x,y] for _,x,y in heap]



        