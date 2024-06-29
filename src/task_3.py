import aiohttp
import asyncio


async def fetch(semaphore: asyncio.Semaphore, url: str):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.request(method="GET", url=url) as response:
                if response.status == 200:
                    print(f'\033[92m{response.headers["Date"]}\033[0m')
                else:
                    print(f'\033[91m{response.headers["Date"]}\033[0m')

                return response.status


async def main():
    url = "http://google.com/"
    semaphore = asyncio.Semaphore(4)
    tasks = []

    for i in range(16):
        tasks.append(fetch(url=url, semaphore=semaphore))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
