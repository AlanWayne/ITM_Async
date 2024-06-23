import sys
sys.path.insert(1, '/home/alex/Programming/Python/ITM_Async/src')
from task_3 import fetch
import cProfile
import pstats
import asyncio


async def profile_time_task_3():
    print("================ Task 3 ================")
    profiler = cProfile.Profile()
    url = "http://google.com/"
    semaphore = asyncio.Semaphore(10)
    tasks = []

    profiler.enable()
    for i in range(10):
        tasks.append(fetch(url=url, semaphore=semaphore))
    await asyncio.gather(*tasks)

    profiler.disable()

    pstats.Stats(profiler).strip_dirs().sort_stats("time").print_stats(10)


if __name__ == "__main__":
    asyncio.run(profile_time_task_3())
