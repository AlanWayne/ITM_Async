import pytest
import asyncio
from src.task_3 import fetch


@pytest.mark.asyncio
async def test_task_3_1():
    url = "http://google.com/"
    semaphore = asyncio.Semaphore(10)
    tasks = []

    for i in range(10):
        tasks.append(fetch(url=url, semaphore=semaphore))

    status_expected = [200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
    status_actual = await asyncio.gather(*tasks)

    assert status_expected == status_actual
