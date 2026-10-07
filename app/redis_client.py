import os
import redis

def get_redis():
    return redis.Redis.from_url(
        os.getenv("REDIS_URL", "redis://localhost:6379/0"),
        decode_responses=True
    )
