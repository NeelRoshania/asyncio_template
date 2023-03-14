import asyncio
import random
import logging
import time

LOGGER = logging.getLogger(__name__) # python_template

def bubble_sort(arr: list) -> list:
    
    """
        bubble sort implementation
            - https://www.programiz.com/dsa/bubble-sort

    """

    # loop to access each array element
    for i in range(len(arr)):

        # loop to compare array elements
        for j in range(0, len(arr) - i - 1):

            # compare two adjacent elements - change > to < to sort in descending order
            if arr[j] > arr[j + 1]:

                # swapping elements if elements are not in the intended order
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

def get_duration(start_time, end_time) -> float:

    """
        Calculate duration in seconds

        start_time:  time in seconds since the epoch as a floating point number
        end_time:  time in seconds since the epoch as a floating point number

    """
    return f'{end_time-start_time:.2f}s'

def get_timestamp(eseconds:float) -> str:

    """
        Returns specified timestamp from epoch seconds
        https://docs.python.org/3.9/library/time.html#time.gmtime

    """

    return time.strftime("%Y%M%d %X", time.gmtime(eseconds))

async def single_sort_task(task_ref:str, arr: list) -> dict:

    """
        A single task - this is compute bound and will block the thread!

    """
    start_time = time.time()
    LOGGER.info(f'starting task: {task_ref}')
    
    sorted_array = await bubble_sort(arr) # this blocks because it is compute bound
    
    end_time = time.time()

    return {
        "task_description": f'{task_ref}',
        "start_time":get_timestamp(start_time),
        "end_time": get_timestamp(end_time),
        "elapsed_time": get_duration(start_time=start_time, end_time=end_time)
    }

async def nested_sort_tasks(task_ref: str, arrs: list) -> None:

    """
        Execute nested tasks - this is compute bound and will block the thread!

    """

    start_time = time.time()

    for i in enumerate(arrs):
        await single_sort_task(f'{task_ref}:{i[1][0]}', i[1][1])

    end_time = time.time()

    LOGGER.info(
        {
            "task_description": task_ref,
            "start_time":get_timestamp(start_time),
            "end_time": get_timestamp(end_time),
            "elapsed_time": get_duration(start_time=start_time, end_time=end_time)
        }
    )

async def non_compute_bound(task_ref:str, arr: list) -> dict:

    """
        A single task

    """
    start_time = time.time()
    LOGGER.info(f'starting task: {task_ref}')
    
    await asyncio.sleep(3)
    
    end_time = time.time()

    return {
        "task_description": f'{task_ref}',
        "start_time":get_timestamp(start_time),
        "end_time": get_timestamp(end_time),
        "elapsed_time": get_duration(start_time=start_time, end_time=end_time)
    }