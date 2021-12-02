# Fixing aioredis-py issue #778

There was a connection reset by peer error that appeared
in redis-py 4.0 and aioredis 2.0. This repository is
attempting to track down where this bug came from in 
redis-py and create a solution.

Run:
1. `docker run --rm -d -p 6379:6379 --name redis redis`
2. `python main.py`
3. Enter Redis CLI: `docker exec -it CONTAINER_ID redis-cli`
4. Get your current client: `CLIENT LIST`. It's going to be the client with
an `addr` does not start with `127.0.0.1`.
5. Kill connection to Python: `CLIENT KILL ADDR ip:port`

TODO: I can't seem to reproduce this error.

### License

Licensed under Apache 2.0

Written by [@Andrew-Chen-Wang](https://github.com/Andrew-Chen-Wang)
