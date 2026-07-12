import heapq as hq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [cnt for cnt in count.values()]
        hq.heapify_max(maxHeap)
        
        time = 0
        q = deque()

        while maxHeap or q:
            time+=1

            if maxHeap:
                cnt = hq.heappop_max(maxHeap) - 1
                if cnt:
                    q.append([cnt, time+n])
                
            if q and q[0][1] == time:
                hq.heappush_max(maxHeap, q.popleft()[0])

        return time









        

        