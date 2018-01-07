from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from redis.client import Redis
from feed.model.tweets import Tweets
from feed.model.users import Users
import json
import jsonpickle
from django.template import loader

def index(request):

    count = int(request.GET.get('count',0))
    since_id = request.GET.get('since_id',None)
    format = request.GET.get('format',"html")
    userid = request.GET.get('userid',"1")
    client = Redis(decode_responses=True)

    ru = client.hgetall("user_"+userid)
    li = []
    l = []
    userdata = {}
    p = client.pipeline()
    tweetidlist = ru['tweets'][1:-1].replace(" ","").split(",")
    tweetCount = len(tweetidlist)

    if since_id:
        tweetidlist = tweetidlist[tweetidlist.index(since_id):]
    if count != 0 and count < len(tweetidlist):
        tweetidlist = tweetidlist[:count]
    tweetwords = ["tweet_" + s  for s in tweetidlist]
    for tweetword in tweetwords:
        p.hgetall(tweetword)
    tcount = 0
    for t in p.execute():
        if t["user"] not in userdata:
            userdata[t["user"]] = client.hgetall("user_"+t["user"])
        #tweetstr = tweetidlist[count] + " : " + t["text"] + " by " + userdata[t["user"]]["name"]
        data = {}
        data["tweet"] = t
        data["tweetid"] = tweetidlist[tcount]
        data["username"] = userdata[t["user"]]["name"]
        data["refCount"] = 20

        if t["user"] == userid and count != 0:
            data["refCount"] = count
        l.append(data)
        tcount = tcount + 1
    #rt = client.hgetall("tweet_1")
    #rt1 = client.hgetall("tweet_2")
    #rt2 = client.hgetall("tweet_3")

    # u = Users(name=ru["name"],id=1)
    # t = Tweets(text=rt["text"],user=u, id=1)
    # t1 = Tweets(text=rt1["text"],user=u, id=2)
    # t2 = Tweets(text=rt2["text"],user=u, id=3)

    #l = [rt2,rt1,rt]
    #li = [3,2,1]

    #data = jsonpickle.encode(l,unpicklable=False)

    userinfo = {"name":ru["name"],"userid":userid, "count":count,"nextStart" : tweetidlist[-1]}
    userinfo["tweetCount"] = tweetCount
    userinfo["follows"] = 4


    template = loader.get_template('index.html')
    context = {
        'user': userinfo,
        'tweets': l
    }
    if format.lower() == "json":
        return JsonResponse(context,safe=False)
    return HttpResponse(template.render(context, request))