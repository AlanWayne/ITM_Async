import pytest
from src.task_4 import send
from os import remove


@pytest.mark.asyncio
async def test_task_4_1():
    request_total = 5
    request_limit = 5
    url = "https://example.com/"

    status_expected = [200, 200, 200, 200, 200]
    status_actual = await send(
        request_total=request_total, request_limit=request_limit, url=url
    )

    assert status_expected == status_actual


@pytest.mark.asyncio
async def test_task_4_2():
    request_total = 5
    lines = []

    with open("log/task_4.log", "r") as file:
        lines = file.readlines()

    record_total = 0
    for line in lines:
        if line.count("status: 200") == 1:
            record_total += 1

    assert request_total == record_total
