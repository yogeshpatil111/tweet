from redis.client import Redis
import random
import uuid
from feed.model.tweets import Tweets
from feed.model.users import Users

client = Redis()
users = {1:{"name":"Yogesh"},2:{"name":"Charles"},3:{"name":"Bob"},4:{"name":"Alice"},5:{"name":"Tom"}}
userfollowermap = {1:[1,2,3,4,5],2:[1,2,3,4],3:[3,4,5],4:[1,2,3,5,5],5:[1,2,3,5]}

usertweets = {1:{},2:{},3:{},4:{},5:{}}
userorderedtweets = {1:[],2:[],3:[],4:[],5:[]}

for j in range(1,6):
    rantimestamp= []
    tweetcount = random.randint(5,200)
    rantimestamp = random.sample(range(1, 500), tweetcount+1)
    rantimestamp.sort(reverse=True)
    for i in range(1,tweetcount+1):
        tweetid = uuid.uuid4().int
        timeorder = rantimestamp[i]
        client.hmset("tweet_"+str(tweetid),{"text":"Tweet Time Order "+ str(timeorder),"user":j})
        for follower in userfollowermap[j]:
            timeorderedTweets = []
            if timeorder in usertweets[follower]:
                timeorderedTweets = usertweets[follower][timeorder]
            timeorderedTweets.append({"id":tweetid})
            usertweets[follower][timeorder] = timeorderedTweets

for user in usertweets:
    timeotweets = list(usertweets[user].keys())
    timeotweets.sort(reverse=True)
    finaltweets = []
    for tweetto in timeotweets:
        for id in usertweets[user][tweetto]:
            finaltweets.append(id['id'])
    userorderedtweets[user] = finaltweets

for u in users:
    client.hmset("user_"+str(u),{"name":users[u]["name"],"tweets":userorderedtweets[u]})

# client.hmset("user_1",{"name":"yogesh"})
# client.hmset("tweet_1",{"text":"first Tweet!","user":1})
# client.hmset("tweet_2",{"text":"Second Tweet!","user":1})
# client.hmset("tweet_3",{"text":"Third Tweet!","user":1})