import os
import redis

REDISTOGO_URL ='redis://redistogo:62c409306bc4ac84542b88a8743ce09e@greeneye.redistogo.com:10445/'
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)