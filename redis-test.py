import redis
import time

if __name__ == '__main__':
    rediscon = redis.Redis(
        host='localhost',
        port=6379
    )
    vals = []
    i=0
    rediscon.flushall()
    start = time.time()

    while i<100000:
        #rediscon.lpush('vatest', i)
        rediscon.set(i, i)
        i+=1
    endtime = time.time()
    print(str(endtime-start))
    print(str('Done writing keys'))
    print(str('Random access test'))
    #i=0
    #while i<10000:
        #vals.append(rediscon.get(i))
    #    val=rediscon.lpop('test')
    #    print(str(val))
    #    i+=100
    #print(vals)

