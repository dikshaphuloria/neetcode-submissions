import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]

        hq.heapify(stones)

        while len(stones) > 1:
            x = -hq.heappop(stones)
            y = -hq.heappop(stones)

            if x > y:
                hq.heappush(stones, y-x)

        stones.append(0)
        return stones[0]*(-1)
            



        
        