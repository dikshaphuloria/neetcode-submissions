class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time,tweetId])
        self.time+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        
        self.followMap[userId].add(userId)
        for key in self.followMap[userId]:
            for i in range(len(self.tweetMap[key])):
                heapq.heappush_max(heap, self.tweetMap[key][i])

        l = len(heap) if len(heap) < 10 else 10
        res = [-1]*l
        for i in range(l):
            res[i] = heapq.heappop_max(heap)[1]
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
