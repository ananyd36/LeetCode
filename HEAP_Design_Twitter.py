# Design Twitter
# Solved 
# Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

# Users and tweets are uniquely identified by their IDs (integers).

# Implement the following methods:

# Twitter() Initializes the twitter object.
# void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
# List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.
# Example 1:

# Input:
# ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]

# Output:
# [null, null, null, [10], [20], null, [20, 10], [20], null, [10]]

# Explanation:
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 10); // User 1 posts a new tweet with id = 10.
# twitter.postTweet(2, 20); // User 2 posts a new tweet with id = 20.
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
# twitter.getNewsFeed(2);   // User 2's news feed should only contain their own tweets -> [20].
# twitter.follow(1, 2);     // User 1 follows user 2.
# twitter.getNewsFeed(1);   // User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
# twitter.getNewsFeed(2);   // User 2's news feed should still only contain their own tweets -> [20].
# twitter.unfollow(1, 2);   // User 1 follows user 2.
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].


class Twitter:

    def __init__(self):
        self.database = {}
        self.tweet_order = 1000      

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_order -= 1
        if userId not in self.database:
            self.database[userId] = [[],[]] # one for tweets other for followers
        self.database[userId][0].append((self.tweet_order, tweetId))

    
    def getUsertweets(self, userId: int) -> List[int]:
        if userId not in self.database:
            return []
        return self.database[userId][0]

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.database:
            return []
        # collecting all tweets from user and follower
        user_tweets = self.database[userId][0]
        follower_tweets = []
        followers = self.database[userId][1]
        for followerId in followers:
            if followerId == userId:
                continue
            follower_tweets.append(self.getUsertweets(followerId))

        #creating a maxHeap
        flat_follo_tweets = [tweet for sublist in follower_tweets for tweet in sublist]
        total_tweets = flat_follo_tweets + user_tweets
        heapq.heapify(total_tweets)

        #retreiving the top 10 tweets or less from the heap
        i = 0
        res = []
        while i < 10 and total_tweets:
            res.append(heapq.heappop(total_tweets)[1]) # only appending tweetId
            #return the tweets in a most recent manner
            i+=1
        return res
        
    # adding follower to the database map
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.database:
            self.database[followerId] = [[],[]]
        if followeeId in self.database[followerId][1]:
            return
        self.database[followerId][1].append(followeeId)

    # removing follower from the database map
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.database:
            return
        else:
            if followeeId not in self.database[followerId][1]:
                return
            self.database[followerId][1].remove(followeeId)
