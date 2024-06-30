from src.task_1 import int_div
from src.task_2 import create_files
from src.task_3 import fetch
from src.task_4 import send
import cProfile
import pstats
import asyncio
import sys
import os


async def test_time_task_1(value: int = 1_000_000):
    profiler = cProfile.Profile()
    value = 20_000_000

    profiler.enable()
    sys.stdout = open(os.devnull, "w")

    await int_div(value)

    sys.stdout = sys.__stdout__
    profiler.disable()

    pstats.Stats(profiler).strip_dirs().sort_stats("time").print_stats(10)


async def test_time_task_2(value: int = 10):
    profiler = cProfile.Profile()

    profiler.enable()
    sys.stdout = open(os.devnull, "w")

    create_files(value)

    sys.stdout = sys.__stdout__
    profiler.disable()

    pstats.Stats(profiler).strip_dirs().sort_stats("time").print_stats(10)


async def test_time_task_3(value: int = 10):
    profiler = cProfile.Profile()
    url = "http://google.com/"
    semaphore = asyncio.Semaphore(value)
    tasks = []

    profiler.enable()
    sys.stdout = open(os.devnull, "w")

    for i in range(10):
        tasks.append(fetch(url=url, semaphore=semaphore))
    await asyncio.gather(*tasks)

    sys.stdout = sys.__stdout__
    profiler.disable()

    pstats.Stats(profiler).strip_dirs().sort_stats("time").print_stats(10)


async def test_time_task_4(value: int = 10):
    profiler = cProfile.Profile()
    request_total = value
    request_limit = request_total // 3
    url = "https://example.com/"

    profiler.enable()
    sys.stdout = open(os.devnull, "w")

    await send(
        request_total=request_total,
        request_limit=request_limit,
        url=url,
    )

    sys.stdout = sys.__stdout__
    profiler.disable()

    pstats.Stats(profiler).strip_dirs().sort_stats("time").print_stats(10)


if __name__ == "__main__":
    arg1 = sys.argv[1] if len(sys.argv) > 1 else 1

    print("\n\033[91m ======== [START] ======== \033[0m\n")

    if arg1 == "1":
        asyncio.run(
            test_time_task_1(sys.argv[2] if len(sys.argv) > 2 else 1_000_000),
        )
    elif arg1 == "2":
        asyncio.run(
            test_time_task_2(sys.argv[2] if len(sys.argv) > 2 else 10),
        )
    elif arg1 == "3":
        asyncio.run(
            test_time_task_3(sys.argv[2] if len(sys.argv) > 2 else 10),
        )
    elif arg1 == "4":
        asyncio.run(
            test_time_task_4(sys.argv[2] if len(sys.argv) > 2 else 10),
        )
    else:
        print("Usage: python time_profile.py [index] [value:optional]")
