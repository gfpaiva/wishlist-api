from os import getenv
import redis


redis = redis.Redis(
    host=getenv('CACHE_HOST', 'localhost'),
    port=getenv('CACHE_PORT', 6379),
    password=getenv('CACHE_PASSWORD', None),
    db=0,
)
