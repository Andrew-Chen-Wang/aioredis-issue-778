import redis
import aioredis
import asyncio, time

class SRedis(redis.Redis):
    ...

def main_sync():
    r = SRedis()
    assert r.set("sync", "something")
    while True:
        print(r.get("sync") == b'something')
        time.sleep(5)


class ARedis(aioredis.Redis):
    ...

async def main_async():
    r = ARedis()
    assert await r.set("async", "something")
    while True:
        print((await r.get("async")) == b"something")
        await asyncio.sleep(5)


if __name__ == "__main__":
    main_sync()
    # asyncio.get_event_loop().run_until_complete(main_async())
