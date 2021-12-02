import redis
import aioredis
import asyncio, time

class SRedis(redis.Redis):
    ...

def main_sync():
    redis = SRedis()
    redis.set("sync", "something")
    while Trye:
        redis.get("sync")
        time.sleep(5)


class ARedis(aioredis.Redis):
    ...

async def main_async():
    redis = ARedis()
    await redis.set("async", "something")

    while True:
        await redis.get("async")
        await asyncio.sleep(5)


if __name__ == "__main__":
    main_sync()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_async())
