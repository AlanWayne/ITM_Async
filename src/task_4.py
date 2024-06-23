import aiohttp
import asyncio


def clear_log():
    with open("src/task_4.log", "w") as file:
        file.write("")


async def fetch(semaphore: asyncio.Semaphore, url: str):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.request(method="GET", url=url) as response:
                with open("src/task_4.log", "a") as file:
                    file.write(
                        f'status: {response.status} = {response.headers["Date"]}\n'
                    )
            


async def main(request_total: int = 1, request_limit: int = 1, url: str = ""):
    clear_log()
    semaphore = asyncio.Semaphore(request_limit)
    tasks = []
    
    for i in range(request_total):
        tasks.append(fetch(url=url, semaphore=semaphore))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    request_total = 50
    request_limit = 10
    url = "https://example.com/"

    asyncio.run(
        main(
            request_total=request_total,
            request_limit=request_limit,
            url=url,
        )
    )
