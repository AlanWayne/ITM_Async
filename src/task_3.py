import aiohttp
import asyncio

url = "http://google.com/"


async def fetch(semaphore: asyncio.Semaphore, id: int = 1):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.request(method="GET", url=url) as response:
                if response.status == 200:
                    print(f'{id}: \033[92m{response.headers["Date"]}\033[0m')
                else:
                    print(f'{id}: \033[91m{response.headers["Date"]}\033[0m')

                await asyncio.sleep(1)


async def main():
    limit = 10
    semaphore = asyncio.Semaphore(limit)
    tasks = []

    for i in range(1, 51):
        tasks.append(fetch(semaphore, i % limit + 1))

    await asyncio.gather(*tasks)


asyncio.run(main())
