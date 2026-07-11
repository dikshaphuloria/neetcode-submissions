import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq.heapify_max(stones)

        while len(stones) > 1:
            x = hq.heappop_max(stones)
            y = hq.heappop_max(stones)
            
            if x > y:
                hq.heappush_max(stones, x-y)

        stones.append(0)
        return stones[0]



        
        