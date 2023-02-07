import random
import time

from asyncio_template import logger

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

def single_sort_task(task_ref:str, arr: list) -> dict:

    """
        A single task

    """
    start_time = time.time()
    
    sorted_array = bubble_sort(arr)
    
    end_time = time.time()

    logger.info(
        {
            "task_description": f'{task_ref}',
            "start_time":get_timestamp(start_time),
            "end_time": get_timestamp(end_time),
            "elapsed_time": get_duration(start_time=start_time, end_time=end_time)
        }
    )

    return sorted_array

def nested_sort_tasks(task_ref: str, arrs: list) -> None:

    """
        Execute nested tasks

    """

    start_time = time.time()

    for i in enumerate(arrs):
        single_sort_task(f'{task_ref}:{i[1][0]}', i[1][1])

    end_time = time.time()

    logger.info(
        {
            "task_description": task_ref,
            "start_time":get_timestamp(start_time),
            "end_time": get_timestamp(end_time),
            "elapsed_time": get_duration(start_time=start_time, end_time=end_time)
        }
    )