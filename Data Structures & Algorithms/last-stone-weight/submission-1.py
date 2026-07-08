import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stone = []

        for n in stones:
            hq.heappush(new_stone, -n)

        x = y = 0
        while len(new_stone) > 1:
            x = -hq.heappop(new_stone)
            y = -hq.heappop(new_stone)

            if x > y:
                y = x - y
                hq.heappush(new_stone, -y)
        new_stone.append(0)
        return -new_stone[0]

            



        
        