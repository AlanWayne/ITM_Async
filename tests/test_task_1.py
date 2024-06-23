from src.task_1 import int_div
import pytest


@pytest.mark.asyncio
async def test_task_1_1():
    value = 1_000_001
    expected_result = [101, 9901]
    actual_result = await int_div(value)

    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_task_1_2():
    value = 1_000_003
    expected_result = []
    actual_result = await int_div(value)

    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_task_1_3():
    value = 19_999_997
    expected_result = [59, 257, 1319, 15163, 77821, 338983]
    actual_result = await int_div(value)

    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_task_1_4():
    value = 999_999
    expected_result = None
    actual_result = await int_div(value)

    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_task_1_5():
    value = 20_000_001
    expected_result = None
    actual_result = await int_div(value)

    assert expected_result == actual_result
