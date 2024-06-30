from src.task_1 import int_div
from src.task_2 import create_files
from src.task_3 import fetch
from src.task_4 import send
import asyncio
import tracemalloc
import sys


def color_output(string: str) -> str:
    if len(string) == 0:
        return "\033[90m" + "Memory profiler" + "\033[0m"

    if string.find("ITM") != -1:
        return "\033[92m" + string + "\033[0m"

    if string.find("async") != -1 or string.find("thread") != -1:
        return "\033[94m" + string + "\033[0m"

    if string.find("logging") != -1:
        return "\033[93m" + string + "\033[0m"

    if string.find("http") != -1:
        return "\033[95m" + string + "\033[0m"

    return "\033[97m" + string + "\033[0m"


def printc(stats: list[tracemalloc.Statistic]) -> None:
    for s in stats[:40]:
        output = color_output(str(s))
        print(output)


def test_mem_task_1(value: int = 1_000_000) -> None:
    asyncio.run(int_div(value))


def test_mem_task_2(value: int = 10) -> None:
    create_files(value)


async def test_mem_task_3(value: int = 10) -> None:
    url = "http://google.com/"
    semaphore = asyncio.Semaphore(value)
    tasks = []

    for i in range(value):
        tasks.append(fetch(url=url, semaphore=semaphore))
    await asyncio.gather(*tasks)


async def test_mem_task_4(value: int = 10) -> None:
    request_total = value
    request_limit = request_total // 3
    url = "https://example.com/"

    await send(
        request_total=request_total,
        request_limit=request_limit,
        url=url,
    )


if __name__ == "__main__":
    arg1 = sys.argv[1] if len(sys.argv) > 1 else 1
    tracemalloc.start()

    print("\n\033[91m ======== [START] ======== \033[0m\n")

    if arg1 == "1":
        test_mem_task_1(sys.argv[2] if len(sys.argv) > 2 else 1_000_000)
    elif arg1 == "2":
        test_mem_task_2(sys.argv[2] if len(sys.argv) > 2 else 10)
    elif arg1 == "3":
        asyncio.run(test_mem_task_3(sys.argv[2] if len(sys.argv) > 2 else 10))
    elif arg1 == "4":
        asyncio.run(test_mem_task_4(sys.argv[2] if len(sys.argv) > 2 else 10))
    else:
        print("Usage: python mem_profile.py [index] [value:optional]")

    printc(tracemalloc.take_snapshot().statistics("traceback"))
    tracemalloc.stop()
