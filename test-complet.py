import redis

r = redis.StrictRedis(host="35.224.255.11", port=6379, db=0)
#print "Loading entries in the Redis DB\n"
#f = open('female-names-2.txt',"r")
#for line in f:
#    n = line.strip()
#    for l in range(1,len(n)):
#        prefix = n[0:l]
#        r.zadd('compl',0,prefix)
#    r.zadd('compl',0,n+"*")

def complete(r,prefix,count):
    results = []
    rangelen = 50 # This is not random, try to get replies < MTU size
    start = r.zrank('compl',prefix)
    if not start:
         return []
    while (len(results) != count):
         range = r.zrange('compl',start,start+rangelen-1)
         start += rangelen
         if not range or len(range) == 0:
             break
         for entry in range:
             minlen = min(len(entry),len(prefix))
             if entry[0:minlen] != prefix[0:minlen]:
                count = len(results)
                break
             if entry[-1] == "*" and len(results) != count:
                results.append(entry[0:-1])

    return results

def autoComplete():
    print complete(r,"abig",50)

if __name__ == "__main__":
    autoComplete()
