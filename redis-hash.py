import redis

if __name__ == '__main__':
    rediscon = redis.StrictRedis(
        host='localhost',
        port=6379
    )
    vals = {"name": "joe", "test": 0}
    i=0
    #rediscon.flushall()

    while i<100:
        vals.update({"test": str(i)})
        key=str(i)
        rediscon.hmset(i, vals)
        i+=1

