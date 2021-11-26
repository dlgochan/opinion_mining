import tweepy
import json

consumer_key = 'kVY7INg6jazHWIMB9frQp5Ouq'
consumer_secret = 'iKWYLCSAnafWSsEN5GOseSnLZAQsMPYAmLRnkK5YhY2InCDTa4'
access_token = '1434698789084745728-zDYXbUNkzG3Hdm2XtMlHSLuOyPIQoT'
access_token_secret = '8in88M4QwrwvXiq6jvYfiJfbakkiPGd6pIxhCHDbXTPGP'
tweetsPerQry = 100
maxTweets = 100000
# search = "(백신패스 OR 위드코로나 OR 단계적일상회복) -filter:retweets"
search = "(아 OR 요 OR 그 OR 하 OR 그 OR 저) -filter:retweets"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#(위드코로나 OR 단계적일상회복) lang:ko -filter:links
f = open("./other.json", mode='w')     # 쓰기 모드
# f = open("./twitter.json", mode='a')     # 쓰기 모드

# minId = 1462531432316686338 # 새로운 위드코로나 트윗 긁을 때 안 겹치게 할라고
minId = 0
maxId = -1
tweetCount = 0
while tweetCount < maxTweets:
    if(maxId <= 0):
        newTweets = api.search_tweets(q=search, count=tweetsPerQry, result_type="recent", tweet_mode="extended")
    else:
        newTweets = api.search_tweets(q=search, lang="ko", count=tweetsPerQry, max_id=str(maxId - 1), result_type="recent", tweet_mode="extended")
    if not newTweets:
        print("Tweet Habis")
        break

    for tweet in newTweets:
        if(tweet._json['id'] > minId):
            print(tweet._json['full_text'])
            f.write(json.dumps(tweet._json))
            f.write('\n')

    tweetCount += len(newTweets)
    maxId = newTweets[-1].id

f.close()

