"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/design-twitter/description/
"""


class Twitter:

    def __init__(self):
        self.follows = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follows.keys():
            self.follows[userId] = [userId]
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        num = 0
        for tweet in reversed(self.tweets):
            if num >= 10:
                break
            if tweet[0] in self.follows.get(userId, [userId]):
                feed.append(tweet[1])
                num += 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = [followerId]
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (
            followerId in self.follows
            and followeeId in self.follows[followerId]
            and followeeId != followerId
        ):
            self.follows[followerId].remove(followeeId)
