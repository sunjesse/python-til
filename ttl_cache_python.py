from cachetools.func import ttl_cache
from threading import Thread
import time

@ttl_cache(maxsize=100, ttl=60)
def get_data():
    time.sleep(1) # simulating a network call
    print("YOOO I RAN")
    return 10

threads = []

for _ in range(10):
    threads.append(Thread(target=get_data))

for t in threads:
    t.start()

for t in threads:
    t.join()

# stdout "YOOO I RAN" only fires once.
# This tells us a few things:
# - ttl_cache is thread-safe.
# - once subsequent threads get their turn at the lock, they will first check
#   to see if there is a cache hit, unlock, and then return.
# - this is a nice decorator to use to easily ttl cache network calls, for example.
