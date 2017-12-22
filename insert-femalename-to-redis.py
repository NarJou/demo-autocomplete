import redis

r = redis.StrictRedis(host="35.192.211.192", port=6379, db=0)

print "Loading entries in the Redis DB\n"
f = open('female-names-2.txt',"r")
for line in f:
    n = line.strip()
    for l in range(1,len(n)):
        prefix = n[0:l]
        r.zadd('names',0,prefix)
    r.zadd('names',0,n+"*")
