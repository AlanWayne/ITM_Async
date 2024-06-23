import sys

sys.path.insert(1, "/home/alex/Programming/Python/ITM_Async/src")
from task_4 import send
import cProfile
import pstats
import asyncio


async def profile_time_task_4():
    print("================ Task 4 ================")
    profiler = cProfile.Profile()
    request_total = 10
    request_limit = 5
    url = "https://example.com/"

    profiler.enable()
    await send(request_total=request_total, request_limit=request_limit, url=url)
    profiler.disable()

    pstats.Stats(profiler).strip_dirs().sort_stats("time").print_stats(10)


if __name__ == "__main__":
    asyncio.run(profile_time_task_4())
