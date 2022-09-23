class Twitter:

    def __init__(self):
        self.tweets = collections.defaultdict(list)
        self.feed = collections.defaultdict(list)
        self.time = 0
        self.following = collections.defaultdict(set)
        self.followers = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followers[userId].add(userId)
        self.following[userId].add(userId)
        
        tweetTuple = (self.time, tweetId, userId)
        self.tweets[userId].append((self.time, tweetId, userId))
        self.time -= 1
        for user in self.followers[userId]:
            heapq.heappush(self.feed[user], tweetTuple)

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        tweetSet = {}
        
        feed = self.feed[userId]
        following = self.following[userId]
        while len(tweetSet) < 10 and feed:
            time, tweetId, userId = heapq.heappop(feed)
            if userId in following and tweetId not in tweetSet:
                ans.append((time, tweetId, userId))
                tweetSet[tweetId] = 1
        
        for val in ans:
            heapq.heappush(feed, val)
        
        return list(tweetSet.keys())
        

    def follow(self, followerId: int, followeeId: int) -> None:
        followerSet = self.following[followerId]
        if followeeId not in followerSet:
            followerSet.add(followeeId)
            for tweet in self.tweets[followeeId]:
                heapq.heappush(self.feed[followerId], tweet)
        
        self.followers[followeeId].add(followerId)
                

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followeeId].discard(followerId)
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)