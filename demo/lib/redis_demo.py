import redis

rdc = redis.Redis(host='192.168.0.201', port=6379)


def get_set(rc: redis.Redis):
    key = 'name'
    value = 'LiLei'
    rc.delete(key)
    rc.set(name=key, value=value, ex=1)
    print(str(rc.get(key), encoding='UTF-8'))


def expire_ttl(rc: redis.Redis):
    key = 'test_ttl'
    rc.delete(key)
    time = 1
    rc.set(key, '')
    rc.expire(key, time)
    print(rc.ttl(key))
    print(rc.pttl(key))


def redis_list(rc: redis.Redis):
    key = 'test_list'
    rc.delete(key)
    print('' + str(rc.llen(key)))
    rc.lpush(key, 2)
    rc.lpush(key, 1)
    rc.rpush(key, 3)
    rc.rpush(key, 4)
    print(rc.llen(key))
    print(rc.lindex(key, 0))
    print(rc.lrange(key, 0, -1))
    print(rc.lrange(key, 1, -1))
    print(rc.lpop(key))
    print(rc.brpop(key))


def redis_set(rc: redis.Redis):
    key = 'test_set'
    rc.delete(key)
    rc.zadd(key, {'a': 2})
    rc.zadd(key, {'a': 2})
    rc.zadd(key, {'c': 3})
    rc.zadd(key, {'d': 4})
    print(rc.zcount(key, 0, 100))
    print(rc.zrange(key, 0, -1))


get_set(rdc)
expire_ttl(rdc)
redis_list(rdc)
redis_set(rdc)
