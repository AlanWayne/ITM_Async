import sys
sys.path.insert(1, '/home/alex/Programming/Python/ITM_Async/src')
from task_1 import int_div
import cProfile
import pstats
import asyncio


async def profile_time_task_1():
    print("================ Task 1 ================")
    profiler = cProfile.Profile()
    value = 20_000_000

    profiler.enable()
    await int_div(value)
    profiler.disable()

    pstats.Stats(profiler).strip_dirs().sort_stats("time").print_stats()


if __name__ == "__main__":
    asyncio.run(profile_time_task_1())
