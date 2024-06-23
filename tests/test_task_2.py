from src.task_2 import create_files
import pytest
from os import listdir

@pytest.mark.asyncio
async def test_task_2_1():
    number_of_files = 10
    create_files(number_of_files)
    files = listdir("text/")
    files.sort()
    
    number_of_files_comfirmed = len(files)
    
    right_names_confirmed = 0
    
    for index, file in enumerate(files):
        if file == f"file_{index}.txt":
            right_names_confirmed += 1

    assert number_of_files == number_of_files_comfirmed
    assert number_of_files == right_names_confirmed

