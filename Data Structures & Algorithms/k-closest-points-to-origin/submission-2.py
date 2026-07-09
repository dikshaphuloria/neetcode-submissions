import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        min_eud_distance = float("inf")
        hq.heapify(points)

        while points:
            x, y = hq.heappop(points)
            eud_distance = math.sqrt((x-0)**2 + (y-0)**2)
            hq.heappush(ans, [[eud_distance], [x , y]])

        res = []
        while k:
            eud, vector = hq.heappop(ans)
            res.append(vector)
            k-=1

        return res
        

            

            




        
        