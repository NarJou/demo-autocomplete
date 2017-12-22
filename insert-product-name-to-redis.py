import redis
import json

r = redis.StrictRedis(host="35.192.211.192", port=6379, db=0)

with open('product-names.json',"r") as f:
    names = json.load(f)
    for name in names:
        n = name["name"]
        for c in range(1,len(n)):
            prefix = n[0:c]
            r.zadd('names',0,prefix)
        r.zadd('names',0,n+"*")
