import sys
sys.path.insert(1, '/home/alex/Programming/Python/ITM_Async/src')
from task_2 import create_files
import cProfile
import pstats
import asyncio


async def profile_time_task_2():
    print("================ Task 2 ================")
    profiler = cProfile.Profile()

    profiler.enable()
    create_files(1000)
    profiler.disable()

    pstats.Stats(profiler).strip_dirs().sort_stats("time").print_stats(10)


if __name__ == "__main__":
    asyncio.run(profile_time_task_2())
